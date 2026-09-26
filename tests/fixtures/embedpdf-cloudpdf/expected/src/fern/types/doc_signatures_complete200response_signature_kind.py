

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocSignaturesComplete200ResponseSignatureKind(enum.StrEnum):
    SIGNATURE = "signature"
    TIMESTAMP = "timestamp"

    def visit(self, signature: typing.Callable[[], T_Result], timestamp: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocSignaturesComplete200ResponseSignatureKind.SIGNATURE:
            return signature()
        if self is DocSignaturesComplete200ResponseSignatureKind.TIMESTAMP:
            return timestamp()
