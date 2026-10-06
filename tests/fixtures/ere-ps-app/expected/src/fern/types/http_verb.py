

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HttpVerb(enum.StrEnum):
    GET = "GET"
    HEAD = "HEAD"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    NULL = "NULL"

    def visit(
        self,
        get: typing.Callable[[], T_Result],
        head: typing.Callable[[], T_Result],
        post: typing.Callable[[], T_Result],
        put: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        null: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HttpVerb.GET:
            return get()
        if self is HttpVerb.HEAD:
            return head()
        if self is HttpVerb.POST:
            return post()
        if self is HttpVerb.PUT:
            return put()
        if self is HttpVerb.DELETE:
            return delete()
        if self is HttpVerb.PATCH:
            return patch()
        if self is HttpVerb.NULL:
            return null()
