

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookToevoegenRequestEvent(enum.StrEnum):
    """
    When will the webhook be requested? (subscribed, modified of deactivated)
    """

    SUBSCRIBED = "subscribed"
    MODIFIED = "modified"
    DEACTIVATED = "deactivated"

    def visit(
        self,
        subscribed: typing.Callable[[], T_Result],
        modified: typing.Callable[[], T_Result],
        deactivated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebhookToevoegenRequestEvent.SUBSCRIBED:
            return subscribed()
        if self is WebhookToevoegenRequestEvent.MODIFIED:
            return modified()
        if self is WebhookToevoegenRequestEvent.DEACTIVATED:
            return deactivated()
