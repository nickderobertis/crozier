

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PagePostResponseDataOne(enum.StrEnum):
    """
    We are still waiting for the notebook to respond to this request for data.
    """

    PENDING = "pending"

    def visit(self, pending: typing.Callable[[], T_Result]) -> T_Result:
        if self is PagePostResponseDataOne.PENDING:
            return pending()
