

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunCreateStatelessOnCompletion(enum.StrEnum):
    """
    Whether to delete or keep the thread created for a stateless run. Must be one of 'delete' or 'keep'.
    """

    DELETE = "delete"
    KEEP = "keep"

    def visit(self, delete: typing.Callable[[], T_Result], keep: typing.Callable[[], T_Result]) -> T_Result:
        if self is RunCreateStatelessOnCompletion.DELETE:
            return delete()
        if self is RunCreateStatelessOnCompletion.KEEP:
            return keep()
