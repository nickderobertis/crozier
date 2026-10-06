

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HalLinkMethod(enum.StrEnum):
    """
    An http method that can be specified in a HAL link.
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
        if self is HalLinkMethod.GET:
            return get()
        if self is HalLinkMethod.POST:
            return post()
        if self is HalLinkMethod.PUT:
            return put()
        if self is HalLinkMethod.DELETE:
            return delete()
        if self is HalLinkMethod.PATCH:
            return patch()
