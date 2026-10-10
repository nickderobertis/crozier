

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IngestedDocObject(enum.StrEnum):
    INGEST_DOCUMENT = "ingest.document"

    def visit(self, ingest_document: typing.Callable[[], T_Result]) -> T_Result:
        if self is IngestedDocObject.INGEST_DOCUMENT:
            return ingest_document()
