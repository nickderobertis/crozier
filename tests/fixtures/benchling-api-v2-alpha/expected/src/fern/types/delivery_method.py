

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeliveryMethod(enum.StrEnum):
    """
    The delivery method for the subscriptions. Currently only webhook is supported.
    """

    WEBHOOK = "WEBHOOK"

    def visit(self, webhook: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeliveryMethod.WEBHOOK:
            return webhook()
