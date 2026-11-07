

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Extensions(enum.StrEnum):
    AD_BLOCKER = "ad-blocker"
    CAPTCHA_SOLVER = "captcha-solver"

    def visit(
        self, ad_blocker: typing.Callable[[], T_Result], captcha_solver: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is Extensions.AD_BLOCKER:
            return ad_blocker()
        if self is Extensions.CAPTCHA_SOLVER:
            return captcha_solver()
