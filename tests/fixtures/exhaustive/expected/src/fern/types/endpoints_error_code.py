

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EndpointsErrorCode(str, enum.Enum):
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    UNAUTHORIZED = "UNAUTHORIZED"
    FORBIDDEN = "FORBIDDEN"
    BAD_REQUEST = "BAD_REQUEST"
    CONFLICT = "CONFLICT"
    GONE = "GONE"
    UNPROCESSABLE_ENTITY = "UNPROCESSABLE_ENTITY"
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
    BAD_GATEWAY = "BAD_GATEWAY"
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"
    UNKNOWN = "Unknown"

    def visit(
        self,
        internal_server_error: typing.Callable[[], T_Result],
        unauthorized: typing.Callable[[], T_Result],
        forbidden: typing.Callable[[], T_Result],
        bad_request: typing.Callable[[], T_Result],
        conflict: typing.Callable[[], T_Result],
        gone: typing.Callable[[], T_Result],
        unprocessable_entity: typing.Callable[[], T_Result],
        not_implemented: typing.Callable[[], T_Result],
        bad_gateway: typing.Callable[[], T_Result],
        service_unavailable: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EndpointsErrorCode.INTERNAL_SERVER_ERROR:
            return internal_server_error()
        if self is EndpointsErrorCode.UNAUTHORIZED:
            return unauthorized()
        if self is EndpointsErrorCode.FORBIDDEN:
            return forbidden()
        if self is EndpointsErrorCode.BAD_REQUEST:
            return bad_request()
        if self is EndpointsErrorCode.CONFLICT:
            return conflict()
        if self is EndpointsErrorCode.GONE:
            return gone()
        if self is EndpointsErrorCode.UNPROCESSABLE_ENTITY:
            return unprocessable_entity()
        if self is EndpointsErrorCode.NOT_IMPLEMENTED:
            return not_implemented()
        if self is EndpointsErrorCode.BAD_GATEWAY:
            return bad_gateway()
        if self is EndpointsErrorCode.SERVICE_UNAVAILABLE:
            return service_unavailable()
        if self is EndpointsErrorCode.UNKNOWN:
            return unknown()
