

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1TenderEntryMethod(enum.StrEnum):
    """ """

    MANUAL = "MANUAL"
    SCANNED = "SCANNED"
    SQUARE_CASH = "SQUARE_CASH"
    SQUARE_WALLET = "SQUARE_WALLET"
    SWIPED = "SWIPED"
    WEB_FORM = "WEB_FORM"
    OTHER = "OTHER"

    def visit(
        self,
        manual: typing.Callable[[], T_Result],
        scanned: typing.Callable[[], T_Result],
        square_cash: typing.Callable[[], T_Result],
        square_wallet: typing.Callable[[], T_Result],
        swiped: typing.Callable[[], T_Result],
        web_form: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1TenderEntryMethod.MANUAL:
            return manual()
        if self is V1TenderEntryMethod.SCANNED:
            return scanned()
        if self is V1TenderEntryMethod.SQUARE_CASH:
            return square_cash()
        if self is V1TenderEntryMethod.SQUARE_WALLET:
            return square_wallet()
        if self is V1TenderEntryMethod.SWIPED:
            return swiped()
        if self is V1TenderEntryMethod.WEB_FORM:
            return web_form()
        if self is V1TenderEntryMethod.OTHER:
            return other()
