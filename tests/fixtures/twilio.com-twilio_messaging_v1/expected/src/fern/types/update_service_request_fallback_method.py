

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateServiceRequestFallbackMethod(enum.StrEnum):
    """
    The HTTP method we should use to call `fallback_url`. Can be: `GET` or `POST`.
    """

    HEAD = "HEAD"
    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
    PUT = "PUT"
    DELETE = "DELETE"

    def visit(
        self,
        head: typing.Callable[[], T_Result],
        get: typing.Callable[[], T_Result],
        post: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        put: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateServiceRequestFallbackMethod.HEAD:
            return head()
        if self is UpdateServiceRequestFallbackMethod.GET:
            return get()
        if self is UpdateServiceRequestFallbackMethod.POST:
            return post()
        if self is UpdateServiceRequestFallbackMethod.PATCH:
            return patch()
        if self is UpdateServiceRequestFallbackMethod.PUT:
            return put()
        if self is UpdateServiceRequestFallbackMethod.DELETE:
            return delete()
