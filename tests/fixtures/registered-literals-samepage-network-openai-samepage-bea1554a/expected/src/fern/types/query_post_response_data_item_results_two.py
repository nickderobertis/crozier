

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryPostResponseDataItemResultsTwo(enum.StrEnum):
    """
    The notebook has rejected this request for data.
    """

    REJECTED = "rejected"

    def visit(self, rejected: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryPostResponseDataItemResultsTwo.REJECTED:
            return rejected()
