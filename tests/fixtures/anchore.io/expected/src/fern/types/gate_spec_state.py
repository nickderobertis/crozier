

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GateSpecState(enum.StrEnum):
    """
    State of the gate and transitively all triggers it contains if not 'active'
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
        if self is GateSpecState.ACTIVE:
            return active()
        if self is GateSpecState.DEPRECATED:
            return deprecated()
        if self is GateSpecState.EOL:
            return eol()
