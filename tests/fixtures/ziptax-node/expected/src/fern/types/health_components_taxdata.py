

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthComponentsTaxdata(enum.StrEnum):
    """
    Tax-data cache status: 'ok', 'empty' (cache not loaded), or 'partial' (fewer than the expected number of records loaded).
    """

    OK = "ok"
    EMPTY = "empty"
    PARTIAL = "partial"

    def visit(
        self,
        ok: typing.Callable[[], T_Result],
        empty: typing.Callable[[], T_Result],
        partial: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HealthComponentsTaxdata.OK:
            return ok()
        if self is HealthComponentsTaxdata.EMPTY:
            return empty()
        if self is HealthComponentsTaxdata.PARTIAL:
            return partial()
