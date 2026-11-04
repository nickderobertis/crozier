

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateAgentWebhookRequestWebhookType(enum.StrEnum):
    PRE_CALL = "pre_call"
    POST_CALL = "post_call"

    def visit(self, pre_call: typing.Callable[[], T_Result], post_call: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateAgentWebhookRequestWebhookType.PRE_CALL:
            return pre_call()
        if self is CreateAgentWebhookRequestWebhookType.POST_CALL:
            return post_call()
