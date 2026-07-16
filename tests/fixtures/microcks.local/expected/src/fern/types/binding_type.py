

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BindingType(enum.StrEnum):
    """
    Protocol binding identifier
    """

    KAFKA = "KAFKA"
    MQTT = "MQTT"
    WS = "WS"
    AMQP = "AMQP"
    NATS = "NATS"
    GOOGLEPUBSUB = "GOOGLEPUBSUB"

    def visit(
        self,
        kafka: typing.Callable[[], T_Result],
        mqtt: typing.Callable[[], T_Result],
        ws: typing.Callable[[], T_Result],
        amqp: typing.Callable[[], T_Result],
        nats: typing.Callable[[], T_Result],
        googlepubsub: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BindingType.KAFKA:
            return kafka()
        if self is BindingType.MQTT:
            return mqtt()
        if self is BindingType.WS:
            return ws()
        if self is BindingType.AMQP:
            return amqp()
        if self is BindingType.NATS:
            return nats()
        if self is BindingType.GOOGLEPUBSUB:
            return googlepubsub()
