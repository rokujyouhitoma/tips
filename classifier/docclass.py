import math


class Classifier:
    def __init__(self, getfeatures, filename=None):
        self.feature_count_dict = {}
        self.category_count_dict = {}
        self.getfeatures = getfeatures

    def increase_feature(self, feature, category):
        self.feature_count_dict.setdefault(feature, {})
        self.feature_count_dict[feature].setdefault(category, 0)
        self.feature_count_dict[feature][category] += 1

    def increase_category(self, category):
        self.category_count_dict.setdefault(category, 0)
        self.category_count_dict[category] += 1

    def feature_count(self, feature, category):
        if feature in self.feature_count_dict:
            if category in self.feature_count_dict[feature]:
                return float(self.feature_count_dict[feature][category])
        return 0.0

    def category_count(self, category):
        if category in self.category_count_dict:
            return float(self.category_count_dict[category])
        return 0

    def total_count(self):
        return sum(self.category_count_dict.values())

    def categories(self):
        return self.category_count_dict.keys()

    def train(self, item, category):
        features = self.getfeatures(item)
        for feature in features:
            self.increase_feature(feature, category)
        self.increase_category(category)

    def feature_probability(self, feature, category):
        category_count = self.category_count(category)
        if category_count == 0:
            return 0
        return self.feature_count(feature, category) / category_count

    def weighted_probability(self, feature, category, probability_function,
                             weight=1.0, ap=0.5):
        basic_probability = probability_function(feature, category)
        categories = self.categories()
        totals = sum(
            [self.feature_count(feature, category) for category in categories])
        b_probability = ((weight * ap) + (totals * basic_probability)) / (
            weight + totals)
        return b_probability


class NaiveBayes(Classifier):
    def __init__(self, getfeatures):
        Classifier.__init__(self, getfeatures)
        self.thresholds = {}

    def set_threshold(self, category, t):
        self.thresholds[category] = t

    def get_threshold(self, category):
        if category not in self.thresholds:
            return 1.0
        return self.thresholds[category]

    def classify(self, item, default=None):
        probabilities = {}
        max = 0.0
        for category in self.categories():
            probabilities[category] = self.probability(item, category)
            if probabilities[category] > max:
                max = probabilities[category]
                best = category
        for category in probabilities:
            if category == best:
                continue
            if probabilities[category] * self.get_threshold(best) > probabilities[best]:
                return default
        return best

    def document_probability(self, item, category):
        features = self.getfeatures(item)
        p = 1
        for feature in features:
            p *= self.weighted_probability(feature, category, self.feature_probability)
        return p

    def probability(self, item, category):
        category_probability = self.category_count(category) / self.total_count()
        document_probability = self.document_probability(item, category)
        return document_probability * category_probability

class FisherClassifier(Classifier):
    def category_probability(self, feature, category):
        clf = self.feature_probability(feature, category)
        if clf == 0:
            return 0
        frequency_sum = sum(
            [self.feature_probability(feature, category) for category in self.categories()])
        probability = clf / frequency_sum
        return probability

    #TODO