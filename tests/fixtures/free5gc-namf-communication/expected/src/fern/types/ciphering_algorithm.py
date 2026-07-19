

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CipheringAlgorithm(enum.StrEnum):
    NEA0 = "NEA0"
    NEA1 = "NEA1"
    NEA2 = "NEA2"
    NEA3 = "NEA3"

    def visit(
        self,
        nea0: typing.Callable[[], T_Result],
        nea1: typing.Callable[[], T_Result],
        nea2: typing.Callable[[], T_Result],
        nea3: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CipheringAlgorithm.NEA0:
            return nea0()
        if self is CipheringAlgorithm.NEA1:
            return nea1()
        if self is CipheringAlgorithm.NEA2:
            return nea2()
        if self is CipheringAlgorithm.NEA3:
            return nea3()
