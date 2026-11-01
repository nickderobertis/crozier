

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class InferredReturnsMixedEnumResponseResultDataValueZero(enum.StrEnum):
    FOO = "FOO"

    def visit(self, foo: typing.Callable[[], T_Result]) -> T_Result:
        if self is InferredReturnsMixedEnumResponseResultDataValueZero.FOO:
            return foo()
