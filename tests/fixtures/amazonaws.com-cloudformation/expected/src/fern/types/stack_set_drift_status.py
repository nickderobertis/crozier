

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class StackSetDriftStatus(str, enum.Enum):
    DRIFTED = "DRIFTED"
    IN_SYNC = "IN_SYNC"
    NOT_CHECKED = "NOT_CHECKED"

    def visit(
        self,
        drifted: typing.Callable[[], T_Result],
        in_sync: typing.Callable[[], T_Result],
        not_checked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StackSetDriftStatus.DRIFTED:
            return drifted()
        if self is StackSetDriftStatus.IN_SYNC:
            return in_sync()
        if self is StackSetDriftStatus.NOT_CHECKED:
            return not_checked()
