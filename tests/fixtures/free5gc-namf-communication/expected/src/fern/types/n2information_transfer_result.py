

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class N2InformationTransferResult(enum.StrEnum):
    N2INFO_TRANSFER_INITIATED = "N2_INFO_TRANSFER_INITIATED"

    def visit(self, n2info_transfer_initiated: typing.Callable[[], T_Result]) -> T_Result:
        if self is N2InformationTransferResult.N2INFO_TRANSFER_INITIATED:
            return n2info_transfer_initiated()
