

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseInProgressStreamingEventResponseObject(enum.StrEnum):
    """
    The object type, which was always `response`.
    """

    RESPONSE = "response"

    def visit(self, response: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseInProgressStreamingEventResponseObject.RESPONSE:
            return response()
