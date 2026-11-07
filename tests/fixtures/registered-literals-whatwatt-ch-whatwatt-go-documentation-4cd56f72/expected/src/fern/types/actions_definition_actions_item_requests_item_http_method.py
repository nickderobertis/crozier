

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActionsDefinitionActionsItemRequestsItemHttpMethod(enum.StrEnum):
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
        if self is ActionsDefinitionActionsItemRequestsItemHttpMethod.GET:
            return get()
        if self is ActionsDefinitionActionsItemRequestsItemHttpMethod.POST:
            return post()
        if self is ActionsDefinitionActionsItemRequestsItemHttpMethod.PUT:
            return put()
        if self is ActionsDefinitionActionsItemRequestsItemHttpMethod.DELETE:
            return delete()
