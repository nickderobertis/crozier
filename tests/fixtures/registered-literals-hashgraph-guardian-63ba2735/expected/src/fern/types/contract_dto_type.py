

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContractDtoType(enum.StrEnum):
    WIPE = "WIPE"
    RETIRE = "RETIRE"

    def visit(self, wipe: typing.Callable[[], T_Result], retire: typing.Callable[[], T_Result]) -> T_Result:
        if self is ContractDtoType.WIPE:
            return wipe()
        if self is ContractDtoType.RETIRE:
            return retire()
