

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsApiFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    API = "api"

    def visit(self, api: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsApiFilterByFieldOneField.API:
            return api()
