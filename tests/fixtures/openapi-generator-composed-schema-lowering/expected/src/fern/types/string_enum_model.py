

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StringEnumModel(enum.StrEnum):
    FOO = "foo"
    BAR = "bar"

    def visit(self, foo: typing.Callable[[], T_Result], bar: typing.Callable[[], T_Result]) -> T_Result:
        if self is StringEnumModel.FOO:
            return foo()
        if self is StringEnumModel.BAR:
            return bar()
