

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsConsumerFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    CONSUMER = "consumer"

    def visit(self, consumer: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsConsumerFilterByFieldOneField.CONSUMER:
            return consumer()
