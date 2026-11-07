

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseFunctionCallArgumentsDoneStreamingEventType(enum.StrEnum):
    """
    The type of the event, always `response.function_call_arguments.done`.
    """

    RESPONSE_FUNCTION_CALL_ARGUMENTS_DONE = "response.function_call_arguments.done"

    def visit(self, response_function_call_arguments_done: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseFunctionCallArgumentsDoneStreamingEventType.RESPONSE_FUNCTION_CALL_ARGUMENTS_DONE:
            return response_function_call_arguments_done()
