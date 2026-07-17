

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType(enum.StrEnum):
    """
    Repayment type
    """

    USBA = "USBA"
    USBU = "USBU"
    USCI = "USCI"
    USCS = "USCS"
    USER = "USER"
    USFA = "USFA"
    USFB = "USFB"
    USFI = "USFI"
    USIO = "USIO"
    USOT = "USOT"
    USPF = "USPF"
    USRW = "USRW"
    USSL = "USSL"

    def visit(
        self,
        usba: typing.Callable[[], T_Result],
        usbu: typing.Callable[[], T_Result],
        usci: typing.Callable[[], T_Result],
        uscs: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
        usfa: typing.Callable[[], T_Result],
        usfb: typing.Callable[[], T_Result],
        usfi: typing.Callable[[], T_Result],
        usio: typing.Callable[[], T_Result],
        usot: typing.Callable[[], T_Result],
        uspf: typing.Callable[[], T_Result],
        usrw: typing.Callable[[], T_Result],
        ussl: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType.USBA:
            return usba()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType.USBU:
            return usbu()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType.USCI:
            return usci()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType.USCS:
            return uscs()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType.USER:
            return user()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType.USFA:
            return usfa()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType.USFB:
            return usfb()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType.USFI:
            return usfi()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType.USIO:
            return usio()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType.USOT:
            return usot()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType.USPF:
            return uspf()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType.USRW:
            return usrw()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType.USSL:
            return ussl()
