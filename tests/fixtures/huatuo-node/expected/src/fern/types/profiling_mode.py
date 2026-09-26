

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProfilingMode(enum.StrEnum):
    ON_CPU = "oncpu"
    OFF_CPU = "offcpu"
    OBJECT_ALLOC = "object_alloc"
    OBJECT_USAGE = "object_usage"
    VIRTUAL_ALLOC = "virtual_alloc"
    PHYSICAL_ALLOC = "physical_alloc"
    PHYSICAL_USAGE = "physical_usage"

    def visit(
        self,
        on_cpu: typing.Callable[[], T_Result],
        off_cpu: typing.Callable[[], T_Result],
        object_alloc: typing.Callable[[], T_Result],
        object_usage: typing.Callable[[], T_Result],
        virtual_alloc: typing.Callable[[], T_Result],
        physical_alloc: typing.Callable[[], T_Result],
        physical_usage: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProfilingMode.ON_CPU:
            return on_cpu()
        if self is ProfilingMode.OFF_CPU:
            return off_cpu()
        if self is ProfilingMode.OBJECT_ALLOC:
            return object_alloc()
        if self is ProfilingMode.OBJECT_USAGE:
            return object_usage()
        if self is ProfilingMode.VIRTUAL_ALLOC:
            return virtual_alloc()
        if self is ProfilingMode.PHYSICAL_ALLOC:
            return physical_alloc()
        if self is ProfilingMode.PHYSICAL_USAGE:
            return physical_usage()
