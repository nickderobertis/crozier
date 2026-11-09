

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsRouteFilterByFieldValueField(enum.StrEnum):
    """
    The field to filter.
    """

    ROUTE = "route"

    def visit(self, route: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsRouteFilterByFieldValueField.ROUTE:
            return route()
