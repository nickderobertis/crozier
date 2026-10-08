

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TurnstileReason(enum.StrEnum):
    EXPIRED = "expired"
    WRONG_LIFT = "wrong_lift"
    OK = "ok"

    def visit(
        self,
        expired: typing.Callable[[], T_Result],
        wrong_lift: typing.Callable[[], T_Result],
        ok: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TurnstileReason.EXPIRED:
            return expired()
        if self is TurnstileReason.WRONG_LIFT:
            return wrong_lift()
        if self is TurnstileReason.OK:
            return ok()
