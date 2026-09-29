

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ValidateInputInputWebhookType(enum.StrEnum):
    HTTP = "http"

    def visit(self, http: typing.Callable[[], T_Result]) -> T_Result:
        if self is ValidateInputInputWebhookType.HTTP:
            return http()
