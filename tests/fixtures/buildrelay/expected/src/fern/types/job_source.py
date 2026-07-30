

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobSource(enum.StrEnum):
    """
    Job source type
    """

    FILESYSTEM = "filesystem"

    def visit(self, filesystem: typing.Callable[[], T_Result]) -> T_Result:
        if self is JobSource.FILESYSTEM:
            return filesystem()
