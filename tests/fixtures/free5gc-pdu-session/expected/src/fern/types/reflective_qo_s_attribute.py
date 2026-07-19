

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReflectiveQoSAttribute(enum.StrEnum):
    RQOS = "RQOS"
    NO_RQOS = "NO_RQOS"

    def visit(self, rqos: typing.Callable[[], T_Result], no_rqos: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReflectiveQoSAttribute.RQOS:
            return rqos()
        if self is ReflectiveQoSAttribute.NO_RQOS:
            return no_rqos()
