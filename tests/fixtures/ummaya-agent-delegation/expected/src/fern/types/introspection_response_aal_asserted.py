

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IntrospectionResponseAalAsserted(enum.StrEnum):
    AAL1 = "AAL1"
    AAL2 = "AAL2"
    AAL3 = "AAL3"

    def visit(
        self,
        aal1: typing.Callable[[], T_Result],
        aal2: typing.Callable[[], T_Result],
        aal3: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IntrospectionResponseAalAsserted.AAL1:
            return aal1()
        if self is IntrospectionResponseAalAsserted.AAL2:
            return aal2()
        if self is IntrospectionResponseAalAsserted.AAL3:
            return aal3()
