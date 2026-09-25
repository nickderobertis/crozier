

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProductStatus(enum.StrEnum):
    LIVE = "live"
    TEST = "test"

    def visit(self, live: typing.Callable[[], T_Result], test: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProductStatus.LIVE:
            return live()
        if self is ProductStatus.TEST:
            return test()
