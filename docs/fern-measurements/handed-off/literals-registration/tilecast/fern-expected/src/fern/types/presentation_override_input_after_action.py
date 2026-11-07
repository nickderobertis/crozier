

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PresentationOverrideInputAfterAction(enum.StrEnum):
    RESUME = "resume"

    def visit(self, resume: typing.Callable[[], T_Result]) -> T_Result:
        if self is PresentationOverrideInputAfterAction.RESUME:
            return resume()
