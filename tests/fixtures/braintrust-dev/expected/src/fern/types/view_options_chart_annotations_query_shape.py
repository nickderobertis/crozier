

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ViewOptionsChartAnnotationsQueryShape(enum.StrEnum):
    TRACES = "traces"
    SPANS = "spans"

    def visit(self, traces: typing.Callable[[], T_Result], spans: typing.Callable[[], T_Result]) -> T_Result:
        if self is ViewOptionsChartAnnotationsQueryShape.TRACES:
            return traces()
        if self is ViewOptionsChartAnnotationsQueryShape.SPANS:
            return spans()
