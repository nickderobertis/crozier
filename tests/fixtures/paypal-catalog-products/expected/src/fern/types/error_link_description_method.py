

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ErrorLinkDescriptionMethod(enum.StrEnum):
    """
    The HTTP method required to make the related call.
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"

    def visit(
        self,
        get: typing.Callable[[], T_Result],
        post: typing.Callable[[], T_Result],
        put: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ErrorLinkDescriptionMethod.GET:
            return get()
        if self is ErrorLinkDescriptionMethod.POST:
            return post()
        if self is ErrorLinkDescriptionMethod.PUT:
            return put()
        if self is ErrorLinkDescriptionMethod.DELETE:
            return delete()
        if self is ErrorLinkDescriptionMethod.PATCH:
            return patch()
