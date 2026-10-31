

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobOperation(enum.StrEnum):
    PARSE = "parse"
    EXTRACT = "extract"
    PARSE_BATCH = "parse_batch"
    EXTRACT_BATCH = "extract_batch"

    def visit(
        self,
        parse: typing.Callable[[], T_Result],
        extract: typing.Callable[[], T_Result],
        parse_batch: typing.Callable[[], T_Result],
        extract_batch: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobOperation.PARSE:
            return parse()
        if self is JobOperation.EXTRACT:
            return extract()
        if self is JobOperation.PARSE_BATCH:
            return parse_batch()
        if self is JobOperation.EXTRACT_BATCH:
            return extract_batch()
