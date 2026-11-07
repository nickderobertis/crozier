

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GameGetByIdResponseReviewsItemPlayMethod(enum.StrEnum):
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
        if self is GameGetByIdResponseReviewsItemPlayMethod.NATIVE:
            return native()
        if self is GameGetByIdResponseReviewsItemPlayMethod.CROSSOVER:
            return crossover()
        if self is GameGetByIdResponseReviewsItemPlayMethod.PARALLELS:
            return parallels()
        if self is GameGetByIdResponseReviewsItemPlayMethod.OTHER:
            return other()
