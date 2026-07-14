

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TriggerParamSpecState(str, enum.Enum):
    """
    State of the trigger parameter
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
        if self is TriggerParamSpecState.ACTIVE:
            return active()
        if self is TriggerParamSpecState.DEPRECATED:
            return deprecated()
        if self is TriggerParamSpecState.EOL:
            return eol()
