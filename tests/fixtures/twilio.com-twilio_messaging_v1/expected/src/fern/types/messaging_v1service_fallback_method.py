

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessagingV1ServiceFallbackMethod(enum.StrEnum):
    """
    The HTTP method we use to call `fallback_url`. Can be: `GET` or `POST`.
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
        if self is MessagingV1ServiceFallbackMethod.HEAD:
            return head()
        if self is MessagingV1ServiceFallbackMethod.GET:
            return get()
        if self is MessagingV1ServiceFallbackMethod.POST:
            return post()
        if self is MessagingV1ServiceFallbackMethod.PATCH:
            return patch()
        if self is MessagingV1ServiceFallbackMethod.PUT:
            return put()
        if self is MessagingV1ServiceFallbackMethod.DELETE:
            return delete()
