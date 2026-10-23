

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookDeliveryKind(enum.StrEnum):
    LARGE_TRANSFER = "large_transfer"
    WALLET_ACTIVITY = "wallet_activity"
    AUTHORITY = "authority"
    PING = "ping"

    def visit(
        self,
        large_transfer: typing.Callable[[], T_Result],
        wallet_activity: typing.Callable[[], T_Result],
        authority: typing.Callable[[], T_Result],
        ping: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebhookDeliveryKind.LARGE_TRANSFER:
            return large_transfer()
        if self is WebhookDeliveryKind.WALLET_ACTIVITY:
            return wallet_activity()
        if self is WebhookDeliveryKind.AUTHORITY:
            return authority()
        if self is WebhookDeliveryKind.PING:
            return ping()
