

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EndpointUpdatedEventType(enum.StrEnum):
    ENDPOINT_UPDATED = "endpoint.updated"

    def visit(self, endpoint_updated: typing.Callable[[], T_Result]) -> T_Result:
        if self is EndpointUpdatedEventType.ENDPOINT_UPDATED:
            return endpoint_updated()
