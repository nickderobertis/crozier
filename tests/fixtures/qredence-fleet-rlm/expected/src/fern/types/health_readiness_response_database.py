

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthReadinessResponseDatabase(enum.StrEnum):
    OK = "ok"
    NOT_CONFIGURED = "not_configured"

    def visit(self, ok: typing.Callable[[], T_Result], not_configured: typing.Callable[[], T_Result]) -> T_Result:
        if self is HealthReadinessResponseDatabase.OK:
            return ok()
        if self is HealthReadinessResponseDatabase.NOT_CONFIGURED:
            return not_configured()
