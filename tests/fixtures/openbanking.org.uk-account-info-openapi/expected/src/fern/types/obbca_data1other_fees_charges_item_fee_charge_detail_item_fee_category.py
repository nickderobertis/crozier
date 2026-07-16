

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeCategory(enum.StrEnum):
    """
    Categorisation of fees and charges into standard categories.
    """

    OTHER = "Other"
    SERVICING = "Servicing"

    def visit(self, other: typing.Callable[[], T_Result], servicing: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeCategory.OTHER:
            return other()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeCategory.SERVICING:
            return servicing()
