

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ContractsApiGetContractsRequestType(enum.StrEnum):
    WIPE = "WIPE"
    RETIRE = "RETIRE"

    def visit(self, wipe: typing.Callable[[], T_Result], retire: typing.Callable[[], T_Result]) -> T_Result:
        if self is ContractsApiGetContractsRequestType.WIPE:
            return wipe()
        if self is ContractsApiGetContractsRequestType.RETIRE:
            return retire()
