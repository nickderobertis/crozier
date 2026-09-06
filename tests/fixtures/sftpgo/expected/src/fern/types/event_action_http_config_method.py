

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventActionHttpConfigMethod(enum.StrEnum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

    def visit(
        self,
        get: typing.Callable[[], T_Result],
        post: typing.Callable[[], T_Result],
        put: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EventActionHttpConfigMethod.GET:
            return get()
        if self is EventActionHttpConfigMethod.POST:
            return post()
        if self is EventActionHttpConfigMethod.PUT:
            return put()
        if self is EventActionHttpConfigMethod.DELETE:
            return delete()
