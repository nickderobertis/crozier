

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntryPointHttpMethod(enum.StrEnum):
    """
    The HTTP method used by the EntryPoint.
    """

    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    DELETE = "DELETE"

    def visit(
        self,
        get: typing.Callable[[], T_Result],
        put: typing.Callable[[], T_Result],
        post: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntryPointHttpMethod.GET:
            return get()
        if self is EntryPointHttpMethod.PUT:
            return put()
        if self is EntryPointHttpMethod.POST:
            return post()
        if self is EntryPointHttpMethod.DELETE:
            return delete()
