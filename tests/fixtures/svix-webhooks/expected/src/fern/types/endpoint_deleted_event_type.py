

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EndpointDeletedEventType(enum.StrEnum):
    ENDPOINT_DELETED = "endpoint.deleted"

    def visit(self, endpoint_deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is EndpointDeletedEventType.ENDPOINT_DELETED:
            return endpoint_deleted()
