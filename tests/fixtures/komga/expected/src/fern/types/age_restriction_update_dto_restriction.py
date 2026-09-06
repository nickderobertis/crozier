

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgeRestrictionUpdateDtoRestriction(enum.StrEnum):
    ALLOW_ONLY = "ALLOW_ONLY"
    EXCLUDE = "EXCLUDE"
    NONE = "NONE"

    def visit(
        self,
        allow_only: typing.Callable[[], T_Result],
        exclude: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgeRestrictionUpdateDtoRestriction.ALLOW_ONLY:
            return allow_only()
        if self is AgeRestrictionUpdateDtoRestriction.EXCLUDE:
            return exclude()
        if self is AgeRestrictionUpdateDtoRestriction.NONE:
            return none()
