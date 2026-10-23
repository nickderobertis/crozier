

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTokensAddressResponseReadingStockPairingsItemStockVerdict(enum.StrEnum):
    CANONICAL = "canonical"
    LOOKALIKE = "lookalike"
    UNCONFIRMED = "unconfirmed"

    def visit(
        self,
        canonical: typing.Callable[[], T_Result],
        lookalike: typing.Callable[[], T_Result],
        unconfirmed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetTokensAddressResponseReadingStockPairingsItemStockVerdict.CANONICAL:
            return canonical()
        if self is GetTokensAddressResponseReadingStockPairingsItemStockVerdict.LOOKALIKE:
            return lookalike()
        if self is GetTokensAddressResponseReadingStockPairingsItemStockVerdict.UNCONFIRMED:
            return unconfirmed()
