class Expression(object):
    def evaluate(self):
        pass

class NumberExpression(Expression):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        return left + right
