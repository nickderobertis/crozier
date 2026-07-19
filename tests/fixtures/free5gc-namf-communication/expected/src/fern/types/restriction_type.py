

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RestrictionType(enum.StrEnum):
    ALLOWED_AREAS = "ALLOWED_AREAS"
    NOT_ALLOWED_AREAS = "NOT_ALLOWED_AREAS"

    def visit(
        self, allowed_areas: typing.Callable[[], T_Result], not_allowed_areas: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is RestrictionType.ALLOWED_AREAS:
            return allowed_areas()
        if self is RestrictionType.NOT_ALLOWED_AREAS:
            return not_allowed_areas()
