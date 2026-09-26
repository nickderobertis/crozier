

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocVersionsAnalysis200ResponseVerdict(enum.StrEnum):
    UNCHANGED = "unchanged"
    PERMITTED = "permitted"
    FORBIDDEN = "forbidden"
    INDETERMINATE = "indeterminate"

    def visit(
        self,
        unchanged: typing.Callable[[], T_Result],
        permitted: typing.Callable[[], T_Result],
        forbidden: typing.Callable[[], T_Result],
        indeterminate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocVersionsAnalysis200ResponseVerdict.UNCHANGED:
            return unchanged()
        if self is DocVersionsAnalysis200ResponseVerdict.PERMITTED:
            return permitted()
        if self is DocVersionsAnalysis200ResponseVerdict.FORBIDDEN:
            return forbidden()
        if self is DocVersionsAnalysis200ResponseVerdict.INDETERMINATE:
            return indeterminate()
