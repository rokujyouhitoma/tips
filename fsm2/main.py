from State import State
from StatefulObjectBase import StatefulObjectBase
from StateMachine import StateMachine

EnemyState = {
    'Wander' : 0,
    'Pursuit': 1,
    'Attack' : 2,
    'Explode': 3
}

class GameObject:
    def Update(self):
        pass

class Enemy(StatefulObjectBase, GameObject):
    def __init__(self):
        self.stateList.append(StateWander(self))
        self.stateList.append(StatePursuit(self))
        self.stateMachine = StateMachine()
        self.ChangeState(EnemyState.get('Wander'))

class StateWander(State):
    pass

class StatePursuit(State):
    pass

class StateAttack(State):
    pass

class StateExplode(State):
    pass

enemy = Enemy()
print(enemy.stateMachine.currentState)
print(enemy.IsCurrentState(EnemyState.get('Wander')))
