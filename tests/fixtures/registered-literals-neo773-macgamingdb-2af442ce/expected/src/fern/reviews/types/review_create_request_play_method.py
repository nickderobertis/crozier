

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ReviewCreateRequestPlayMethod(enum.StrEnum):
    NATIVE = "NATIVE"
    CROSSOVER = "CROSSOVER"
    PARALLELS = "PARALLELS"

    def visit(
        self,
        native: typing.Callable[[], T_Result],
        crossover: typing.Callable[[], T_Result],
        parallels: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReviewCreateRequestPlayMethod.NATIVE:
            return native()
        if self is ReviewCreateRequestPlayMethod.CROSSOVER:
            return crossover()
        if self is ReviewCreateRequestPlayMethod.PARALLELS:
            return parallels()
