
class StatefulObjectBase:
    stateList = []
    stateMachine = None

    def ChangeState(self, state):
        if self.stateMachine is None:
            return
        self.stateMachine.ChangeState(self.stateList[state])

    def IsCurrentState(self, state):
        if self.stateMachine is None:
            return None
        return self.stateMachine.currentState is self.stateList[state]

    def Update(self):
        if self.stateMachine is not None:
            self.stateMachine.Update()
