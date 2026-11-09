

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsStatusCodeGroupedFilterByFieldOneField(enum.StrEnum):
    """
    The field to filter.
    """

    STATUS_CODE_GROUPED = "status_code_grouped"

    def visit(self, status_code_grouped: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsStatusCodeGroupedFilterByFieldOneField.STATUS_CODE_GROUPED:
            return status_code_grouped()
