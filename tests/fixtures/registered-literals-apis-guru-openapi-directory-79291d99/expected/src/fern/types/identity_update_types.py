

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IdentityUpdateTypes(enum.StrEnum):
    """
    The possible types of identity data that may have changed.
    """

    PHONES = "PHONES"
    ADDRESSES = "ADDRESSES"
    EMAILS = "EMAILS"
    NAMES = "NAMES"

    def visit(
        self,
        phones: typing.Callable[[], T_Result],
        addresses: typing.Callable[[], T_Result],
        emails: typing.Callable[[], T_Result],
        names: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IdentityUpdateTypes.PHONES:
            return phones()
        if self is IdentityUpdateTypes.ADDRESSES:
            return addresses()
        if self is IdentityUpdateTypes.EMAILS:
            return emails()
        if self is IdentityUpdateTypes.NAMES:
            return names()
