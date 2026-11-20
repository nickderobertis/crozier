

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PagesRequestResponsePageTwo(enum.StrEnum):
    """
    The notebook declined the request.
    """

    REJECTED = "rejected"

    def visit(self, rejected: typing.Callable[[], T_Result]) -> T_Result:
        if self is PagesRequestResponsePageTwo.REJECTED:
            return rejected()
