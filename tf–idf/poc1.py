import collections
import itertools
import math

# Prepared the document
# Quoted by https://makitani.net/shimauma/coe
docs = [d.split("/") for d in [
    "CoE/と/は/、/Center/ /of/ /Excellence/（/センター/・/オブ/・/エクセレンス/）/の/略",
    "横断/組織/、/中央/組織/、/横断/基盤/の/こと/。",
    "人材/や/ノウハウ/、/ツール/など/を/集約/した/横断組織/を/「/CoE/」/「/センター/・/オブ/・/エクセレンス/」/と/呼ぶ/こと/が/増え/て/いる/。",
]]

def tf_idf(t, d):
    """
    >>> t = "今日"
    >>> d = "今日/は/雨/が/降っ/て/い/ます/。".split("/")
    >>> tf_idf(t, d)
    0.12206803207423442
    """
    return tf(t, d) * idf(t)

def tf(t, d):
    """
    >>> doc = "雨/は/コーラ/ が/飲め/ない".split("/")
    >>> tf("雨", doc)
    0.16666666666666666
    >>> tf("コーラ", doc)
    0.16666666666666666
    """
    words = collections.Counter(d)
    return words[t] / sum(words.values())

def idf(t):
    """
    >>> idf("雨")
    0.0
    >>> idf("コーラ")
    1.0986122886681098
    """
    D = len(docs)
    df = collections.Counter([t in doc for doc in docs])[True]
    return math.log(D / df)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    word_vectors = set(itertools.chain.from_iterable(docs))
    feature_vectors = [[
        tf_idf(word, doc) for word in word_vectors
    ] for doc in docs]

    import pprint
    pprint.pprint(feature_vectors)
    pprint.pprint(word_vectors)

    def euclidean_distance(vec1, vec2):
        return math.sqrt(math.fabs(sum([q - p for q,p in zip(vec1, vec2)])))

    print("0->1", euclidean_distance(feature_vectors[0], feature_vectors[1]))
    print("0->2", euclidean_distance(feature_vectors[0], feature_vectors[2]))
    print("1->2", euclidean_distance(feature_vectors[1], feature_vectors[2]))

