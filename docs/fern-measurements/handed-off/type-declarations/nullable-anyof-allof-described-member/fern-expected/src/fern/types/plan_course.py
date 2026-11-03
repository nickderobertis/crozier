

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlanCourse(enum.StrEnum):
    """
    The planned course.
    """

    STARTER = "starter"
    MAIN = "main"
    DESSERT = "dessert"

    def visit(
        self,
        starter: typing.Callable[[], T_Result],
        main: typing.Callable[[], T_Result],
        dessert: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlanCourse.STARTER:
            return starter()
        if self is PlanCourse.MAIN:
            return main()
        if self is PlanCourse.DESSERT:
            return dessert()
