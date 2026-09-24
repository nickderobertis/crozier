

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateQuoteResponseDataLinksItemType(enum.StrEnum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"

    def visit(
        self,
        get: typing.Callable[[], T_Result],
        post: typing.Callable[[], T_Result],
        put: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateQuoteResponseDataLinksItemType.GET:
            return get()
        if self is UpdateQuoteResponseDataLinksItemType.POST:
            return post()
        if self is UpdateQuoteResponseDataLinksItemType.PUT:
            return put()
        if self is UpdateQuoteResponseDataLinksItemType.PATCH:
            return patch()
