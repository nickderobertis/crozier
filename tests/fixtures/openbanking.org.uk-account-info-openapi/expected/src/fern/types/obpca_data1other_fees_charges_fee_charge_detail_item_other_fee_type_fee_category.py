

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherFeeTypeFeeCategory(str, enum.Enum):
    """
    Categorisation of fees and charges into standard categories.
    """

    OTHER = "Other"
    SERVICING = "Servicing"

    def visit(self, other: typing.Callable[[], T_Result], servicing: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherFeeTypeFeeCategory.OTHER:
            return other()
        if self is ObpcaData1OtherFeesChargesFeeChargeDetailItemOtherFeeTypeFeeCategory.SERVICING:
            return servicing()
