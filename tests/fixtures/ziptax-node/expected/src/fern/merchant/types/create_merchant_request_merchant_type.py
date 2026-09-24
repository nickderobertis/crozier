

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateMerchantRequestMerchantType(enum.StrEnum):
    """
    The merchant's compliance model, chosen once at creation. 'taxcloud' (the default) starts the TaxCloud invite process, so TaxCloud can handle registration, filing, and remittance for the merchant. 'self-managed' skips the invite entirely and the merchant is active as soon as the call returns, with the merchant remaining responsible for their own compliance. 'connected' and 'offline' are deprecated aliases for 'taxcloud' and 'self-managed' respectively; they are still accepted but should not be used in new integrations.
    """

    TAXCLOUD = "taxcloud"
    SELF_MANAGED = "self-managed"
    CONNECTED = "connected"
    OFFLINE = "offline"

    def visit(
        self,
        taxcloud: typing.Callable[[], T_Result],
        self_managed: typing.Callable[[], T_Result],
        connected: typing.Callable[[], T_Result],
        offline: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateMerchantRequestMerchantType.TAXCLOUD:
            return taxcloud()
        if self is CreateMerchantRequestMerchantType.SELF_MANAGED:
            return self_managed()
        if self is CreateMerchantRequestMerchantType.CONNECTED:
            return connected()
        if self is CreateMerchantRequestMerchantType.OFFLINE:
            return offline()
