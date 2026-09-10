

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FourHundredTwentyTwoDetailsItemCountryNotSupportedDescription(enum.StrEnum):
    THIS_MERCHANT_COUNTRY_IS_NOT_CURRENTLY_SUPPORTED = "This merchant country is not currently supported."

    def visit(self, this_merchant_country_is_not_currently_supported: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is FourHundredTwentyTwoDetailsItemCountryNotSupportedDescription.THIS_MERCHANT_COUNTRY_IS_NOT_CURRENTLY_SUPPORTED
        ):
            return this_merchant_country_is_not_currently_supported()
