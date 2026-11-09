

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricsStatusCodeFilterByFieldValueField(enum.StrEnum):
    """
    The field to filter.
    """

    STATUS_CODE = "status_code"

    def visit(self, status_code: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetricsStatusCodeFilterByFieldValueField.STATUS_CODE:
            return status_code()
