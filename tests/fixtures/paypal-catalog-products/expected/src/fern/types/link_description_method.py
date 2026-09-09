

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinkDescriptionMethod(enum.StrEnum):
    """
    The HTTP method required to make the related call.
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    HEAD = "HEAD"
    CONNECT = "CONNECT"
    OPTIONS = "OPTIONS"
    PATCH = "PATCH"

    def visit(
        self,
        get: typing.Callable[[], T_Result],
        post: typing.Callable[[], T_Result],
        put: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        head: typing.Callable[[], T_Result],
        connect: typing.Callable[[], T_Result],
        options: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LinkDescriptionMethod.GET:
            return get()
        if self is LinkDescriptionMethod.POST:
            return post()
        if self is LinkDescriptionMethod.PUT:
            return put()
        if self is LinkDescriptionMethod.DELETE:
            return delete()
        if self is LinkDescriptionMethod.HEAD:
            return head()
        if self is LinkDescriptionMethod.CONNECT:
            return connect()
        if self is LinkDescriptionMethod.OPTIONS:
            return options()
        if self is LinkDescriptionMethod.PATCH:
            return patch()
