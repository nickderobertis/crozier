

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GameGetFilterCountsRequestPlayMethod(enum.StrEnum):
    ALL = "ALL"
    NATIVE = "NATIVE"
    CROSSOVER = "CROSSOVER"
    PARALLELS = "PARALLELS"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        native: typing.Callable[[], T_Result],
        crossover: typing.Callable[[], T_Result],
        parallels: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GameGetFilterCountsRequestPlayMethod.ALL:
            return all_()
        if self is GameGetFilterCountsRequestPlayMethod.NATIVE:
            return native()
        if self is GameGetFilterCountsRequestPlayMethod.CROSSOVER:
            return crossover()
        if self is GameGetFilterCountsRequestPlayMethod.PARALLELS:
            return parallels()
