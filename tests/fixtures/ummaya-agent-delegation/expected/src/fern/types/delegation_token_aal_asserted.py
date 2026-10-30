

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DelegationTokenAalAsserted(enum.StrEnum):
    AAL1 = "AAL1"
    AAL2 = "AAL2"
    AAL3 = "AAL3"

    def visit(
        self,
        aal1: typing.Callable[[], T_Result],
        aal2: typing.Callable[[], T_Result],
        aal3: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DelegationTokenAalAsserted.AAL1:
            return aal1()
        if self is DelegationTokenAalAsserted.AAL2:
            return aal2()
        if self is DelegationTokenAalAsserted.AAL3:
            return aal3()
