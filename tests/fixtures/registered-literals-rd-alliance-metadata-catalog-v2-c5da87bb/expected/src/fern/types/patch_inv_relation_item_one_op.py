

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchInvRelationItemOneOp(enum.StrEnum):
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
        if self is PatchInvRelationItemOneOp.ADD:
            return add()
        if self is PatchInvRelationItemOneOp.REMOVE:
            return remove()
        if self is PatchInvRelationItemOneOp.REPLACE:
            return replace()
        if self is PatchInvRelationItemOneOp.TEST:
            return test()
