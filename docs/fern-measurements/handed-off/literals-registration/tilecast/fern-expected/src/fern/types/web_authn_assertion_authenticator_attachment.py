

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebAuthnAssertionAuthenticatorAttachment(enum.StrEnum):
    PLATFORM = "platform"
    CROSS_PLATFORM = "cross-platform"

    def visit(self, platform: typing.Callable[[], T_Result], cross_platform: typing.Callable[[], T_Result]) -> T_Result:
        if self is WebAuthnAssertionAuthenticatorAttachment.PLATFORM:
            return platform()
        if self is WebAuthnAssertionAuthenticatorAttachment.CROSS_PLATFORM:
            return cross_platform()
