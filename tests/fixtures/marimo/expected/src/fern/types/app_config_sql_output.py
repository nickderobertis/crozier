

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppConfigSqlOutput(enum.StrEnum):
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
        if self is AppConfigSqlOutput.AUTO:
            return auto()
        if self is AppConfigSqlOutput.LAZY_POLARS:
            return lazy_polars()
        if self is AppConfigSqlOutput.NATIVE:
            return native()
        if self is AppConfigSqlOutput.PANDAS:
            return pandas()
        if self is AppConfigSqlOutput.POLARS:
            return polars()
