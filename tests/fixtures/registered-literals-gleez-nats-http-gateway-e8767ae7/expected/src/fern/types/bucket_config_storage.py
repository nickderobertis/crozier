

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BucketConfigStorage(enum.StrEnum):
    FILE = "file"
    MEMORY = "memory"

    def visit(self, file: typing.Callable[[], T_Result], memory: typing.Callable[[], T_Result]) -> T_Result:
        if self is BucketConfigStorage.FILE:
            return file()
        if self is BucketConfigStorage.MEMORY:
            return memory()
