from janome.tokenizer import Tokenizer
import math
import pprint


def tokenize(doc):
    t = Tokenizer()
    tokens = t.tokenize(doc)
    return (token.surface for token in tokens)


def normalize(s):
    return s.lower()


def stopword(s):
    stop_words = tuple('（）、') + tuple([chr(i) for i in range(12353, 12436)])
    return s in stop_words


def getwords(doc):
    return dict([(normalize(s), 1) for s in tokenize(doc) if not stopword(s)])


class classifier:
    def __init__(self, getfeatures):
        self.fc = {}
        self.cc = {}
        self.getfeatures = getfeatures
        self.con = None

    def fc_all(self):
        res = self.con.execute("select * from fc").fetchall()
        pprint.pprint(res)
        return res

    def flush_database(self):
        self.con.execute("DROP TABLE IF EXISTS fc;")
        self.con.execute("DROP TABLE IF EXISTS cc;")
        self.init_db()

    def cc_all(self):
        res = self.con.execute("select * from cc").fetchall()
        pprint.pprint(res)
        return res

    def setdb(self, db_uri):
        self.db_uri = db_uri

    def init_db(self):
        self.con.execute("create table if not exists fc(feature,category,count)")
        self.con.execute("create table if not exists cc(category,count)")

    def incf(self, f, cat):
        count = self.fcount(f, cat)
        if count == 0:
            self.con.execute("insert into fc values ('%s','%s',1)" % (f, cat))
        else:
            self.con.execute(
                "update fc set count=%d where feature='%s' and category='%s'"
                % (count + 1, f, cat)
            )

    def fcount(self, f, cat):
        res = self.con.execute(
            'select count from fc where feature="%s" and category="%s"' % (f, cat)
        ).fetchone()
        if res == None:
            return 0
        else:
            return float(res[0])

    def incc(self, cat):
        count = self.catcount(cat)
        if count == 0:
            self.con.execute("insert into cc values ('%s',1)" % (cat))
        else:
            self.con.execute(
                "update cc set count=%d where category='%s'" % (count + 1, cat)
            )

    def catcount(self, cat):
        res = self.con.execute(
            'select count from cc where category="%s"' % (cat)
        ).fetchone()
        if res == None:
            return 0
        else:
            return float(res[0])

    def categories(self):
        cur = self.con.execute("select category from cc")
        return [d[0] for d in cur]

    def totalcount(self):
        res = self.con.execute("select sum(count) from cc").fetchone()
        if res == None:
            return 0
        return res[0]

    def train(self, item, cat):
        features = self.getfeatures(item)
        for f in features:
            self.incf(f, cat)

        self.incc(cat)
        self.con.commit()

    def fprob(self, f, cat):
        if self.catcount(cat) == 0:
            return 0

        return self.fcount(f, cat) / self.catcount(cat)

    def weightedprob(self, f, cat, prf, weight=1.0, ap=0.5):
        basicprob = prf(f, cat)

        totals = sum([self.fcount(f, c) for c in self.categories()])

        bp = ((weight * ap) + (totals * basicprob)) / (weight + totals)
        return bp


class naivebayes(classifier):
    def __init__(self, getfeatures):
        classifier.__init__(self, getfeatures)
        self.thresholds = {}

    def docprob(self, item, cat):
        features = self.getfeatures(item)
        p = 1
        for f in features:
            p *= self.weightedprob(f, cat, self.fprob)
        return p

    def prob(self, item, cat):
        catprob = self.catcount(cat) / self.totalcount()
        docprob = self.docprob(item, cat)
        return docprob * catprob

    def setthreshold(self, cat, t):
        self.thresholds[cat] = t

    def getthreshold(self, cat):
        if cat not in self.thresholds:
            return 1.0
        return self.thresholds[cat]

    def classify(self, item, default=None):
        probs = {}
        max = 0.0
        for cat in self.categories():
            probs[cat] = self.prob(item, cat)
            pprint.pprint(probs)
            if probs[cat] > max:
                max = probs[cat]
                best = cat

        for cat in probs:
            if cat == best:
                continue
            if probs[cat] * self.getthreshold(best) > probs[best]:
                return default
        return best


class fisherclassifier(classifier):
    def cprob(self, f, cat):
        clf = self.fprob(f, cat)
        if clf == 0:
            return 0

        freqsum = sum([self.fprob(f, c) for c in self.categories()])

        p = clf / (freqsum)

        return p

    def fisherprob(self, item, cat):
        p = 1
        features = self.getfeatures(item)
        for f in features:
            p *= self.weightedprob(f, cat, self.cprob)

        fscore = -2 * math.log(p)

        return self.invchi2(fscore, len(features) * 2)

    def invchi2(self, chi, df):
        m = chi / 2.0
        sum = term = math.exp(-m)
        for i in range(1, df // 2):
            term *= m / i
            sum += term
        return min(sum, 1.0)

    def __init__(self, getfeatures):
        classifier.__init__(self, getfeatures)
        self.minimums = {}

    def setminimum(self, cat, min):
        self.minimums[cat] = min

    def getminimum(self, cat):
        if cat not in self.minimums:
            return 0
        return self.minimums[cat]

    def classify(self, item, default=None):
        best = default
        max = 0.0
        for c in self.categories():
            p = self.fisherprob(item, c)
            print(c, p)
            if p > self.getminimum(c) and p > max:
                best = c
                max = p
        return best


if __name__ == "__main__":

    def sample_traning(nb):
        nb.train(
            "abc",
            "alphabet",
        )
        nb.train(
            "123",
            "number",
        )

    cl = fisherclassifier(getwords)
    cl.setdb(":memory:")
    sample_traning(cl)
    print(cl.classify("890"))
