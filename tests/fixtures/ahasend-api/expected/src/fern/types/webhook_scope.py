

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookScope(enum.StrEnum):
    """
    Webhook scope
    """

    GLOBAL = "global"
    SCOPED = "scoped"

    def visit(self, global_: typing.Callable[[], T_Result], scoped: typing.Callable[[], T_Result]) -> T_Result:
        if self is WebhookScope.GLOBAL:
            return global_()
        if self is WebhookScope.SCOPED:
            return scoped()
