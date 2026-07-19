

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TraceDepth(enum.StrEnum):
    MINIMUM = "MINIMUM"
    MEDIUM = "MEDIUM"
    MAXIMUM = "MAXIMUM"
    MINIMUM_WO_VENDOR_EXTENSION = "MINIMUM_WO_VENDOR_EXTENSION"
    MEDIUM_WO_VENDOR_EXTENSION = "MEDIUM_WO_VENDOR_EXTENSION"
    MAXIMUM_WO_VENDOR_EXTENSION = "MAXIMUM_WO_VENDOR_EXTENSION"

    def visit(
        self,
        minimum: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        maximum: typing.Callable[[], T_Result],
        minimum_wo_vendor_extension: typing.Callable[[], T_Result],
        medium_wo_vendor_extension: typing.Callable[[], T_Result],
        maximum_wo_vendor_extension: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TraceDepth.MINIMUM:
            return minimum()
        if self is TraceDepth.MEDIUM:
            return medium()
        if self is TraceDepth.MAXIMUM:
            return maximum()
        if self is TraceDepth.MINIMUM_WO_VENDOR_EXTENSION:
            return minimum_wo_vendor_extension()
        if self is TraceDepth.MEDIUM_WO_VENDOR_EXTENSION:
            return medium_wo_vendor_extension()
        if self is TraceDepth.MAXIMUM_WO_VENDOR_EXTENSION:
            return maximum_wo_vendor_extension()
