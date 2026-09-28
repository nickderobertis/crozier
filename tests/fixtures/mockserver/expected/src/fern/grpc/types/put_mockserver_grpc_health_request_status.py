

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverGrpcHealthRequestStatus(enum.StrEnum):
    UNKNOWN = "UNKNOWN"
    SERVING = "SERVING"
    NOT_SERVING = "NOT_SERVING"
    SERVICE_UNKNOWN = "SERVICE_UNKNOWN"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        serving: typing.Callable[[], T_Result],
        not_serving: typing.Callable[[], T_Result],
        service_unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PutMockserverGrpcHealthRequestStatus.UNKNOWN:
            return unknown()
        if self is PutMockserverGrpcHealthRequestStatus.SERVING:
            return serving()
        if self is PutMockserverGrpcHealthRequestStatus.NOT_SERVING:
            return not_serving()
        if self is PutMockserverGrpcHealthRequestStatus.SERVICE_UNKNOWN:
            return service_unknown()
