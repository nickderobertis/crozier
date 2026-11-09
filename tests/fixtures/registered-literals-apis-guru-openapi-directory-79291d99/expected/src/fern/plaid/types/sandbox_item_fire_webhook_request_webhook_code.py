

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SandboxItemFireWebhookRequestWebhookCode(enum.StrEnum):
    """
    The webhook codes that can be fired by this test endpoint.
    """

    DEFAULT_UPDATE = "DEFAULT_UPDATE"
    NEW_ACCOUNTS_AVAILABLE = "NEW_ACCOUNTS_AVAILABLE"
    AUTH_DATA_UPDATE = "AUTH_DATA_UPDATE"
    RECURRING_TRANSACTIONS_UPDATE = "RECURRING_TRANSACTIONS_UPDATE"
    SYNC_UPDATES_AVAILABLE = "SYNC_UPDATES_AVAILABLE"

    def visit(
        self,
        default_update: typing.Callable[[], T_Result],
        new_accounts_available: typing.Callable[[], T_Result],
        auth_data_update: typing.Callable[[], T_Result],
        recurring_transactions_update: typing.Callable[[], T_Result],
        sync_updates_available: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SandboxItemFireWebhookRequestWebhookCode.DEFAULT_UPDATE:
            return default_update()
        if self is SandboxItemFireWebhookRequestWebhookCode.NEW_ACCOUNTS_AVAILABLE:
            return new_accounts_available()
        if self is SandboxItemFireWebhookRequestWebhookCode.AUTH_DATA_UPDATE:
            return auth_data_update()
        if self is SandboxItemFireWebhookRequestWebhookCode.RECURRING_TRANSACTIONS_UPDATE:
            return recurring_transactions_update()
        if self is SandboxItemFireWebhookRequestWebhookCode.SYNC_UPDATES_AVAILABLE:
            return sync_updates_available()
