

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileStorageType(enum.StrEnum):
    S3 = "s3"

    def visit(self, s3: typing.Callable[[], T_Result]) -> T_Result:
        if self is FileStorageType.S3:
            return s3()
