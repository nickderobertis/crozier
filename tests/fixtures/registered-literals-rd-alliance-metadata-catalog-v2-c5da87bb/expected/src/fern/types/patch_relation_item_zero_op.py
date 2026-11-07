

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchRelationItemZeroOp(enum.StrEnum):
    """
    Operation to perform.
    """

    ADD = "add"
    REMOVE = "remove"
    REPLACE = "replace"
    TEST = "test"

    def visit(
        self,
        add: typing.Callable[[], T_Result],
        remove: typing.Callable[[], T_Result],
        replace: typing.Callable[[], T_Result],
        test: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchRelationItemZeroOp.ADD:
            return add()
        if self is PatchRelationItemZeroOp.REMOVE:
            return remove()
        if self is PatchRelationItemZeroOp.REPLACE:
            return replace()
        if self is PatchRelationItemZeroOp.TEST:
            return test()
