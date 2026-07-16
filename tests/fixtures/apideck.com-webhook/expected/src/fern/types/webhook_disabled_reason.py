

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookDisabledReason(enum.StrEnum):
    """
    Indicates if the webhook has has been disabled as it reached its retry limit or if account is over the usage allocated by it's plan.
    """

    NONE = "none"
    RETRY_LIMIT = "retry_limit"
    USAGE_LIMIT = "usage_limit"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        retry_limit: typing.Callable[[], T_Result],
        usage_limit: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebhookDisabledReason.NONE:
            return none()
        if self is WebhookDisabledReason.RETRY_LIMIT:
            return retry_limit()
        if self is WebhookDisabledReason.USAGE_LIMIT:
            return usage_limit()
