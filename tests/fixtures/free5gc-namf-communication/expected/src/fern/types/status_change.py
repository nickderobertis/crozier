

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StatusChange(enum.StrEnum):
    AMF_UNAVAILABLE = "AMF_UNAVAILABLE"
    AMF_AVAILABLE = "AMF_AVAILABLE"

    def visit(
        self, amf_unavailable: typing.Callable[[], T_Result], amf_available: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is StatusChange.AMF_UNAVAILABLE:
            return amf_unavailable()
        if self is StatusChange.AMF_AVAILABLE:
            return amf_available()
