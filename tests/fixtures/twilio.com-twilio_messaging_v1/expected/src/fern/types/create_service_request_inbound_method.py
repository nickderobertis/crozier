

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateServiceRequestInboundMethod(enum.StrEnum):
    """
    The HTTP method we should use to call `inbound_request_url`. Can be `GET` or `POST` and the default is `POST`.
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
        if self is CreateServiceRequestInboundMethod.HEAD:
            return head()
        if self is CreateServiceRequestInboundMethod.GET:
            return get()
        if self is CreateServiceRequestInboundMethod.POST:
            return post()
        if self is CreateServiceRequestInboundMethod.PATCH:
            return patch()
        if self is CreateServiceRequestInboundMethod.PUT:
            return put()
        if self is CreateServiceRequestInboundMethod.DELETE:
            return delete()
