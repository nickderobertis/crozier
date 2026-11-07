

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsUpstreamStatusCodeGroupedFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    UPSTREAM_STATUS_CODE_GROUPED = "upstream_status_code_grouped"

    def visit(self, upstream_status_code_grouped: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsUpstreamStatusCodeGroupedFilterByFieldOneField.UPSTREAM_STATUS_CODE_GROUPED:
            return upstream_status_code_grouped()
