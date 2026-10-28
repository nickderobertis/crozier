

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaginationLinkMethod(enum.StrEnum):
    GET = "GET"
    POST = "POST"

    def visit(self, get: typing.Callable[[], T_Result], post: typing.Callable[[], T_Result]) -> T_Result:
        if self is PaginationLinkMethod.GET:
            return get()
        if self is PaginationLinkMethod.POST:
            return post()
