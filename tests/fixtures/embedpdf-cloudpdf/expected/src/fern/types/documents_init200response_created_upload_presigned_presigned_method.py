

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentsInit200ResponseCreatedUploadPresignedPresignedMethod(enum.StrEnum):
    PUT = "PUT"

    def visit(self, put: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocumentsInit200ResponseCreatedUploadPresignedPresignedMethod.PUT:
            return put()
