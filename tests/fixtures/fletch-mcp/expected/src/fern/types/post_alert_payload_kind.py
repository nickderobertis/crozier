

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostAlertPayloadKind(enum.StrEnum):
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
        if self is PostAlertPayloadKind.LARGE_TRANSFER:
            return large_transfer()
        if self is PostAlertPayloadKind.WALLET_ACTIVITY:
            return wallet_activity()
        if self is PostAlertPayloadKind.AUTHORITY:
            return authority()
        if self is PostAlertPayloadKind.PING:
            return ping()
