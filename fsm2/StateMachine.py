
class StateMachine:
    currentState = None

    def ChangeState(self, state):
        if self.currentState is not None:
            self.currentState.Exit()
        self.currentState = state
        self.currentState.Enter()

    def Update(self):
        if self.currentState is not None:
            self.currentState.Execute()
