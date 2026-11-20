

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PagesRequestResponsePageOne(enum.StrEnum):
    """
    The notebook has not answered yet.
    """

    PENDING = "pending"

    def visit(self, pending: typing.Callable[[], T_Result]) -> T_Result:
        if self is PagesRequestResponsePageOne.PENDING:
            return pending()
