

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteDirectoryBehavior(enum.StrEnum):
    """
    Whether a delete can remove a non-empty directory.
    """

    NON_RECURSIVE = "non_recursive"
    RECURSIVE = "recursive"

    def visit(self, non_recursive: typing.Callable[[], T_Result], recursive: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteDirectoryBehavior.NON_RECURSIVE:
            return non_recursive()
        if self is DeleteDirectoryBehavior.RECURSIVE:
            return recursive()
