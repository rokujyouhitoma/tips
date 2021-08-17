class State(object):
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def entry(self):
        print('%s entry' % (self.name))

    def execute(self):
        print('%s execute' % (self.name))

    def exit(self):
        print('%s exit' % (self.name))

    def __str__(self):
        return '<State %s>' % self.name


class StateMachine(object):
    def __init__(self):
        self.startState = None
        self.currentState = None
        self.transactions = {}

    def add_transition(self, current_state, event_name, next_state, action):
        # TODO
        if event_name in self.transactions:
            self.transactions[event_name].append(next_state)
        else:
            self.transactions[event_name] = [next_state]

    def set_start(self, state):
        self.startState = state

    def run(self):
        while True:
            break

class HFSM(StateMachine):
    def __init__(self):
        super(HFSM, self).__init__()


if __name__ == '__main__':
    start   = State('start', None)
    state_4 = State('state_4', None)
    state_0 = State('state_0', state_4)
    state_1 = State('state_1', state_4)
    state_2 = State('state_2', state_1)
    state_3 = State('state_3', state_2)
    end     = State('end', None)

    action_0 = lambda: 1

    m = HFSM()

    m.add_transition(start, None, state_0, None)
    m.add_transition(state_0, 'event_0', state_3, action_0)
    m.add_transition(state_1, 'event_1', state_0, None)
    m.add_transition(state_0, 'event_1', end, None)
    m.add_transition(end, None, None, None)

    m.set_start(start)
