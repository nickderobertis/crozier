

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinksType(enum.StrEnum):
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
        if self is LinksType.GET:
            return get()
        if self is LinksType.POST:
            return post()
        if self is LinksType.PUT:
            return put()
        if self is LinksType.PATCH:
            return patch()
