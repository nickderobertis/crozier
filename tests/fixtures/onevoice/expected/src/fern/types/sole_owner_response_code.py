

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SoleOwnerResponseCode(enum.StrEnum):
    SOLE_OWNER_OF_BUSINESSES = "sole_owner_of_businesses"

    def visit(self, sole_owner_of_businesses: typing.Callable[[], T_Result]) -> T_Result:
        if self is SoleOwnerResponseCode.SOLE_OWNER_OF_BUSINESSES:
            return sole_owner_of_businesses()
