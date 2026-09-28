

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverBreakpointMatcherRequestPhasesItem(enum.StrEnum):
    REQUEST = "REQUEST"
    RESPONSE = "RESPONSE"
    RESPONSE_STREAM = "RESPONSE_STREAM"
    INBOUND_STREAM = "INBOUND_STREAM"

    def visit(
        self,
        request: typing.Callable[[], T_Result],
        response: typing.Callable[[], T_Result],
        response_stream: typing.Callable[[], T_Result],
        inbound_stream: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PutMockserverBreakpointMatcherRequestPhasesItem.REQUEST:
            return request()
        if self is PutMockserverBreakpointMatcherRequestPhasesItem.RESPONSE:
            return response()
        if self is PutMockserverBreakpointMatcherRequestPhasesItem.RESPONSE_STREAM:
            return response_stream()
        if self is PutMockserverBreakpointMatcherRequestPhasesItem.INBOUND_STREAM:
            return inbound_stream()
