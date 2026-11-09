

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class VerifyBundleV2ResponseResolvedTier(enum.StrEnum):
    ROUTINE = "routine"
    STANDARD = "standard"
    ELEVATED = "elevated"
    MAXIMUM = "maximum"

    def visit(
        self,
        routine: typing.Callable[[], T_Result],
        standard: typing.Callable[[], T_Result],
        elevated: typing.Callable[[], T_Result],
        maximum: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VerifyBundleV2ResponseResolvedTier.ROUTINE:
            return routine()
        if self is VerifyBundleV2ResponseResolvedTier.STANDARD:
            return standard()
        if self is VerifyBundleV2ResponseResolvedTier.ELEVATED:
            return elevated()
        if self is VerifyBundleV2ResponseResolvedTier.MAXIMUM:
            return maximum()
