from hfsm import *
from enum import Enum

class StateName(Enum):
    IDLE = "idle"
    MOVE = "move"
    WALK = "walk"
    RUN = "run"

class TriggerName(Enum):
    MOVE = "move"
    STOP = "stop"
    IDLE = "idle"
    WALK = "walk"
    RUN = "run"

class Robot:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name}: 移動開始")

    def walk(self):
        print(f"{self.name}: 歩行開始")

    def run(self):
        print(f"{self.name}: 走行開始")

    def stop(self):
        print(f"{self.name}: 停止")

    def idle(self):
        print(f"{self.name}: アイドル状態")

if __name__ == "__main__":
    """
    状態遷移表:
    状態遷移の木構造
    idle
    └── move
        ├── walk
        └── run

    idle 階層
    | 現在の状態 | トリガー | 遷移先の状態 | 効果          |
    |-----------|----------|------------|---------------|
    | idle      | move     | move       | robot.move()  |
    | * | idle     | idle       | robot.idle()  |

    move 階層
    | 現在の状態 | トリガー | 遷移先の状態 | 効果          |
    |-----------|----------|------------|---------------|
    | move      | walk     | walk       | robot.walk()  |
    | move      | run      | run        | robot.run()   |

    walk 階層
    | 現在の状態 | トリガー | 遷移先の状態 | 効果          |
    |-----------|----------|------------|---------------|
    | walk      | stop     | idle       | robot.stop()  |

    run 階層
    | 現在の状態 | トリガー | 遷移先の状態 | 効果          |
    |-----------|----------|------------|---------------|
    | run       | stop     | idle       | robot.stop()  |
    """
    robot = Robot("テストロボット")
    states = [State(StateName.IDLE), State(StateName.MOVE), State(StateName.WALK, State(StateName.MOVE)), State(StateName.RUN, State(StateName.MOVE))]
    transitions = [
        Transition(trigger=Trigger(TriggerName.MOVE), source=Source(states[0]), destination=Destination(states[1]), effect=Effect(lambda: robot.move())),
        Transition(trigger=Trigger(TriggerName.WALK), source=Source(states[1]), destination=Destination(states[2]), effect=Effect(lambda: robot.walk())),
        Transition(trigger=Trigger(TriggerName.RUN), source=Source(states[1]), destination=Destination(states[3]), effect=Effect(lambda: robot.run())),
        Transition(trigger=Trigger(TriggerName.STOP), source=Source(states[2]), destination=Destination(states[0]), effect=Effect(lambda: robot.stop())),
        Transition(trigger=Trigger(TriggerName.STOP), source=Source(states[3]), destination=Destination(states[0]), effect=Effect(lambda: robot.stop())),
        Transition(trigger=Trigger(TriggerName.IDLE), source=Source('*'), destination=Destination(states[0]), effect=Effect(lambda: robot.idle())),
    ]
    hfsm = HFSM(initial_state=states[0], states=states, transitions=transitions)

    # テスト
    assert hfsm.state.name == StateName.IDLE
    hfsm.trigger('move')
    assert hfsm.state.name == StateName.MOVE
    hfsm.trigger('walk')
    assert hfsm.state.name == StateName.WALK
    hfsm.trigger('stop')
    assert hfsm.state.name == StateName.IDLE
    hfsm.trigger('move')
    hfsm.trigger('run')
    assert hfsm.state.name == StateName.RUN
    hfsm.trigger('stop')
    assert hfsm.state.name == StateName.IDLE

    print("全てのテストが成功しました。")
