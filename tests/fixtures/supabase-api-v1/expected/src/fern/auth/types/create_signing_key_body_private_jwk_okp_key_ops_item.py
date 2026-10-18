

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSigningKeyBodyPrivateJwkOkpKeyOpsItem(enum.StrEnum):
    SIGN = "sign"
    VERIFY = "verify"

    def visit(self, sign: typing.Callable[[], T_Result], verify: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSigningKeyBodyPrivateJwkOkpKeyOpsItem.SIGN:
            return sign()
        if self is CreateSigningKeyBodyPrivateJwkOkpKeyOpsItem.VERIFY:
            return verify()
