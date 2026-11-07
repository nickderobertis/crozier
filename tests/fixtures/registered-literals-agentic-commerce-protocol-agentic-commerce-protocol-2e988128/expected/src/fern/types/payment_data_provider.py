

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentDataProvider(enum.StrEnum):
    STRIPE = "stripe"

    def visit(self, stripe: typing.Callable[[], T_Result]) -> T_Result:
        if self is PaymentDataProvider.STRIPE:
            return stripe()
