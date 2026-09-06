

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EndpointDisabledEventType(enum.StrEnum):
    ENDPOINT_DISABLED = "endpoint.disabled"

    def visit(self, endpoint_disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is EndpointDisabledEventType.ENDPOINT_DISABLED:
            return endpoint_disabled()
