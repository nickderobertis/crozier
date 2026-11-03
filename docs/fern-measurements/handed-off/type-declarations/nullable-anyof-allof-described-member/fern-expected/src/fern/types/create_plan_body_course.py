

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreatePlanBodyCourse(enum.StrEnum):
    """
    Which course to plan, if any.
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
        if self is CreatePlanBodyCourse.STARTER:
            return starter()
        if self is CreatePlanBodyCourse.MAIN:
            return main()
        if self is CreatePlanBodyCourse.DESSERT:
            return dessert()
