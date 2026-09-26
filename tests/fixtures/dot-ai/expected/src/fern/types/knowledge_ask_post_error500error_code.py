

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KnowledgeAskPostError500ErrorCode(enum.StrEnum):
    SEARCH_ERROR = "SEARCH_ERROR"
    SYNTHESIS_ERROR = "SYNTHESIS_ERROR"

    def visit(
        self, search_error: typing.Callable[[], T_Result], synthesis_error: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is KnowledgeAskPostError500ErrorCode.SEARCH_ERROR:
            return search_error()
        if self is KnowledgeAskPostError500ErrorCode.SYNTHESIS_ERROR:
            return synthesis_error()
