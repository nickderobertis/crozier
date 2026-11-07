

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseCreatedStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.created`.
    """

    RESPONSE_CREATED = "response.created"

    def visit(self, response_created: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseCreatedStreamingEventType.RESPONSE_CREATED:
            return response_created()
