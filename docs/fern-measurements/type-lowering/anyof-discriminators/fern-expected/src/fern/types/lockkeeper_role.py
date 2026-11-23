

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LockkeeperRole(enum.StrEnum):
    LOCKKEEPER = "lockkeeper"

    def visit(self, lockkeeper: typing.Callable[[], T_Result]) -> T_Result:
        if self is LockkeeperRole.LOCKKEEPER:
            return lockkeeper()
