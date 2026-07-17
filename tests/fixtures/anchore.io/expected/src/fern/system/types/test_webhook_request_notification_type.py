

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TestWebhookRequestNotificationType(enum.StrEnum):
    TAG_UPDATE = "tag_update"
    ANALYSIS_UPDATE = "analysis_update"
    VULN_UPDATE = "vuln_update"
    POLICY_EVAL = "policy_eval"

    def visit(
        self,
        tag_update: typing.Callable[[], T_Result],
        analysis_update: typing.Callable[[], T_Result],
        vuln_update: typing.Callable[[], T_Result],
        policy_eval: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TestWebhookRequestNotificationType.TAG_UPDATE:
            return tag_update()
        if self is TestWebhookRequestNotificationType.ANALYSIS_UPDATE:
            return analysis_update()
        if self is TestWebhookRequestNotificationType.VULN_UPDATE:
            return vuln_update()
        if self is TestWebhookRequestNotificationType.POLICY_EVAL:
            return policy_eval()
