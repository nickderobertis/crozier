

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocVersionsSignatures200ResponseSignaturesItemKind(enum.StrEnum):
    SIGNATURE = "signature"
    TIMESTAMP = "timestamp"

    def visit(self, signature: typing.Callable[[], T_Result], timestamp: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocVersionsSignatures200ResponseSignaturesItemKind.SIGNATURE:
            return signature()
        if self is DocVersionsSignatures200ResponseSignaturesItemKind.TIMESTAMP:
            return timestamp()
