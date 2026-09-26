

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderHealthRowStatus(enum.StrEnum):
    OK = "ok"
    WARN = "warn"
    ERROR = "error"

    def visit(
        self,
        ok: typing.Callable[[], T_Result],
        warn: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProviderHealthRowStatus.OK:
            return ok()
        if self is ProviderHealthRowStatus.WARN:
            return warn()
        if self is ProviderHealthRowStatus.ERROR:
            return error()
