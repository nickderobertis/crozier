

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryTagsFormat(enum.StrEnum):
    STANDARD = "standard"
    SQLCOMMENTER = "sqlcommenter"
    STANDARD_PREPENDED = "standard_prepended"

    def visit(
        self,
        standard: typing.Callable[[], T_Result],
        sqlcommenter: typing.Callable[[], T_Result],
        standard_prepended: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is QueryTagsFormat.STANDARD:
            return standard()
        if self is QueryTagsFormat.SQLCOMMENTER:
            return sqlcommenter()
        if self is QueryTagsFormat.STANDARD_PREPENDED:
            return standard_prepended()
