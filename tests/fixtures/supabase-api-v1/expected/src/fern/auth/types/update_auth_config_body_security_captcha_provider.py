

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateAuthConfigBodySecurityCaptchaProvider(enum.StrEnum):
    TURNSTILE = "turnstile"
    HCAPTCHA = "hcaptcha"

    def visit(self, turnstile: typing.Callable[[], T_Result], hcaptcha: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateAuthConfigBodySecurityCaptchaProvider.TURNSTILE:
            return turnstile()
        if self is UpdateAuthConfigBodySecurityCaptchaProvider.HCAPTCHA:
            return hcaptcha()
