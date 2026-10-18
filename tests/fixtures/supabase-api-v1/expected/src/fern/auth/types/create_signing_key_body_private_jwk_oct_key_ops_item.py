

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSigningKeyBodyPrivateJwkOctKeyOpsItem(enum.StrEnum):
    SIGN = "sign"
    VERIFY = "verify"

    def visit(self, sign: typing.Callable[[], T_Result], verify: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSigningKeyBodyPrivateJwkOctKeyOpsItem.SIGN:
            return sign()
        if self is CreateSigningKeyBodyPrivateJwkOctKeyOpsItem.VERIFY:
            return verify()
