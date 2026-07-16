

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeRepaymentAmountType(str, enum.Enum):
    """
    The repayment is for paying just the interest only or both interest and capital or bullet amount or balance to date etc
    """

    RABD = "RABD"
    RABL = "RABL"
    RACI = "RACI"
    RAFC = "RAFC"
    RAIO = "RAIO"
    RALT = "RALT"
    USOT = "USOT"

    def visit(
        self,
        rabd: typing.Callable[[], T_Result],
        rabl: typing.Callable[[], T_Result],
        raci: typing.Callable[[], T_Result],
        rafc: typing.Callable[[], T_Result],
        raio: typing.Callable[[], T_Result],
        ralt: typing.Callable[[], T_Result],
        usot: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentAmountType.RABD:
            return rabd()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentAmountType.RABL:
            return rabl()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentAmountType.RACI:
            return raci()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentAmountType.RAFC:
            return rafc()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentAmountType.RAIO:
            return raio()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentAmountType.RALT:
            return ralt()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentAmountType.USOT:
            return usot()
