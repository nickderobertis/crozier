

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EndpointMetadataQueryReferenceMethodsItem(enum.StrEnum):
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
        if self is EndpointMetadataQueryReferenceMethodsItem.GET:
            return get()
        if self is EndpointMetadataQueryReferenceMethodsItem.POST:
            return post()
        if self is EndpointMetadataQueryReferenceMethodsItem.PUT:
            return put()
        if self is EndpointMetadataQueryReferenceMethodsItem.DELETE:
            return delete()
        if self is EndpointMetadataQueryReferenceMethodsItem.PATCH:
            return patch()
