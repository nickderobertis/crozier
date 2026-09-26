

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocSignaturesAnalysis200ResponseCurrentVerdict(enum.StrEnum):
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
        if self is DocSignaturesAnalysis200ResponseCurrentVerdict.UNCHANGED:
            return unchanged()
        if self is DocSignaturesAnalysis200ResponseCurrentVerdict.PERMITTED:
            return permitted()
        if self is DocSignaturesAnalysis200ResponseCurrentVerdict.FORBIDDEN:
            return forbidden()
        if self is DocSignaturesAnalysis200ResponseCurrentVerdict.INDETERMINATE:
            return indeterminate()
