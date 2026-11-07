

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class OtherSlurpRequestPartsItem(enum.StrEnum):
    EXT = "ext"
    INT = "int"
    TOKEN = "token"
    NFTS = "nfts"
    ONE_THOUSAND_ONE_HUNDRED_FIFTY_FIVE = "1155"
    MINER = "miner"
    UNCLES = "uncles"
    WITHDRAWALS = "withdrawals"
    SOME = "some"
    ALL = "all"

    def visit(
        self,
        ext: typing.Callable[[], T_Result],
        int_: typing.Callable[[], T_Result],
        token: typing.Callable[[], T_Result],
        nfts: typing.Callable[[], T_Result],
        one_thousand_one_hundred_fifty_five: typing.Callable[[], T_Result],
        miner: typing.Callable[[], T_Result],
        uncles: typing.Callable[[], T_Result],
        withdrawals: typing.Callable[[], T_Result],
        some: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OtherSlurpRequestPartsItem.EXT:
            return ext()
        if self is OtherSlurpRequestPartsItem.INT:
            return int_()
        if self is OtherSlurpRequestPartsItem.TOKEN:
            return token()
        if self is OtherSlurpRequestPartsItem.NFTS:
            return nfts()
        if self is OtherSlurpRequestPartsItem.ONE_THOUSAND_ONE_HUNDRED_FIFTY_FIVE:
            return one_thousand_one_hundred_fifty_five()
        if self is OtherSlurpRequestPartsItem.MINER:
            return miner()
        if self is OtherSlurpRequestPartsItem.UNCLES:
            return uncles()
        if self is OtherSlurpRequestPartsItem.WITHDRAWALS:
            return withdrawals()
        if self is OtherSlurpRequestPartsItem.SOME:
            return some()
        if self is OtherSlurpRequestPartsItem.ALL:
            return all_()
