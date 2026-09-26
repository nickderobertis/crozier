

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApiErrorName(enum.StrEnum):
    API_ERROR = "APIError"

    def visit(self, api_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApiErrorName.API_ERROR:
            return api_error()
