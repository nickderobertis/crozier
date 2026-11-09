

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AchClass(enum.StrEnum):
    """
    Specifies the use case of the transfer. Required for transfers on an ACH network.

    `"ccd"` - Corporate Credit or Debit - fund transfer between two corporate bank accounts

    `"ppd"` - Prearranged Payment or Deposit - the transfer is part of a pre-existing relationship with a consumer, eg. bill payment

    `"tel"` - Telephone-Initiated Entry

    `"web"` - Internet-Initiated Entry - debits from a consumer’s account where their authorization is obtained over the Internet
    """

    CCD = "ccd"
    PPD = "ppd"
    TEL = "tel"
    WEB = "web"

    def visit(
        self,
        ccd: typing.Callable[[], T_Result],
        ppd: typing.Callable[[], T_Result],
        tel: typing.Callable[[], T_Result],
        web: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AchClass.CCD:
            return ccd()
        if self is AchClass.PPD:
            return ppd()
        if self is AchClass.TEL:
            return tel()
        if self is AchClass.WEB:
            return web()
