

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OpenapiValidationErrorsTarget(enum.StrEnum):
    REQUEST_BODY = "requestBody"
    QUERY = "query"
    HEADERS = "headers"
    RESPONSE_BODY = "responseBody"

    def visit(
        self,
        request_body: typing.Callable[[], T_Result],
        query: typing.Callable[[], T_Result],
        headers: typing.Callable[[], T_Result],
        response_body: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OpenapiValidationErrorsTarget.REQUEST_BODY:
            return request_body()
        if self is OpenapiValidationErrorsTarget.QUERY:
            return query()
        if self is OpenapiValidationErrorsTarget.HEADERS:
            return headers()
        if self is OpenapiValidationErrorsTarget.RESPONSE_BODY:
            return response_body()
