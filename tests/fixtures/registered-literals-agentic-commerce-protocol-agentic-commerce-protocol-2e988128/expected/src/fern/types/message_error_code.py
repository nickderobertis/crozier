

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageErrorCode(enum.StrEnum):
    MISSING = "missing"
    INVALID = "invalid"
    OUT_OF_STOCK = "out_of_stock"
    PAYMENT_DECLINED = "payment_declined"
    REQUIRES_SIGN_IN = "requires_sign_in"
    REQUIRES3DS = "requires_3ds"

    def visit(
        self,
        missing: typing.Callable[[], T_Result],
        invalid: typing.Callable[[], T_Result],
        out_of_stock: typing.Callable[[], T_Result],
        payment_declined: typing.Callable[[], T_Result],
        requires_sign_in: typing.Callable[[], T_Result],
        requires3ds: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageErrorCode.MISSING:
            return missing()
        if self is MessageErrorCode.INVALID:
            return invalid()
        if self is MessageErrorCode.OUT_OF_STOCK:
            return out_of_stock()
        if self is MessageErrorCode.PAYMENT_DECLINED:
            return payment_declined()
        if self is MessageErrorCode.REQUIRES_SIGN_IN:
            return requires_sign_in()
        if self is MessageErrorCode.REQUIRES3DS:
            return requires3ds()
