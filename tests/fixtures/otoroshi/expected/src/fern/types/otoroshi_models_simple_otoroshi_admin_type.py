

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OtoroshiModelsSimpleOtoroshiAdminType(enum.StrEnum):
    """
    the kind of admin
    """

    SIMPLE = "simple"
    WEBAUTHN = "webauthn"

    def visit(self, simple: typing.Callable[[], T_Result], webauthn: typing.Callable[[], T_Result]) -> T_Result:
        if self is OtoroshiModelsSimpleOtoroshiAdminType.SIMPLE:
            return simple()
        if self is OtoroshiModelsSimpleOtoroshiAdminType.WEBAUTHN:
            return webauthn()
