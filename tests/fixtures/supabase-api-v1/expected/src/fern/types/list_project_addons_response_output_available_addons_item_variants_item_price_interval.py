

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemPriceInterval(enum.StrEnum):
    MONTHLY = "monthly"
    HOURLY = "hourly"

    def visit(self, monthly: typing.Callable[[], T_Result], hourly: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemPriceInterval.MONTHLY:
            return monthly()
        if self is ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemPriceInterval.HOURLY:
            return hourly()
