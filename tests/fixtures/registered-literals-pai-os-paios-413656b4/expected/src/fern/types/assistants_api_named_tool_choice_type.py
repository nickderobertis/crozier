

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssistantsApiNamedToolChoiceType(enum.StrEnum):
    """
    The type of the tool. If type is `function`, the function name must be set
    """

    FUNCTION = "function"
    CODE_INTERPRETER = "code_interpreter"
    RETRIEVAL = "retrieval"

    def visit(
        self,
        function: typing.Callable[[], T_Result],
        code_interpreter: typing.Callable[[], T_Result],
        retrieval: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssistantsApiNamedToolChoiceType.FUNCTION:
            return function()
        if self is AssistantsApiNamedToolChoiceType.CODE_INTERPRETER:
            return code_interpreter()
        if self is AssistantsApiNamedToolChoiceType.RETRIEVAL:
            return retrieval()
