

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftType(str, enum.Enum):
    """
    An overdraft can either be 'committed' which means that the facility cannot be withdrawn without reasonable notification before it's agreed end date, or 'on demand' which means that the financial institution can demand repayment at any point in time.
    """

    OVCO = "OVCO"
    OVOD = "OVOD"
    OVOT = "OVOT"

    def visit(
        self,
        ovco: typing.Callable[[], T_Result],
        ovod: typing.Callable[[], T_Result],
        ovot: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftType.OVCO:
            return ovco()
        if self is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftType.OVOD:
            return ovod()
        if self is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftType.OVOT:
            return ovot()
