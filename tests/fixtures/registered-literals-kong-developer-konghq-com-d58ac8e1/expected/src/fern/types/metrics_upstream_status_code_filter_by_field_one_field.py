

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsUpstreamStatusCodeFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    UPSTREAM_STATUS_CODE = "upstream_status_code"

    def visit(self, upstream_status_code: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsUpstreamStatusCodeFilterByFieldOneField.UPSTREAM_STATUS_CODE:
            return upstream_status_code()
