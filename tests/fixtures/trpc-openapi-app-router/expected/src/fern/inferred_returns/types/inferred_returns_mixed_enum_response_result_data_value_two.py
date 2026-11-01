

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class InferredReturnsMixedEnumResponseResultDataValueTwo(enum.StrEnum):
    BAZ = "BAZ"

    def visit(self, baz: typing.Callable[[], T_Result]) -> T_Result:
        if self is InferredReturnsMixedEnumResponseResultDataValueTwo.BAZ:
            return baz()
