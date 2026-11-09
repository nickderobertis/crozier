

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IssuingCountry(enum.StrEnum):
    """
    A binary match indicator specifying whether the country that issued the provided document matches the country that the user separately provided to Plaid.

    Note: You can configure whether a `no_match` on `issuing_country` fails the `documentary_verification` by editing your Plaid Template.
    """

    MATCH = "match"
    NO_MATCH = "no_match"

    def visit(self, match: typing.Callable[[], T_Result], no_match: typing.Callable[[], T_Result]) -> T_Result:
        if self is IssuingCountry.MATCH:
            return match()
        if self is IssuingCountry.NO_MATCH:
            return no_match()
