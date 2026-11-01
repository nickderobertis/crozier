

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ComplexTypesLiteralResponseResultDataStrLit(enum.StrEnum):
    HELLO = "hello"

    def visit(self, hello: typing.Callable[[], T_Result]) -> T_Result:
        if self is ComplexTypesLiteralResponseResultDataStrLit.HELLO:
            return hello()
