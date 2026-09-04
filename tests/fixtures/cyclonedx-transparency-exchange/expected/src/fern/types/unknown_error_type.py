

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UnknownErrorType(enum.StrEnum):
    """
    Classification of TEA error response
    """

    OBJECT_UNKNOWN = "OBJECT_UNKNOWN"
    OBJECT_NOT_SHAREABLE = "OBJECT_NOT_SHAREABLE"

    def visit(
        self, object_unknown: typing.Callable[[], T_Result], object_not_shareable: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is UnknownErrorType.OBJECT_UNKNOWN:
            return object_unknown()
        if self is UnknownErrorType.OBJECT_NOT_SHAREABLE:
            return object_not_shareable()
