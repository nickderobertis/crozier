

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EndpointCreatedEventType(enum.StrEnum):
    ENDPOINT_CREATED = "endpoint.created"

    def visit(self, endpoint_created: typing.Callable[[], T_Result]) -> T_Result:
        if self is EndpointCreatedEventType.ENDPOINT_CREATED:
            return endpoint_created()
