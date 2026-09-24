

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaxCloudAddressCountryCode(enum.StrEnum):
    """
    ISO 3166-1 alpha-2 country code of the address. US (United States) or CA (Canada). Defaults to US when omitted.
    """

    US = "US"
    CA = "CA"

    def visit(self, us: typing.Callable[[], T_Result], ca: typing.Callable[[], T_Result]) -> T_Result:
        if self is TaxCloudAddressCountryCode.US:
            return us()
        if self is TaxCloudAddressCountryCode.CA:
            return ca()
