

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptLogId(enum.StrEnum):
    """
    A literal 'p' which identifies the object as a project prompt
    """

    P = "p"

    def visit(self, p: typing.Callable[[], T_Result]) -> T_Result:
        if self is PromptLogId.P:
            return p()
