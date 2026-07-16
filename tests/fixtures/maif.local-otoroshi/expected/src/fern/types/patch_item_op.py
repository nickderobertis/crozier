

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PatchItemOp(str, enum.Enum):
    ADD = "add"
    REPLACE = "replace"
    REMOVE = "remove"
    COPY = "copy"
    TEST = "test"

    def visit(
        self,
        add: typing.Callable[[], T_Result],
        replace: typing.Callable[[], T_Result],
        remove: typing.Callable[[], T_Result],
        copy: typing.Callable[[], T_Result],
        test: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchItemOp.ADD:
            return add()
        if self is PatchItemOp.REPLACE:
            return replace()
        if self is PatchItemOp.REMOVE:
            return remove()
        if self is PatchItemOp.COPY:
            return copy()
        if self is PatchItemOp.TEST:
            return test()
