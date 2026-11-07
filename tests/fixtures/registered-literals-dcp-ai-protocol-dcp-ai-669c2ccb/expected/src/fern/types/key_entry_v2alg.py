

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KeyEntryV2Alg(enum.StrEnum):
    ED25519 = "ed25519"
    ML_DSA65 = "ml-dsa-65"
    SLH_DSA192F = "slh-dsa-192f"

    def visit(
        self,
        ed25519: typing.Callable[[], T_Result],
        ml_dsa65: typing.Callable[[], T_Result],
        slh_dsa192f: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is KeyEntryV2Alg.ED25519:
            return ed25519()
        if self is KeyEntryV2Alg.ML_DSA65:
            return ml_dsa65()
        if self is KeyEntryV2Alg.SLH_DSA192F:
            return slh_dsa192f()
