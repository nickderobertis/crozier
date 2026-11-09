

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsResponseSourceFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    RESPONSE_SOURCE = "response_source"

    def visit(self, response_source: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsResponseSourceFilterByFieldOneField.RESPONSE_SOURCE:
            return response_source()
