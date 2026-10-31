

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractionReviewEventPreviousValueType(enum.StrEnum):
    FIELD_CONFIRMED = "field_confirmed"

    def visit(self, field_confirmed: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExtractionReviewEventPreviousValueType.FIELD_CONFIRMED:
            return field_confirmed()
