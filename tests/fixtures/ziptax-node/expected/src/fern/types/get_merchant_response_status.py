

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetMerchantResponseStatus(enum.StrEnum):
    """
    Derived TaxCloud lifecycle status: 'taxcloud_invited' (invite sent, not yet accepted), 'taxcloud_connected' (TaxCloud credentials set and active), 'taxcloud_disconnected' (previously connected, now disconnected), or 'external_compliance' (managed outside TaxCloud).
    """

    TAXCLOUD_INVITED = "taxcloud_invited"
    TAXCLOUD_CONNECTED = "taxcloud_connected"
    TAXCLOUD_DISCONNECTED = "taxcloud_disconnected"
    EXTERNAL_COMPLIANCE = "external_compliance"

    def visit(
        self,
        taxcloud_invited: typing.Callable[[], T_Result],
        taxcloud_connected: typing.Callable[[], T_Result],
        taxcloud_disconnected: typing.Callable[[], T_Result],
        external_compliance: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetMerchantResponseStatus.TAXCLOUD_INVITED:
            return taxcloud_invited()
        if self is GetMerchantResponseStatus.TAXCLOUD_CONNECTED:
            return taxcloud_connected()
        if self is GetMerchantResponseStatus.TAXCLOUD_DISCONNECTED:
            return taxcloud_disconnected()
        if self is GetMerchantResponseStatus.EXTERNAL_COMPLIANCE:
            return external_compliance()
