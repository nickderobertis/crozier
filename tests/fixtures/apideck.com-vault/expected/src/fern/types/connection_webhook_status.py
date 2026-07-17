

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectionWebhookStatus(enum.StrEnum):
    """
    The status of the webhook.
    """

    ENABLED = "enabled"
    DISABLED = "disabled"

    def visit(self, enabled: typing.Callable[[], T_Result], disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConnectionWebhookStatus.ENABLED:
            return enabled()
        if self is ConnectionWebhookStatus.DISABLED:
            return disabled()
