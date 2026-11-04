

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ContributorGetByIdResponseReviewsItemPlayMethod(enum.StrEnum):
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
        if self is ContributorGetByIdResponseReviewsItemPlayMethod.NATIVE:
            return native()
        if self is ContributorGetByIdResponseReviewsItemPlayMethod.CROSSOVER:
            return crossover()
        if self is ContributorGetByIdResponseReviewsItemPlayMethod.PARALLELS:
            return parallels()
        if self is ContributorGetByIdResponseReviewsItemPlayMethod.OTHER:
            return other()
