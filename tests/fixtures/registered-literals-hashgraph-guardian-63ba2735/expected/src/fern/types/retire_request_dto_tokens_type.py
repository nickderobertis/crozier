

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RetireRequestDtoTokensType(enum.StrEnum):
    NON_FUNGIBLE = "non-fungible"
    FUNGIBLE = "fungible"

    def visit(self, non_fungible: typing.Callable[[], T_Result], fungible: typing.Callable[[], T_Result]) -> T_Result:
        if self is RetireRequestDtoTokensType.NON_FUNGIBLE:
            return non_fungible()
        if self is RetireRequestDtoTokensType.FUNGIBLE:
            return fungible()
