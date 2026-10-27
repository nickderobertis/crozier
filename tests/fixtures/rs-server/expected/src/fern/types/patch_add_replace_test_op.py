

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchAddReplaceTestOp(enum.StrEnum):
    ADD = "add"
    REPLACE = "replace"
    TEST = "test"

    def visit(
        self,
        add: typing.Callable[[], T_Result],
        replace: typing.Callable[[], T_Result],
        test: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchAddReplaceTestOp.ADD:
            return add()
        if self is PatchAddReplaceTestOp.REPLACE:
            return replace()
        if self is PatchAddReplaceTestOp.TEST:
            return test()
