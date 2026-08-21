

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Method(enum.StrEnum):
    GET = "GET"
    HEAD = "HEAD"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"
    DELETE = "DELETE"

    def visit(
        self,
        get: typing.Callable[[], T_Result],
        head: typing.Callable[[], T_Result],
        post: typing.Callable[[], T_Result],
        put: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        options: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Method.GET:
            return get()
        if self is Method.HEAD:
            return head()
        if self is Method.POST:
            return post()
        if self is Method.PUT:
            return put()
        if self is Method.PATCH:
            return patch()
        if self is Method.OPTIONS:
            return options()
        if self is Method.DELETE:
            return delete()
