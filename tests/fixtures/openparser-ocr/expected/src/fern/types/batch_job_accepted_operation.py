

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BatchJobAcceptedOperation(enum.StrEnum):
    PARSE_BATCH = "parse_batch"
    EXTRACT_BATCH = "extract_batch"

    def visit(
        self, parse_batch: typing.Callable[[], T_Result], extract_batch: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is BatchJobAcceptedOperation.PARSE_BATCH:
            return parse_batch()
        if self is BatchJobAcceptedOperation.EXTRACT_BATCH:
            return extract_batch()
