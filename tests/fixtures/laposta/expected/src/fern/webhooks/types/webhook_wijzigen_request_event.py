

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookWijzigenRequestEvent(enum.StrEnum):
    """
    When will the webhook be requested? (subscribed, modified or deactivated)
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
        if self is WebhookWijzigenRequestEvent.SUBSCRIBED:
            return subscribed()
        if self is WebhookWijzigenRequestEvent.MODIFIED:
            return modified()
        if self is WebhookWijzigenRequestEvent.DEACTIVATED:
            return deactivated()
