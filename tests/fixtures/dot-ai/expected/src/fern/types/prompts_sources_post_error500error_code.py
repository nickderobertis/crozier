

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PromptsSourcesPostError500ErrorCode(enum.StrEnum):
    PROMPTS_SOURCE_INGEST_ERROR = "PROMPTS_SOURCE_INGEST_ERROR"

    def visit(self, prompts_source_ingest_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is PromptsSourcesPostError500ErrorCode.PROMPTS_SOURCE_INGEST_ERROR:
            return prompts_source_ingest_error()
