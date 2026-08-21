

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventType(enum.StrEnum):
    VIEWER_REQUEST = "viewer-request"
    VIEWER_RESPONSE = "viewer-response"
    ORIGIN_REQUEST = "origin-request"
    ORIGIN_RESPONSE = "origin-response"

    def visit(
        self,
        viewer_request: typing.Callable[[], T_Result],
        viewer_response: typing.Callable[[], T_Result],
        origin_request: typing.Callable[[], T_Result],
        origin_response: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EventType.VIEWER_REQUEST:
            return viewer_request()
        if self is EventType.VIEWER_RESPONSE:
            return viewer_response()
        if self is EventType.ORIGIN_REQUEST:
            return origin_request()
        if self is EventType.ORIGIN_RESPONSE:
            return origin_response()
