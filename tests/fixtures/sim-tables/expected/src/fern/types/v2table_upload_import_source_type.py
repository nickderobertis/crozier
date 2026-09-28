

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2TableUploadImportSourceType(enum.StrEnum):
    """
    Upload-backed import discriminator.
    """

    UPLOAD = "upload"

    def visit(self, upload: typing.Callable[[], T_Result]) -> T_Result:
        if self is V2TableUploadImportSourceType.UPLOAD:
            return upload()
