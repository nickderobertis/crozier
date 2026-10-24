

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookObject(enum.StrEnum):
    """
    Object type identifier
    """

    WEBHOOK = "webhook"

    def visit(self, webhook: typing.Callable[[], T_Result]) -> T_Result:
        if self is WebhookObject.WEBHOOK:
            return webhook()
