

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookState(enum.StrEnum):
    """
    The status of this webhook: active or deleted
    """

    ACTIVE = "active"
    DELETED = "deleted"

    def visit(self, active: typing.Callable[[], T_Result], deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is WebhookState.ACTIVE:
            return active()
        if self is WebhookState.DELETED:
            return deleted()
