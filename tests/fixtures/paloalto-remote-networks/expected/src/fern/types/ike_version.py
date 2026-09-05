

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IkeVersion(enum.StrEnum):
    IKEV1 = "ikev1"
    IKEV2 = "ikev2"
    IKEV2PREFERRED = "ikev2-preferred"

    def visit(
        self,
        ikev1: typing.Callable[[], T_Result],
        ikev2: typing.Callable[[], T_Result],
        ikev2preferred: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IkeVersion.IKEV1:
            return ikev1()
        if self is IkeVersion.IKEV2:
            return ikev2()
        if self is IkeVersion.IKEV2PREFERRED:
            return ikev2preferred()
