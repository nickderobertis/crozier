

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeRateType(str, enum.Enum):
    """
    Rate type for Fee/Charge (where it is charged in terms of a rate rather than an amount)
    """

    GROSS = "Gross"
    OTHER = "Other"

    def visit(self, gross: typing.Callable[[], T_Result], other: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeRateType.GROSS:
            return gross()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeRateType.OTHER:
            return other()
