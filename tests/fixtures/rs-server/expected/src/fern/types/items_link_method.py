

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ItemsLinkMethod(enum.StrEnum):
    GET = "GET"
    POST = "POST"

    def visit(self, get: typing.Callable[[], T_Result], post: typing.Callable[[], T_Result]) -> T_Result:
        if self is ItemsLinkMethod.GET:
            return get()
        if self is ItemsLinkMethod.POST:
            return post()
