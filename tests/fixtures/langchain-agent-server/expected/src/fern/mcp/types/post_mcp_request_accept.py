

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostMcpRequestAccept(enum.StrEnum):
    APPLICATION_JSON_TEXT_EVENT_STREAM = "application/json, text/event-stream"

    def visit(self, application_json_text_event_stream: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostMcpRequestAccept.APPLICATION_JSON_TEXT_EVENT_STREAM:
            return application_json_text_event_stream()
