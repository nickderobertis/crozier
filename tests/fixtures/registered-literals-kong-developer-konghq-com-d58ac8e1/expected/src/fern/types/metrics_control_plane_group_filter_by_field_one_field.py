

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsControlPlaneGroupFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    CONTROL_PLANE_GROUP = "control_plane_group"

    def visit(self, control_plane_group: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsControlPlaneGroupFilterByFieldOneField.CONTROL_PLANE_GROUP:
            return control_plane_group()
