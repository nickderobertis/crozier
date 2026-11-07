

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsControlPlaneFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    CONTROL_PLANE = "control_plane"

    def visit(self, control_plane: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsControlPlaneFilterByFieldOneField.CONTROL_PLANE:
            return control_plane()
