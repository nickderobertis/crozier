

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverRetrieveRequestType(enum.StrEnum):
    LOGS = "logs"
    REQUESTS = "requests"
    REQUEST_RESPONSES = "request_responses"
    RECORDED_EXPECTATIONS = "recorded_expectations"
    ACTIVE_EXPECTATIONS = "active_expectations"
    METRICS = "metrics"

    def visit(
        self,
        logs: typing.Callable[[], T_Result],
        requests: typing.Callable[[], T_Result],
        request_responses: typing.Callable[[], T_Result],
        recorded_expectations: typing.Callable[[], T_Result],
        active_expectations: typing.Callable[[], T_Result],
        metrics: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PutMockserverRetrieveRequestType.LOGS:
            return logs()
        if self is PutMockserverRetrieveRequestType.REQUESTS:
            return requests()
        if self is PutMockserverRetrieveRequestType.REQUEST_RESPONSES:
            return request_responses()
        if self is PutMockserverRetrieveRequestType.RECORDED_EXPECTATIONS:
            return recorded_expectations()
        if self is PutMockserverRetrieveRequestType.ACTIVE_EXPECTATIONS:
            return active_expectations()
        if self is PutMockserverRetrieveRequestType.METRICS:
            return metrics()
