

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AddQuoteResponseDataLinksItemType(enum.StrEnum):
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
        if self is AddQuoteResponseDataLinksItemType.GET:
            return get()
        if self is AddQuoteResponseDataLinksItemType.POST:
            return post()
        if self is AddQuoteResponseDataLinksItemType.PUT:
            return put()
        if self is AddQuoteResponseDataLinksItemType.PATCH:
            return patch()
