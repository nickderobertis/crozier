

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinkType(enum.StrEnum):
    PRESIGNED = "PRESIGNED"
    S3 = "S3"

    def visit(self, presigned: typing.Callable[[], T_Result], s3: typing.Callable[[], T_Result]) -> T_Result:
        if self is LinkType.PRESIGNED:
            return presigned()
        if self is LinkType.S3:
            return s3()
