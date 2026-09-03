

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MethodNotAllowedErrorBodyError(enum.StrEnum):
    """
    Error code, available in error response.
    """

    METHOD_NOT_ALLOWED = "method_not_allowed"

    def visit(self, method_not_allowed: typing.Callable[[], T_Result]) -> T_Result:
        if self is MethodNotAllowedErrorBodyError.METHOD_NOT_ALLOWED:
            return method_not_allowed()
