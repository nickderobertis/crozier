

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApplicationType(enum.StrEnum):
    """
    The data type
    """

    NPQ_APPLICATION = "npq_application"

    def visit(self, npq_application: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApplicationType.NPQ_APPLICATION:
            return npq_application()
