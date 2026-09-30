

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchRequestInfluenceClassItem(enum.StrEnum):
    C1 = "C1"
    C2 = "C2"
    C3 = "C3"
    C4 = "C4"
    C5 = "C5"

    def visit(
        self,
        c1: typing.Callable[[], T_Result],
        c2: typing.Callable[[], T_Result],
        c3: typing.Callable[[], T_Result],
        c4: typing.Callable[[], T_Result],
        c5: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchRequestInfluenceClassItem.C1:
            return c1()
        if self is SearchRequestInfluenceClassItem.C2:
            return c2()
        if self is SearchRequestInfluenceClassItem.C3:
            return c3()
        if self is SearchRequestInfluenceClassItem.C4:
            return c4()
        if self is SearchRequestInfluenceClassItem.C5:
            return c5()
