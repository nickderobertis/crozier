

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ActivityShowAs(str, enum.Enum):
    FREE = "free"
    BUSY = "busy"

    def visit(self, free: typing.Callable[[], T_Result], busy: typing.Callable[[], T_Result]) -> T_Result:
        if self is ActivityShowAs.FREE:
            return free()
        if self is ActivityShowAs.BUSY:
            return busy()
