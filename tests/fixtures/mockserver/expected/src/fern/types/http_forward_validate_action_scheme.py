

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HttpForwardValidateActionScheme(enum.StrEnum):
    HTTP = "HTTP"
    HTTPS = "HTTPS"

    def visit(self, http: typing.Callable[[], T_Result], https: typing.Callable[[], T_Result]) -> T_Result:
        if self is HttpForwardValidateActionScheme.HTTP:
            return http()
        if self is HttpForwardValidateActionScheme.HTTPS:
            return https()
