

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookPostStatus(enum.StrEnum):
    """
    Status of the Webhook. `created` will register the webhook in the created state and the service instance will attempt to start sending events. `disabled` will register the webhook in a disabled state and will not send events. Assumed to be `created` if not set.
    """

    CREATED = "created"
    DISABLED = "disabled"

    def visit(self, created: typing.Callable[[], T_Result], disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is WebhookPostStatus.CREATED:
            return created()
        if self is WebhookPostStatus.DISABLED:
            return disabled()
