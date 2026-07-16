

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetRecordHandlerProgressRequestErrorCode(str, enum.Enum):
    NOT_UPDATABLE = "NotUpdatable"
    INVALID_REQUEST = "InvalidRequest"
    ACCESS_DENIED = "AccessDenied"
    INVALID_CREDENTIALS = "InvalidCredentials"
    ALREADY_EXISTS = "AlreadyExists"
    NOT_FOUND = "NotFound"
    RESOURCE_CONFLICT = "ResourceConflict"
    THROTTLING = "Throttling"
    SERVICE_LIMIT_EXCEEDED = "ServiceLimitExceeded"
    NOT_STABILIZED = "NotStabilized"
    GENERAL_SERVICE_EXCEPTION = "GeneralServiceException"
    SERVICE_INTERNAL_ERROR = "ServiceInternalError"
    NETWORK_FAILURE = "NetworkFailure"
    INTERNAL_FAILURE = "InternalFailure"
    INVALID_TYPE_CONFIGURATION = "InvalidTypeConfiguration"
    HANDLER_INTERNAL_FAILURE = "HandlerInternalFailure"
    NON_COMPLIANT = "NonCompliant"
    UNKNOWN = "Unknown"
    UNSUPPORTED_TARGET = "UnsupportedTarget"

    def visit(
        self,
        not_updatable: typing.Callable[[], T_Result],
        invalid_request: typing.Callable[[], T_Result],
        access_denied: typing.Callable[[], T_Result],
        invalid_credentials: typing.Callable[[], T_Result],
        already_exists: typing.Callable[[], T_Result],
        not_found: typing.Callable[[], T_Result],
        resource_conflict: typing.Callable[[], T_Result],
        throttling: typing.Callable[[], T_Result],
        service_limit_exceeded: typing.Callable[[], T_Result],
        not_stabilized: typing.Callable[[], T_Result],
        general_service_exception: typing.Callable[[], T_Result],
        service_internal_error: typing.Callable[[], T_Result],
        network_failure: typing.Callable[[], T_Result],
        internal_failure: typing.Callable[[], T_Result],
        invalid_type_configuration: typing.Callable[[], T_Result],
        handler_internal_failure: typing.Callable[[], T_Result],
        non_compliant: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        unsupported_target: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetRecordHandlerProgressRequestErrorCode.NOT_UPDATABLE:
            return not_updatable()
        if self is GetRecordHandlerProgressRequestErrorCode.INVALID_REQUEST:
            return invalid_request()
        if self is GetRecordHandlerProgressRequestErrorCode.ACCESS_DENIED:
            return access_denied()
        if self is GetRecordHandlerProgressRequestErrorCode.INVALID_CREDENTIALS:
            return invalid_credentials()
        if self is GetRecordHandlerProgressRequestErrorCode.ALREADY_EXISTS:
            return already_exists()
        if self is GetRecordHandlerProgressRequestErrorCode.NOT_FOUND:
            return not_found()
        if self is GetRecordHandlerProgressRequestErrorCode.RESOURCE_CONFLICT:
            return resource_conflict()
        if self is GetRecordHandlerProgressRequestErrorCode.THROTTLING:
            return throttling()
        if self is GetRecordHandlerProgressRequestErrorCode.SERVICE_LIMIT_EXCEEDED:
            return service_limit_exceeded()
        if self is GetRecordHandlerProgressRequestErrorCode.NOT_STABILIZED:
            return not_stabilized()
        if self is GetRecordHandlerProgressRequestErrorCode.GENERAL_SERVICE_EXCEPTION:
            return general_service_exception()
        if self is GetRecordHandlerProgressRequestErrorCode.SERVICE_INTERNAL_ERROR:
            return service_internal_error()
        if self is GetRecordHandlerProgressRequestErrorCode.NETWORK_FAILURE:
            return network_failure()
        if self is GetRecordHandlerProgressRequestErrorCode.INTERNAL_FAILURE:
            return internal_failure()
        if self is GetRecordHandlerProgressRequestErrorCode.INVALID_TYPE_CONFIGURATION:
            return invalid_type_configuration()
        if self is GetRecordHandlerProgressRequestErrorCode.HANDLER_INTERNAL_FAILURE:
            return handler_internal_failure()
        if self is GetRecordHandlerProgressRequestErrorCode.NON_COMPLIANT:
            return non_compliant()
        if self is GetRecordHandlerProgressRequestErrorCode.UNKNOWN:
            return unknown()
        if self is GetRecordHandlerProgressRequestErrorCode.UNSUPPORTED_TARGET:
            return unsupported_target()
