

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UploadImportSourceType(enum.StrEnum):
    LOCAL = "local"
    HTTP = "http"

    def visit(self, local: typing.Callable[[], T_Result], http: typing.Callable[[], T_Result]) -> T_Result:
        if self is UploadImportSourceType.LOCAL:
            return local()
        if self is UploadImportSourceType.HTTP:
            return http()
