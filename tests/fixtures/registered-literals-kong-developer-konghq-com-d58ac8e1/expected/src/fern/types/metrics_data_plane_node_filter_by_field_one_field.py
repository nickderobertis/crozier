

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsDataPlaneNodeFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    DATA_PLANE_NODE = "data_plane_node"

    def visit(self, data_plane_node: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsDataPlaneNodeFilterByFieldOneField.DATA_PLANE_NODE:
            return data_plane_node()
