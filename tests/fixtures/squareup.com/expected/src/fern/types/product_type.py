

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProductType(enum.StrEnum):
    """ """

    TERMINAL_API = "TERMINAL_API"

    def visit(self, terminal_api: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProductType.TERMINAL_API:
            return terminal_api()
