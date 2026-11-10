

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FdxPartyType(enum.StrEnum):
    """
    Identifies the type of a party
    """

    DATA_ACCESS_PLATFORM = "DATA_ACCESS_PLATFORM"
    DATA_PROVIDER = "DATA_PROVIDER"
    DATA_RECIPIENT = "DATA_RECIPIENT"
    INDIVIDUAL = "INDIVIDUAL"
    MERCHANT = "MERCHANT"
    VENDOR = "VENDOR"

    def visit(
        self,
        data_access_platform: typing.Callable[[], T_Result],
        data_provider: typing.Callable[[], T_Result],
        data_recipient: typing.Callable[[], T_Result],
        individual: typing.Callable[[], T_Result],
        merchant: typing.Callable[[], T_Result],
        vendor: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FdxPartyType.DATA_ACCESS_PLATFORM:
            return data_access_platform()
        if self is FdxPartyType.DATA_PROVIDER:
            return data_provider()
        if self is FdxPartyType.DATA_RECIPIENT:
            return data_recipient()
        if self is FdxPartyType.INDIVIDUAL:
            return individual()
        if self is FdxPartyType.MERCHANT:
            return merchant()
        if self is FdxPartyType.VENDOR:
            return vendor()
