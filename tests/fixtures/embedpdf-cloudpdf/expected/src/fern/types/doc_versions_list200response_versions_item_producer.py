

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocVersionsList200ResponseVersionsItemProducer(enum.StrEnum):
    UPLOAD = "upload"
    SIGNATURE = "signature"

    def visit(self, upload: typing.Callable[[], T_Result], signature: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocVersionsList200ResponseVersionsItemProducer.UPLOAD:
            return upload()
        if self is DocVersionsList200ResponseVersionsItemProducer.SIGNATURE:
            return signature()
