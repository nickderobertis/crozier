

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RateLimitAlgorithm(enum.StrEnum):
    """
    Rate-limiting algorithm; defaults to fixed_window
    """

    FIXED_WINDOW = "fixed_window"
    TOKEN_BUCKET = "token_bucket"

    def visit(
        self, fixed_window: typing.Callable[[], T_Result], token_bucket: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is RateLimitAlgorithm.FIXED_WINDOW:
            return fixed_window()
        if self is RateLimitAlgorithm.TOKEN_BUCKET:
            return token_bucket()
