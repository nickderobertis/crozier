

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertStateValue(enum.StrEnum):
    OK = "OK"
    PENDING = "PENDING"
    FIRING = "FIRING"

    def visit(
        self,
        ok: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        firing: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AlertStateValue.OK:
            return ok()
        if self is AlertStateValue.PENDING:
            return pending()
        if self is AlertStateValue.FIRING:
            return firing()
