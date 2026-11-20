

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PagePostResponseDataTwo(enum.StrEnum):
    """
    The notebook has rejected this request for data.
    """

    REJECTED = "rejected"

    def visit(self, rejected: typing.Callable[[], T_Result]) -> T_Result:
        if self is PagePostResponseDataTwo.REJECTED:
            return rejected()
