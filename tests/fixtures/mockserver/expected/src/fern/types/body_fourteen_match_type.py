

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyFourteenMatchType(enum.StrEnum):
    STRICT = "STRICT"
    ONLY_MATCHING_FIELDS = "ONLY_MATCHING_FIELDS"

    def visit(
        self, strict: typing.Callable[[], T_Result], only_matching_fields: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is BodyFourteenMatchType.STRICT:
            return strict()
        if self is BodyFourteenMatchType.ONLY_MATCHING_FIELDS:
            return only_matching_fields()
