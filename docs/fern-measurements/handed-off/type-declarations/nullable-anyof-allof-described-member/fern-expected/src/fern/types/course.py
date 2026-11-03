

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Course(enum.StrEnum):
    STARTER = "starter"
    MAIN = "main"
    DESSERT = "dessert"

    def visit(
        self,
        starter: typing.Callable[[], T_Result],
        main: typing.Callable[[], T_Result],
        dessert: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Course.STARTER:
            return starter()
        if self is Course.MAIN:
            return main()
        if self is Course.DESSERT:
            return dessert()
