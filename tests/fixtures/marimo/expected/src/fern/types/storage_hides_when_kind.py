

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StorageHidesWhenKind(enum.StrEnum):
    STORAGE = "storage"

    def visit(self, storage: typing.Callable[[], T_Result]) -> T_Result:
        if self is StorageHidesWhenKind.STORAGE:
            return storage()
