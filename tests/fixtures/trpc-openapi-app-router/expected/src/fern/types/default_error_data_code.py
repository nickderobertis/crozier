

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DefaultErrorDataCode(enum.StrEnum):
    PARSE_ERROR = "PARSE_ERROR"
    BAD_REQUEST = "BAD_REQUEST"
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
    BAD_GATEWAY = "BAD_GATEWAY"
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"
    GATEWAY_TIMEOUT = "GATEWAY_TIMEOUT"
    UNAUTHORIZED = "UNAUTHORIZED"
    PAYMENT_REQUIRED = "PAYMENT_REQUIRED"
    FORBIDDEN = "FORBIDDEN"
    NOT_FOUND = "NOT_FOUND"
    METHOD_NOT_SUPPORTED = "METHOD_NOT_SUPPORTED"
    TIMEOUT = "TIMEOUT"
    CONFLICT = "CONFLICT"
    PRECONDITION_FAILED = "PRECONDITION_FAILED"
    PAYLOAD_TOO_LARGE = "PAYLOAD_TOO_LARGE"
    UNSUPPORTED_MEDIA_TYPE = "UNSUPPORTED_MEDIA_TYPE"
    UNPROCESSABLE_CONTENT = "UNPROCESSABLE_CONTENT"
    PRECONDITION_REQUIRED = "PRECONDITION_REQUIRED"
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"
    CLIENT_CLOSED_REQUEST = "CLIENT_CLOSED_REQUEST"

    def visit(
        self,
        parse_error: typing.Callable[[], T_Result],
        bad_request: typing.Callable[[], T_Result],
        internal_server_error: typing.Callable[[], T_Result],
        not_implemented: typing.Callable[[], T_Result],
        bad_gateway: typing.Callable[[], T_Result],
        service_unavailable: typing.Callable[[], T_Result],
        gateway_timeout: typing.Callable[[], T_Result],
        unauthorized: typing.Callable[[], T_Result],
        payment_required: typing.Callable[[], T_Result],
        forbidden: typing.Callable[[], T_Result],
        not_found: typing.Callable[[], T_Result],
        method_not_supported: typing.Callable[[], T_Result],
        timeout: typing.Callable[[], T_Result],
        conflict: typing.Callable[[], T_Result],
        precondition_failed: typing.Callable[[], T_Result],
        payload_too_large: typing.Callable[[], T_Result],
        unsupported_media_type: typing.Callable[[], T_Result],
        unprocessable_content: typing.Callable[[], T_Result],
        precondition_required: typing.Callable[[], T_Result],
        too_many_requests: typing.Callable[[], T_Result],
        client_closed_request: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DefaultErrorDataCode.PARSE_ERROR:
            return parse_error()
        if self is DefaultErrorDataCode.BAD_REQUEST:
            return bad_request()
        if self is DefaultErrorDataCode.INTERNAL_SERVER_ERROR:
            return internal_server_error()
        if self is DefaultErrorDataCode.NOT_IMPLEMENTED:
            return not_implemented()
        if self is DefaultErrorDataCode.BAD_GATEWAY:
            return bad_gateway()
        if self is DefaultErrorDataCode.SERVICE_UNAVAILABLE:
            return service_unavailable()
        if self is DefaultErrorDataCode.GATEWAY_TIMEOUT:
            return gateway_timeout()
        if self is DefaultErrorDataCode.UNAUTHORIZED:
            return unauthorized()
        if self is DefaultErrorDataCode.PAYMENT_REQUIRED:
            return payment_required()
        if self is DefaultErrorDataCode.FORBIDDEN:
            return forbidden()
        if self is DefaultErrorDataCode.NOT_FOUND:
            return not_found()
        if self is DefaultErrorDataCode.METHOD_NOT_SUPPORTED:
            return method_not_supported()
        if self is DefaultErrorDataCode.TIMEOUT:
            return timeout()
        if self is DefaultErrorDataCode.CONFLICT:
            return conflict()
        if self is DefaultErrorDataCode.PRECONDITION_FAILED:
            return precondition_failed()
        if self is DefaultErrorDataCode.PAYLOAD_TOO_LARGE:
            return payload_too_large()
        if self is DefaultErrorDataCode.UNSUPPORTED_MEDIA_TYPE:
            return unsupported_media_type()
        if self is DefaultErrorDataCode.UNPROCESSABLE_CONTENT:
            return unprocessable_content()
        if self is DefaultErrorDataCode.PRECONDITION_REQUIRED:
            return precondition_required()
        if self is DefaultErrorDataCode.TOO_MANY_REQUESTS:
            return too_many_requests()
        if self is DefaultErrorDataCode.CLIENT_CLOSED_REQUEST:
            return client_closed_request()
