

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TriggerSpecState(enum.StrEnum):
    """
    State of the trigger
    """

    ACTIVE = "active"
    DEPRECATED = "deprecated"
    EOL = "eol"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
        eol: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TriggerSpecState.ACTIVE:
            return active()
        if self is TriggerSpecState.DEPRECATED:
            return deprecated()
        if self is TriggerSpecState.EOL:
            return eol()
