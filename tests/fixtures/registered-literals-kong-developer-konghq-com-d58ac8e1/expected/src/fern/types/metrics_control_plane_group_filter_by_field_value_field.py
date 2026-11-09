

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsControlPlaneGroupFilterByFieldValueField(enum.StrEnum):
    """
    The field to filter.
    """

    CONTROL_PLANE_GROUP = "control_plane_group"

    def visit(self, control_plane_group: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsControlPlaneGroupFilterByFieldValueField.CONTROL_PLANE_GROUP:
            return control_plane_group()
