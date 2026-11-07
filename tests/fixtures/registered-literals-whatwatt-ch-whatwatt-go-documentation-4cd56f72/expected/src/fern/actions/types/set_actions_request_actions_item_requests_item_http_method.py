

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SetActionsRequestActionsItemRequestsItemHttpMethod(enum.StrEnum):
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
        if self is SetActionsRequestActionsItemRequestsItemHttpMethod.GET:
            return get()
        if self is SetActionsRequestActionsItemRequestsItemHttpMethod.POST:
            return post()
        if self is SetActionsRequestActionsItemRequestsItemHttpMethod.PUT:
            return put()
        if self is SetActionsRequestActionsItemRequestsItemHttpMethod.DELETE:
            return delete()
