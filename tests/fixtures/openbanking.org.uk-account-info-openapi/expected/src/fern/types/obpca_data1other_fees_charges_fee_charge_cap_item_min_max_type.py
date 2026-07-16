

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObpcaData1OtherFeesChargesFeeChargeCapItemMinMaxType(enum.StrEnum):
    """
    Indicates that this is the minimum/ maximum fee/charge that can be applied by the financial institution
    """

    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"

    def visit(self, minimum: typing.Callable[[], T_Result], maximum: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObpcaData1OtherFeesChargesFeeChargeCapItemMinMaxType.MINIMUM:
            return minimum()
        if self is ObpcaData1OtherFeesChargesFeeChargeCapItemMinMaxType.MAXIMUM:
            return maximum()
