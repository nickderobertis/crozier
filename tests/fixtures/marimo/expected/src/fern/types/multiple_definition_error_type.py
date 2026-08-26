

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MultipleDefinitionErrorType(enum.StrEnum):
    MULTIPLE_DEFS = "multiple-defs"

    def visit(self, multiple_defs: typing.Callable[[], T_Result]) -> T_Result:
        if self is MultipleDefinitionErrorType.MULTIPLE_DEFS:
            return multiple_defs()
