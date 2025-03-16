from enum import Enum

class State:
    """
    状態を定義するクラス。

    - name: 状態の名前 (Enum)。
    - parent: 親の状態 (State or None)。
    """
    def __init__(self, name: Enum, parent: 'State' = None):
        self.name = name
        self.parent = parent

class Trigger:
    """
    トリガーを定義するクラス。

    - name: トリガーの名前 (Enum)。
    """
    def __init__(self, name: Enum):
        self.name = name

class Source:
    """
    遷移元を定義するクラス。

    - state: 遷移元の状態 (State or list[State] or str)。
    """
    def __init__(self, state):
        self.state = state

class Destination:
    """
    遷移先を定義するクラス。

    - state: 遷移先の状態 (State)。
    """
    def __init__(self, state: State):
        self.state = state

class Effect:
    """
    効果を定義するクラス。

    - function: 実行する関数 (callable)。
    """
    def __init__(self, function):
        self.function = function

class Transition:
    """
    状態遷移を定義するクラス。

    - trigger: 状態遷移を発生させるトリガー (Trigger)。
    - source: 遷移元の状態 (Source)。
    - destination: 遷移先の状態 (Destination)。
    - effect: 状態遷移時に実行される効果 (Effect)。
    """
    def __init__(self, trigger: Trigger, source: Source, destination: Destination, effect: Effect = None):
        self.trigger = trigger
        self.source = source
        self.destination = destination
        self.effect = effect

class HFSM:
    """
    階層型有限状態機械 (HFSM) クラス。

    状態遷移は、トリガー、遷移元の状態 (source)、遷移先の状態 (destination)、および効果 (effect) によって定義されます。

    - trigger: 状態遷移を発生させるイベント。
    - source: 遷移元の状態。'*' は任意の状態を意味します。
    - destination: 遷移先の状態。
    - effect: 状態遷移時に実行される関数。
    """
    def __init__(self, initial_state, states, transitions):
        """
        HFSMの初期化。

        Args:
            initial_state (State): 初期状態。
            states (list[State]): 状態のリスト。
            transitions (list[Transition]): 遷移のリスト。
        """
        self.state = initial_state
        self.states = states
        self.transitions = transitions

    def trigger(self, event):
        """
        イベントに基づいて状態遷移を発生させる。

        Args:
            event (str): 発生させるイベント。
        """
        for transition in self.transitions:
            if transition.trigger.name.value == event and self.match_source(transition.source.state):
                self.state = transition.destination.state
                if transition.effect:
                    transition.effect.function()
                return

    def match_source(self, source):
        """
        遷移元の状態が現在の状態と一致するかどうかを判定する。

        Args:
            source (State or list[State]): 遷移元の状態。'*' は任意の状態を意味します。

        Returns:
            bool: 遷移元の状態が現在の状態と一致する場合はTrue、そうでない場合はFalse。
        """
        if source == '*':
            return True
        if isinstance(source, State):
            return self.state == source or self.state.parent == source
        if isinstance(source, list):
            return self.state in source or (self.state.parent in source if self.state.parent else False)
        return False
