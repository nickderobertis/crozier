

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChainstateStateRequestPartsItem(enum.StrEnum):
    BALANCE = "balance"
    NONCE = "nonce"
    CODE = "code"
    PROXY = "proxy"
    DEPLOYED = "deployed"
    ACCTTYPE = "accttype"
    SOME = "some"
    ALL = "all"

    def visit(
        self,
        balance: typing.Callable[[], T_Result],
        nonce: typing.Callable[[], T_Result],
        code: typing.Callable[[], T_Result],
        proxy: typing.Callable[[], T_Result],
        deployed: typing.Callable[[], T_Result],
        accttype: typing.Callable[[], T_Result],
        some: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChainstateStateRequestPartsItem.BALANCE:
            return balance()
        if self is ChainstateStateRequestPartsItem.NONCE:
            return nonce()
        if self is ChainstateStateRequestPartsItem.CODE:
            return code()
        if self is ChainstateStateRequestPartsItem.PROXY:
            return proxy()
        if self is ChainstateStateRequestPartsItem.DEPLOYED:
            return deployed()
        if self is ChainstateStateRequestPartsItem.ACCTTYPE:
            return accttype()
        if self is ChainstateStateRequestPartsItem.SOME:
            return some()
        if self is ChainstateStateRequestPartsItem.ALL:
            return all_()
