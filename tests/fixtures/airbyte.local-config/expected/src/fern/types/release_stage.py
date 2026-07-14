

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ReleaseStage(str, enum.Enum):
    ALPHA = "alpha"
    BETA = "beta"
    GENERALLY_AVAILABLE = "generally_available"
    CUSTOM = "custom"

    def visit(
        self,
        alpha: typing.Callable[[], T_Result],
        beta: typing.Callable[[], T_Result],
        generally_available: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReleaseStage.ALPHA:
            return alpha()
        if self is ReleaseStage.BETA:
            return beta()
        if self is ReleaseStage.GENERALLY_AVAILABLE:
            return generally_available()
        if self is ReleaseStage.CUSTOM:
            return custom()
