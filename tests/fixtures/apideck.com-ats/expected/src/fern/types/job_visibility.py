

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobVisibility(enum.StrEnum):
    """
    The visibility of the job
    """

    PUBLIC = "public"
    INTERNAL = "internal"

    def visit(self, public: typing.Callable[[], T_Result], internal: typing.Callable[[], T_Result]) -> T_Result:
        if self is JobVisibility.PUBLIC:
            return public()
        if self is JobVisibility.INTERNAL:
            return internal()
