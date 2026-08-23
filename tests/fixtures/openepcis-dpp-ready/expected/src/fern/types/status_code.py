

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StatusCode(enum.StrEnum):
    """
    Generic status code (EN 18222 Table 15).
    """

    SUCCESS = "Success"
    SUCCESS_CREATED = "SuccessCreated"
    SUCCESS_ACCEPTED = "SuccessAccepted"
    SUCCESS_NO_CONTENT = "SuccessNoContent"
    CLIENT_ERROR_BAD_REQUEST = "ClientErrorBadRequest"
    CLIENT_NOT_AUTHORIZED = "ClientNotAuthorized"
    CLIENT_FORBIDDEN = "ClientForbidden"
    CLIENT_METHOD_NOT_ALLOWED = "ClientMethodNotAllowed"
    CLIENT_ERROR_RESOURCE_NOT_FOUND = "ClientErrorResourceNotFound"
    CLIENT_RESOURCE_CONFLICT = "ClientResourceConflict"
    SERVER_INTERNAL_ERROR = "ServerInternalError"
    SERVER_NOT_IMPLEMENTED = "ServerNotImplemented"
    SERVER_ERROR_BAD_GATEWAY = "ServerErrorBadGateway"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        success_created: typing.Callable[[], T_Result],
        success_accepted: typing.Callable[[], T_Result],
        success_no_content: typing.Callable[[], T_Result],
        client_error_bad_request: typing.Callable[[], T_Result],
        client_not_authorized: typing.Callable[[], T_Result],
        client_forbidden: typing.Callable[[], T_Result],
        client_method_not_allowed: typing.Callable[[], T_Result],
        client_error_resource_not_found: typing.Callable[[], T_Result],
        client_resource_conflict: typing.Callable[[], T_Result],
        server_internal_error: typing.Callable[[], T_Result],
        server_not_implemented: typing.Callable[[], T_Result],
        server_error_bad_gateway: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StatusCode.SUCCESS:
            return success()
        if self is StatusCode.SUCCESS_CREATED:
            return success_created()
        if self is StatusCode.SUCCESS_ACCEPTED:
            return success_accepted()
        if self is StatusCode.SUCCESS_NO_CONTENT:
            return success_no_content()
        if self is StatusCode.CLIENT_ERROR_BAD_REQUEST:
            return client_error_bad_request()
        if self is StatusCode.CLIENT_NOT_AUTHORIZED:
            return client_not_authorized()
        if self is StatusCode.CLIENT_FORBIDDEN:
            return client_forbidden()
        if self is StatusCode.CLIENT_METHOD_NOT_ALLOWED:
            return client_method_not_allowed()
        if self is StatusCode.CLIENT_ERROR_RESOURCE_NOT_FOUND:
            return client_error_resource_not_found()
        if self is StatusCode.CLIENT_RESOURCE_CONFLICT:
            return client_resource_conflict()
        if self is StatusCode.SERVER_INTERNAL_ERROR:
            return server_internal_error()
        if self is StatusCode.SERVER_NOT_IMPLEMENTED:
            return server_not_implemented()
        if self is StatusCode.SERVER_ERROR_BAD_GATEWAY:
            return server_error_bad_gateway()
