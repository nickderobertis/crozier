

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocVersionsAnalysis200ResponseMode(enum.StrEnum):
    AUTHORITATIVE = "authoritative"
    EXPLORATORY = "exploratory"

    def visit(
        self, authoritative: typing.Callable[[], T_Result], exploratory: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is DocVersionsAnalysis200ResponseMode.AUTHORITATIVE:
            return authoritative()
        if self is DocVersionsAnalysis200ResponseMode.EXPLORATORY:
            return exploratory()
