

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ReviewListMineResponseItemPlayMethod(enum.StrEnum):
    NATIVE = "NATIVE"
    CROSSOVER = "CROSSOVER"
    PARALLELS = "PARALLELS"
    OTHER = "OTHER"

    def visit(
        self,
        native: typing.Callable[[], T_Result],
        crossover: typing.Callable[[], T_Result],
        parallels: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReviewListMineResponseItemPlayMethod.NATIVE:
            return native()
        if self is ReviewListMineResponseItemPlayMethod.CROSSOVER:
            return crossover()
        if self is ReviewListMineResponseItemPlayMethod.PARALLELS:
            return parallels()
        if self is ReviewListMineResponseItemPlayMethod.OTHER:
            return other()
