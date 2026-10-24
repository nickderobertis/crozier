

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RouteObject(enum.StrEnum):
    """
    Object type identifier
    """

    ROUTE = "route"

    def visit(self, route: typing.Callable[[], T_Result]) -> T_Result:
        if self is RouteObject.ROUTE:
            return route()
