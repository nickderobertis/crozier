

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSigningKeyBodyPrivateJwkRsaKeyOpsItem(enum.StrEnum):
    SIGN = "sign"
    VERIFY = "verify"

    def visit(self, sign: typing.Callable[[], T_Result], verify: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSigningKeyBodyPrivateJwkRsaKeyOpsItem.SIGN:
            return sign()
        if self is CreateSigningKeyBodyPrivateJwkRsaKeyOpsItem.VERIFY:
            return verify()
