

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListProductsRequestStatus(enum.StrEnum):
    """
    Filter by product status. Omit for all products.
    """

    LIVE = "live"
    TEST = "test"

    def visit(self, live: typing.Callable[[], T_Result], test: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListProductsRequestStatus.LIVE:
            return live()
        if self is ListProductsRequestStatus.TEST:
            return test()
