

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractionReviewEventOneType(enum.StrEnum):
    FIELD_CONFIRMATION_RETRACTED = "field_confirmation_retracted"

    def visit(self, field_confirmation_retracted: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExtractionReviewEventOneType.FIELD_CONFIRMATION_RETRACTED:
            return field_confirmation_retracted()
