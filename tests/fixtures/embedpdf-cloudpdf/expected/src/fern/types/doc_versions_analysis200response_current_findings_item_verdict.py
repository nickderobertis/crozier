

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocVersionsAnalysis200ResponseCurrentFindingsItemVerdict(enum.StrEnum):
    PERMITTED = "permitted"
    FORBIDDEN = "forbidden"
    INCOMPLETE = "incomplete"

    def visit(
        self,
        permitted: typing.Callable[[], T_Result],
        forbidden: typing.Callable[[], T_Result],
        incomplete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocVersionsAnalysis200ResponseCurrentFindingsItemVerdict.PERMITTED:
            return permitted()
        if self is DocVersionsAnalysis200ResponseCurrentFindingsItemVerdict.FORBIDDEN:
            return forbidden()
        if self is DocVersionsAnalysis200ResponseCurrentFindingsItemVerdict.INCOMPLETE:
            return incomplete()
