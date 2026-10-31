

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobAcceptedOperation(enum.StrEnum):
    PARSE = "parse"
    EXTRACT = "extract"

    def visit(self, parse: typing.Callable[[], T_Result], extract: typing.Callable[[], T_Result]) -> T_Result:
        if self is JobAcceptedOperation.PARSE:
            return parse()
        if self is JobAcceptedOperation.EXTRACT:
            return extract()
