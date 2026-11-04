

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowRetryPolicyWebhookOnRetry(enum.StrEnum):
    """
    Whether to send a webhook for every attempt or only the final attempt
    """

    FINAL_ONLY = "final_only"
    EVERY_ATTEMPT = "every_attempt"

    def visit(
        self, final_only: typing.Callable[[], T_Result], every_attempt: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is WorkflowRetryPolicyWebhookOnRetry.FINAL_ONLY:
            return final_only()
        if self is WorkflowRetryPolicyWebhookOnRetry.EVERY_ATTEMPT:
            return every_attempt()
