

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BrandRegistrationsEnumIdentityStatus(enum.StrEnum):
    SELF_DECLARED = "SELF_DECLARED"
    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"
    VETTED_VERIFIED = "VETTED_VERIFIED"

    def visit(
        self,
        self_declared: typing.Callable[[], T_Result],
        unverified: typing.Callable[[], T_Result],
        verified: typing.Callable[[], T_Result],
        vetted_verified: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BrandRegistrationsEnumIdentityStatus.SELF_DECLARED:
            return self_declared()
        if self is BrandRegistrationsEnumIdentityStatus.UNVERIFIED:
            return unverified()
        if self is BrandRegistrationsEnumIdentityStatus.VERIFIED:
            return verified()
        if self is BrandRegistrationsEnumIdentityStatus.VETTED_VERIFIED:
            return vetted_verified()
