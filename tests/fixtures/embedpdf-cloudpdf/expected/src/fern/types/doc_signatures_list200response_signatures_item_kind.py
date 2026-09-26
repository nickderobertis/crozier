

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocSignaturesList200ResponseSignaturesItemKind(enum.StrEnum):
    SIGNATURE = "signature"
    TIMESTAMP = "timestamp"

    def visit(self, signature: typing.Callable[[], T_Result], timestamp: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocSignaturesList200ResponseSignaturesItemKind.SIGNATURE:
            return signature()
        if self is DocSignaturesList200ResponseSignaturesItemKind.TIMESTAMP:
            return timestamp()
