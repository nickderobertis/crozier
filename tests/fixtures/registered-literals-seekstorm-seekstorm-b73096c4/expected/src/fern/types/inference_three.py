

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InferenceThree(enum.StrEnum):
    """
    No inference
    """

    NONE = "None"

    def visit(self, none: typing.Callable[[], T_Result]) -> T_Result:
        if self is InferenceThree.NONE:
            return none()
