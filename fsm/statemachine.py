from string import upper

class InitializationError(Exception):
    def __init__(self, *args, **kwds):
        super(Exception, self).__init__(*args, **kwds)

class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=False):
        name = upper(name)
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = upper(name)

    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError('must call .set_start() before .run()')
        if not self.endStates:
            raise InitializationError('at least one state must be an end_state')
        while True:
            (newState, cargo) = handler(cargo)
            if upper(newState) in self.endStates:
                break
            else:
                handler = self.handlers[upper(newState)]

