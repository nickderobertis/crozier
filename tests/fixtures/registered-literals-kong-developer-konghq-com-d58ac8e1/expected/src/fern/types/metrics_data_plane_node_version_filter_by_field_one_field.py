

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsDataPlaneNodeVersionFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    DATA_PLANE_NODE_VERSION = "data_plane_node_version"

    def visit(self, data_plane_node_version: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsDataPlaneNodeVersionFilterByFieldOneField.DATA_PLANE_NODE_VERSION:
            return data_plane_node_version()
