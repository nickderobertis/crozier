

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectTypeApi(enum.StrEnum):
    ALL = "all"
    TEMPLATE = "template"
    USER = "user"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        template: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProjectTypeApi.ALL:
            return all_()
        if self is ProjectTypeApi.TEMPLATE:
            return template()
        if self is ProjectTypeApi.USER:
            return user()
