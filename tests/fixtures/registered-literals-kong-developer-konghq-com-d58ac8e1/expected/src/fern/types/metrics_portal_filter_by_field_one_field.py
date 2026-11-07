

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsPortalFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    PORTAL = "portal"

    def visit(self, portal: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsPortalFilterByFieldOneField.PORTAL:
            return portal()
