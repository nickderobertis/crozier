

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QuoteLinksItemType(enum.StrEnum):
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
        if self is QuoteLinksItemType.GET:
            return get()
        if self is QuoteLinksItemType.POST:
            return post()
        if self is QuoteLinksItemType.PUT:
            return put()
        if self is QuoteLinksItemType.PATCH:
            return patch()
