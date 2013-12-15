import re
import docclass


def sample_train(classifier):
    classifier.train('Nobody owns the watter.', 'good')
    classifier.train('the quick rabbit jumps fences', 'good')
    classifier.train('buy pharmaceuticals now', 'bad')
    classifier.train('make quick money at the online casino', 'bad')
    classifier.train('the quick brown fox jumps', 'good')


def getwords(doc):
    splitter = re.compile('\\W*')
    words = [s.lower() for s in splitter.split(doc)
             if len(s) > 2 and len(s) < 20]
    return dict([(w, 1) for w in words])

if __name__ == '__main__':
    #TODO: 1
    print("====")
    classifier = docclass.Classifier(getwords)
    sample_train(classifier)
    print(classifier.weighted_probability(
        'money', 'good', classifier.feature_probability))
    sample_train(classifier)
    print(classifier.weighted_probability(
        'money', 'good', classifier.feature_probability))
    print(classifier.feature_probability('quick', 'good'))

    #TODO: 2
    print("====")
    classifier = docclass.NaiveBayes(getwords)
    sample_train(classifier)
    print(classifier.probability('quick rabbit', 'good'))
    print(classifier.probability('quick rabbit', 'bad'))

    #TODO: 3
    print("====")
    classifier = docclass.NaiveBayes(getwords)
    sample_train(classifier)
    print(classifier.classify('quick rabbit', default="unknown"))
    print(classifier.classify('quick money', default="unknown"))
    classifier.set_threshold('bad', 3.0)
    print(classifier.classify('quick money', default="unknown"))
    for i in range(10):
        sample_train(classifier)
    print(classifier.classify('quick money', default="unknown"))
