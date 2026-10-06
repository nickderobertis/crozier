

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConsumerCapabilitiesNotificationOp(enum.StrEnum):
    CONSUMER_CAPABILITIES = "consumer-capabilities"

    def visit(self, consumer_capabilities: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConsumerCapabilitiesNotificationOp.CONSUMER_CAPABILITIES:
            return consumer_capabilities()
