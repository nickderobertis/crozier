

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFrequency(enum.StrEnum):
    """
    Repayment frequency
    """

    SMDA = "SMDA"
    SMFL = "SMFL"
    SMFO = "SMFO"
    SMHY = "SMHY"
    SMMO = "SMMO"
    SMOT = "SMOT"
    SMQU = "SMQU"
    SMWE = "SMWE"
    SMYE = "SMYE"

    def visit(
        self,
        smda: typing.Callable[[], T_Result],
        smfl: typing.Callable[[], T_Result],
        smfo: typing.Callable[[], T_Result],
        smhy: typing.Callable[[], T_Result],
        smmo: typing.Callable[[], T_Result],
        smot: typing.Callable[[], T_Result],
        smqu: typing.Callable[[], T_Result],
        smwe: typing.Callable[[], T_Result],
        smye: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFrequency.SMDA:
            return smda()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFrequency.SMFL:
            return smfl()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFrequency.SMFO:
            return smfo()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFrequency.SMHY:
            return smhy()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFrequency.SMMO:
            return smmo()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFrequency.SMOT:
            return smot()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFrequency.SMQU:
            return smqu()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFrequency.SMWE:
            return smwe()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFrequency.SMYE:
            return smye()
