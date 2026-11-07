

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsRouteFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    ROUTE = "route"

    def visit(self, route: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsRouteFilterByFieldOneField.ROUTE:
            return route()
