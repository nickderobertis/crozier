

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Error503Message(enum.StrEnum):
    SERVICE_UNAVAILABLE = "Service Unavailable."

    def visit(self, service_unavailable: typing.Callable[[], T_Result]) -> T_Result:
        if self is Error503Message.SERVICE_UNAVAILABLE:
            return service_unavailable()
