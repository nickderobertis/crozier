

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseFailedStreamingEventResponseObject(enum.StrEnum):
    """
    The object type, which was always `response`.
    """

    RESPONSE = "response"

    def visit(self, response: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseFailedStreamingEventResponseObject.RESPONSE:
            return response()
