

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgeRestrictionDtoRestriction(enum.StrEnum):
    ALLOW_ONLY = "ALLOW_ONLY"
    EXCLUDE = "EXCLUDE"

    def visit(self, allow_only: typing.Callable[[], T_Result], exclude: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgeRestrictionDtoRestriction.ALLOW_ONLY:
            return allow_only()
        if self is AgeRestrictionDtoRestriction.EXCLUDE:
            return exclude()
