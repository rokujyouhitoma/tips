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
    0.0
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
    0.0
    """
    D = len(docs)
    df = collections.Counter([t in doc for doc in docs])[True]
    if df == 0:
        return 0.0
    return math.log(D / df)


def euclidean_distance(vec1, vec2):
    return math.sqrt(math.fabs(sum([q - p for q,p in zip(vec1, vec2)])))

def cosine_similarity(vec1, vec2):
    """
    >>> v1 = [1, 1, 1, 0, 0]
    >>> v2 = [0, 1, 1, 1, 0]
    >>> v3 = [1, 1, 0, 0, 1]
    >>> cosine_similarity(v1, v2)
    0.6666666666666667
    >>> cosine_similarity(v1, v3)
    0.6666666666666667
    >>> cosine_similarity(v2, v3)
    0.33333333333333337
    """
    return sum([a*b for a,b in zip(vec1, vec2)]) / (math.sqrt(sum(vec1)) * math.sqrt(sum(vec2)))


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

    print("Euclidean Distance")
    print("0->0", 1 - euclidean_distance(feature_vectors[0], feature_vectors[0]))
    print("0->1", 1 - euclidean_distance(feature_vectors[0], feature_vectors[1]))
    print("0->2", 1 - euclidean_distance(feature_vectors[0], feature_vectors[2]))
    print("1->0", 1 - euclidean_distance(feature_vectors[1], feature_vectors[0]))
    print("1->1", 1 - euclidean_distance(feature_vectors[1], feature_vectors[1]))
    print("1->2", 1 - euclidean_distance(feature_vectors[1], feature_vectors[2]))
    print("2->0", 1 - euclidean_distance(feature_vectors[2], feature_vectors[0]))
    print("2->1", 1 - euclidean_distance(feature_vectors[2], feature_vectors[1]))
    print("2->2", 1 - euclidean_distance(feature_vectors[2], feature_vectors[2]))

    #print("Cosine Similarity")
    print("0->0", 1 - cosine_similarity(feature_vectors[0], feature_vectors[0]))
    print("0->1", 1 - cosine_similarity(feature_vectors[0], feature_vectors[1]))
    print("0->2", 1 - cosine_similarity(feature_vectors[0], feature_vectors[2]))
    print("1->2", 1 - cosine_similarity(feature_vectors[1], feature_vectors[2]))
