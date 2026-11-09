

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FdxHateoasLinkAction(enum.StrEnum):
    """
    HTTP Method to use for the request
    """

    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
    DELETE = "DELETE"
    PUT = "PUT"

    def visit(
        self,
        get: typing.Callable[[], T_Result],
        post: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        put: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FdxHateoasLinkAction.GET:
            return get()
        if self is FdxHateoasLinkAction.POST:
            return post()
        if self is FdxHateoasLinkAction.PATCH:
            return patch()
        if self is FdxHateoasLinkAction.DELETE:
            return delete()
        if self is FdxHateoasLinkAction.PUT:
            return put()
