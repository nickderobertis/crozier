

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationProviderProvider(enum.StrEnum):
    STRIPE = "stripe"
    ADYEN = "adyen"

    def visit(self, stripe: typing.Callable[[], T_Result], adyen: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthenticationProviderProvider.STRIPE:
            return stripe()
        if self is AuthenticationProviderProvider.ADYEN:
            return adyen()
