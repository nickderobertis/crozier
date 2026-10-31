

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractionReviewEventThreeType(enum.StrEnum):
    COMPLETION_RETRACTED = "completion_retracted"

    def visit(self, completion_retracted: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExtractionReviewEventThreeType.COMPLETION_RETRACTED:
            return completion_retracted()
