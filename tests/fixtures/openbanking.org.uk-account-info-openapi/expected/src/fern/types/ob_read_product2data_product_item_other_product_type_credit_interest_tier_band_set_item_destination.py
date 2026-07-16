

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemDestination(enum.StrEnum):
    """
    Describes whether accrued interest is payable only to the BCA or to another bank account
    """

    INOT = "INOT"
    INPA = "INPA"
    INSC = "INSC"

    def visit(
        self,
        inot: typing.Callable[[], T_Result],
        inpa: typing.Callable[[], T_Result],
        insc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemDestination.INOT:
            return inot()
        if self is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemDestination.INPA:
            return inpa()
        if self is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemDestination.INSC:
            return insc()
