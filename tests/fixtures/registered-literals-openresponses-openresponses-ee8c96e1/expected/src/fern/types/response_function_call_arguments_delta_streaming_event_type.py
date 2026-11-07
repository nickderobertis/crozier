

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseFunctionCallArgumentsDeltaStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.function_call_arguments.delta`.
    """

    RESPONSE_FUNCTION_CALL_ARGUMENTS_DELTA = "response.function_call_arguments.delta"

    def visit(self, response_function_call_arguments_delta: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseFunctionCallArgumentsDeltaStreamingEventType.RESPONSE_FUNCTION_CALL_ARGUMENTS_DELTA:
            return response_function_call_arguments_delta()
