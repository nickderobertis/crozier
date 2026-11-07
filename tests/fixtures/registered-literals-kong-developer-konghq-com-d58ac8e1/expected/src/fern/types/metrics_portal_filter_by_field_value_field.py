

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsPortalFilterByFieldValueField(enum.StrEnum):
    """
    The field to filter.
    """

    PORTAL = "portal"

    def visit(self, portal: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsPortalFilterByFieldValueField.PORTAL:
            return portal()
