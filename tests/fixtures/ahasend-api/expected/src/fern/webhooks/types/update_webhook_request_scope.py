

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateWebhookRequestScope(enum.StrEnum):
    """
    Webhook scope. Omit or send null to keep the current scope.
    """

    GLOBAL = "global"
    SCOPED = "scoped"

    def visit(self, global_: typing.Callable[[], T_Result], scoped: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateWebhookRequestScope.GLOBAL:
            return global_()
        if self is UpdateWebhookRequestScope.SCOPED:
            return scoped()
