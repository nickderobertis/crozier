

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookSupportSubscriptionLevel(enum.StrEnum):
    """
    Received events are scoped to connection or across integration.
    """

    CONNECTION = "connection"
    INTEGRATION = "integration"

    def visit(self, connection: typing.Callable[[], T_Result], integration: typing.Callable[[], T_Result]) -> T_Result:
        if self is WebhookSupportSubscriptionLevel.CONNECTION:
            return connection()
        if self is WebhookSupportSubscriptionLevel.INTEGRATION:
            return integration()
