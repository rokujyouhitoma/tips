from typing import Any


class Value:
    def body(self) -> Any:
        pass


class Condition:
    def is_match(self, value: Value) -> bool:
        pass
