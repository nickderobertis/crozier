

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocVersionsAnalysis200ResponseBasisSource(enum.StrEnum):
    PERSISTED = "persisted"
    WORKING_COPY = "working-copy"

    def visit(self, persisted: typing.Callable[[], T_Result], working_copy: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocVersionsAnalysis200ResponseBasisSource.PERSISTED:
            return persisted()
        if self is DocVersionsAnalysis200ResponseBasisSource.WORKING_COPY:
            return working_copy()
