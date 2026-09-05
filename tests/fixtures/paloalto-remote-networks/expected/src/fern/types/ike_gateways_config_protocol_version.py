

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IkeGatewaysConfigProtocolVersion(enum.StrEnum):
    IKEV2PREFERRED = "ikev2-preferred"
    IKEV1 = "ikev1"
    IKEV2 = "ikev2"

    def visit(
        self,
        ikev2preferred: typing.Callable[[], T_Result],
        ikev1: typing.Callable[[], T_Result],
        ikev2: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IkeGatewaysConfigProtocolVersion.IKEV2PREFERRED:
            return ikev2preferred()
        if self is IkeGatewaysConfigProtocolVersion.IKEV1:
            return ikev1()
        if self is IkeGatewaysConfigProtocolVersion.IKEV2:
            return ikev2()
