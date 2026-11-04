

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseCreatedStreamingEventResponseObject(enum.StrEnum):
    """
    The object type, which was always `response`.
    """

    RESPONSE = "response"

    def visit(self, response: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseCreatedStreamingEventResponseObject.RESPONSE:
            return response()
