# Prepared the document
doc1 = "あなたは問題を解決することが大好きです。"
doc2 = "あなたは問題を解決することが好きです。"

# import math
# math.log(1024)

def tf_idf(t, d):
    """
    >>> tf_idf("あなた", {})
    1
    """
    return tf(t, d) * idf(t)

def tf(t, d):
    # TODO
    return 1

def idf(t):
    # TODO
    return 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
