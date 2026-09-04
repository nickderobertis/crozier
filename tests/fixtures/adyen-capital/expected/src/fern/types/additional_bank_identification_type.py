

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdditionalBankIdentificationType(enum.StrEnum):
    """
    The type of additional bank identification, depending on the country.

    Possible values:

     * **auBsbCode**: The 6-digit [Australian Bank State Branch (BSB) code](https://en.wikipedia.org/wiki/Bank_state_branch), without separators or spaces.
     * **caRoutingNumber**: The 9-digit [Canadian routing number](https://en.wikipedia.org/wiki/Routing_number_(Canada)), in EFT format, without separators or spaces.
     * **gbSortCode**: The 6-digit [UK sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or spaces
     * **usRoutingNumber**: The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or spaces.
    """

    AU_BSB_CODE = "auBsbCode"
    CA_ROUTING_NUMBER = "caRoutingNumber"
    GB_SORT_CODE = "gbSortCode"
    US_ROUTING_NUMBER = "usRoutingNumber"

    def visit(
        self,
        au_bsb_code: typing.Callable[[], T_Result],
        ca_routing_number: typing.Callable[[], T_Result],
        gb_sort_code: typing.Callable[[], T_Result],
        us_routing_number: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdditionalBankIdentificationType.AU_BSB_CODE:
            return au_bsb_code()
        if self is AdditionalBankIdentificationType.CA_ROUTING_NUMBER:
            return ca_routing_number()
        if self is AdditionalBankIdentificationType.GB_SORT_CODE:
            return gb_sort_code()
        if self is AdditionalBankIdentificationType.US_ROUTING_NUMBER:
            return us_routing_number()
