

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IntegrityAlgorithm(enum.StrEnum):
    NIA0 = "NIA0"
    NIA1 = "NIA1"
    NIA2 = "NIA2"
    NIA3 = "NIA3"

    def visit(
        self,
        nia0: typing.Callable[[], T_Result],
        nia1: typing.Callable[[], T_Result],
        nia2: typing.Callable[[], T_Result],
        nia3: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IntegrityAlgorithm.NIA0:
            return nia0()
        if self is IntegrityAlgorithm.NIA1:
            return nia1()
        if self is IntegrityAlgorithm.NIA2:
            return nia2()
        if self is IntegrityAlgorithm.NIA3:
            return nia3()
