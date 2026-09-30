

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OtelExporterConfigTracesPropagatorsItem(enum.StrEnum):
    """
    Possible trace propagators to use with OTLP
    """

    B3 = "b3"
    TRACECONTEXT = "tracecontext"

    def visit(self, b3: typing.Callable[[], T_Result], tracecontext: typing.Callable[[], T_Result]) -> T_Result:
        if self is OtelExporterConfigTracesPropagatorsItem.B3:
            return b3()
        if self is OtelExporterConfigTracesPropagatorsItem.TRACECONTEXT:
            return tracecontext()
