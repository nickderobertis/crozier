

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WebhookHttpMethod(str, enum.Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"

    def visit(
        self,
        get: typing.Callable[[], T_Result],
        post: typing.Callable[[], T_Result],
        put: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebhookHttpMethod.GET:
            return get()
        if self is WebhookHttpMethod.POST:
            return post()
        if self is WebhookHttpMethod.PUT:
            return put()
        if self is WebhookHttpMethod.PATCH:
            return patch()
        if self is WebhookHttpMethod.DELETE:
            return delete()
