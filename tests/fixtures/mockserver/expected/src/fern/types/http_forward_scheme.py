

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HttpForwardScheme(enum.StrEnum):
    HTTP = "HTTP"
    HTTPS = "HTTPS"

    def visit(self, http: typing.Callable[[], T_Result], https: typing.Callable[[], T_Result]) -> T_Result:
        if self is HttpForwardScheme.HTTP:
            return http()
        if self is HttpForwardScheme.HTTPS:
            return https()
