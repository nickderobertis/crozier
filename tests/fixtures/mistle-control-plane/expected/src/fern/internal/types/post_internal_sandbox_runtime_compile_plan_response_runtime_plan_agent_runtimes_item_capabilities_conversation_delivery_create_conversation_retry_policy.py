

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemCapabilitiesConversationDeliveryCreateConversationRetryPolicy(
    enum.StrEnum
):
    IDEMPOTENT = "idempotent"
    SINGLE_ATTEMPT = "single_attempt"

    def visit(
        self, idempotent: typing.Callable[[], T_Result], single_attempt: typing.Callable[[], T_Result]
    ) -> T_Result:
        if (
            self
            is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemCapabilitiesConversationDeliveryCreateConversationRetryPolicy.IDEMPOTENT
        ):
            return idempotent()
        if (
            self
            is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAgentRuntimesItemCapabilitiesConversationDeliveryCreateConversationRetryPolicy.SINGLE_ATTEMPT
        ):
            return single_attempt()
