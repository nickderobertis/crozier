

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OtoroshiModelsGlobalJwtVerifierType(enum.StrEnum):
    """
    the kind of verifier
    """

    GLOBAL = "global"

    def visit(self, global_: typing.Callable[[], T_Result]) -> T_Result:
        if self is OtoroshiModelsGlobalJwtVerifierType.GLOBAL:
            return global_()
