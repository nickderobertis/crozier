

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferOperationType(enum.StrEnum):
    """
    Operations:
      * `upload`
      * `download`
    """

    UPLOAD = "upload"
    DOWNLOAD = "download"

    def visit(self, upload: typing.Callable[[], T_Result], download: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransferOperationType.UPLOAD:
            return upload()
        if self is TransferOperationType.DOWNLOAD:
            return download()
