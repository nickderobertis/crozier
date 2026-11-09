

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsApplicationFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    APPLICATION = "application"

    def visit(self, application: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsApplicationFilterByFieldOneField.APPLICATION:
            return application()
