

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchRelationItemOneOp(enum.StrEnum):
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
        if self is PatchRelationItemOneOp.ADD:
            return add()
        if self is PatchRelationItemOneOp.REMOVE:
            return remove()
        if self is PatchRelationItemOneOp.REPLACE:
            return replace()
        if self is PatchRelationItemOneOp.TEST:
            return test()
