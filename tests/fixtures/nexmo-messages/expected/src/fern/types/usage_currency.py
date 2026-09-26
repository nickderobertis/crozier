

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UsageCurrency(enum.StrEnum):
    """
    The charge currency in ISO 4217 format.
    """

    EUR = "EUR"

    def visit(self, eur: typing.Callable[[], T_Result]) -> T_Result:
        if self is UsageCurrency.EUR:
            return eur()
