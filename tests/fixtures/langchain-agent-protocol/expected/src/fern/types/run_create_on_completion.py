

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunCreateOnCompletion(enum.StrEnum):
    """
    Whether to delete or keep the thread when run completes. Must be one of 'delete' or 'keep'. Defaults to 'delete' when thread_id not provided, otherwise 'keep'.
    """

    DELETE = "delete"
    KEEP = "keep"

    def visit(self, delete: typing.Callable[[], T_Result], keep: typing.Callable[[], T_Result]) -> T_Result:
        if self is RunCreateOnCompletion.DELETE:
            return delete()
        if self is RunCreateOnCompletion.KEEP:
            return keep()
