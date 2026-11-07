

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetPprofDataRequestHandler(enum.StrEnum):
    ALLOCS = "allocs"
    BLOCK = "block"
    CMDLINE = "cmdline"
    GOROUTINE = "goroutine"
    HEAP = "heap"
    MUTEX = "mutex"
    PROFILE = "profile"
    THREADCREATE = "threadcreate"
    TRACE = "trace"

    def visit(
        self,
        allocs: typing.Callable[[], T_Result],
        block: typing.Callable[[], T_Result],
        cmdline: typing.Callable[[], T_Result],
        goroutine: typing.Callable[[], T_Result],
        heap: typing.Callable[[], T_Result],
        mutex: typing.Callable[[], T_Result],
        profile: typing.Callable[[], T_Result],
        threadcreate: typing.Callable[[], T_Result],
        trace: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetPprofDataRequestHandler.ALLOCS:
            return allocs()
        if self is GetPprofDataRequestHandler.BLOCK:
            return block()
        if self is GetPprofDataRequestHandler.CMDLINE:
            return cmdline()
        if self is GetPprofDataRequestHandler.GOROUTINE:
            return goroutine()
        if self is GetPprofDataRequestHandler.HEAP:
            return heap()
        if self is GetPprofDataRequestHandler.MUTEX:
            return mutex()
        if self is GetPprofDataRequestHandler.PROFILE:
            return profile()
        if self is GetPprofDataRequestHandler.THREADCREATE:
            return threadcreate()
        if self is GetPprofDataRequestHandler.TRACE:
            return trace()
