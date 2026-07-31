

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessagingV1ServiceInboundMethod(enum.StrEnum):
    """
    The HTTP method we use to call `inbound_request_url`. Can be `GET` or `POST`.
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
        if self is MessagingV1ServiceInboundMethod.HEAD:
            return head()
        if self is MessagingV1ServiceInboundMethod.GET:
            return get()
        if self is MessagingV1ServiceInboundMethod.POST:
            return post()
        if self is MessagingV1ServiceInboundMethod.PATCH:
            return patch()
        if self is MessagingV1ServiceInboundMethod.PUT:
            return put()
        if self is MessagingV1ServiceInboundMethod.DELETE:
            return delete()
