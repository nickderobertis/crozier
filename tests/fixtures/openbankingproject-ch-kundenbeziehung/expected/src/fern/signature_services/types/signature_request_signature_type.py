

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SignatureRequestSignatureType(enum.StrEnum):
    QES = "qes"
    AES = "aes"
    SIMPLE = "simple"

    def visit(
        self,
        qes: typing.Callable[[], T_Result],
        aes: typing.Callable[[], T_Result],
        simple: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SignatureRequestSignatureType.QES:
            return qes()
        if self is SignatureRequestSignatureType.AES:
            return aes()
        if self is SignatureRequestSignatureType.SIMPLE:
            return simple()
