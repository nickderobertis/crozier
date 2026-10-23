

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetWatchersIdResponseWatcherKind(enum.StrEnum):
    LARGE_TRANSFER = "large_transfer"
    WALLET_ACTIVITY = "wallet_activity"
    REGISTRY_EVENT = "registry_event"
    LISTING_EVENT = "listing_event"
    TOKEN_EVENT = "token_event"
    NEW_POOL = "new_pool"

    def visit(
        self,
        large_transfer: typing.Callable[[], T_Result],
        wallet_activity: typing.Callable[[], T_Result],
        registry_event: typing.Callable[[], T_Result],
        listing_event: typing.Callable[[], T_Result],
        token_event: typing.Callable[[], T_Result],
        new_pool: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetWatchersIdResponseWatcherKind.LARGE_TRANSFER:
            return large_transfer()
        if self is GetWatchersIdResponseWatcherKind.WALLET_ACTIVITY:
            return wallet_activity()
        if self is GetWatchersIdResponseWatcherKind.REGISTRY_EVENT:
            return registry_event()
        if self is GetWatchersIdResponseWatcherKind.LISTING_EVENT:
            return listing_event()
        if self is GetWatchersIdResponseWatcherKind.TOKEN_EVENT:
            return token_event()
        if self is GetWatchersIdResponseWatcherKind.NEW_POOL:
            return new_pool()
