

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ProductType(str, enum.Enum):
    """ """

    TERMINAL_API = "TERMINAL_API"

    def visit(self, terminal_api: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProductType.TERMINAL_API:
            return terminal_api()
