

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RuntimeConfigDefaultSqlOutput(enum.StrEnum):
    AUTO = "auto"
    LAZY_POLARS = "lazy-polars"
    NATIVE = "native"
    PANDAS = "pandas"
    POLARS = "polars"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        lazy_polars: typing.Callable[[], T_Result],
        native: typing.Callable[[], T_Result],
        pandas: typing.Callable[[], T_Result],
        polars: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RuntimeConfigDefaultSqlOutput.AUTO:
            return auto()
        if self is RuntimeConfigDefaultSqlOutput.LAZY_POLARS:
            return lazy_polars()
        if self is RuntimeConfigDefaultSqlOutput.NATIVE:
            return native()
        if self is RuntimeConfigDefaultSqlOutput.PANDAS:
            return pandas()
        if self is RuntimeConfigDefaultSqlOutput.POLARS:
            return polars()
