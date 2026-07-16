

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ChangeSetHooksStatus(str, enum.Enum):
    PLANNING = "PLANNING"
    PLANNED = "PLANNED"
    UNAVAILABLE = "UNAVAILABLE"

    def visit(
        self,
        planning: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChangeSetHooksStatus.PLANNING:
            return planning()
        if self is ChangeSetHooksStatus.PLANNED:
            return planned()
        if self is ChangeSetHooksStatus.UNAVAILABLE:
            return unavailable()
