

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class JobConfigType(str, enum.Enum):
    CHECK_CONNECTION_SOURCE = "check_connection_source"
    CHECK_CONNECTION_DESTINATION = "check_connection_destination"
    DISCOVER_SCHEMA = "discover_schema"
    GET_SPEC = "get_spec"
    SYNC = "sync"
    RESET_CONNECTION = "reset_connection"

    def visit(
        self,
        check_connection_source: typing.Callable[[], T_Result],
        check_connection_destination: typing.Callable[[], T_Result],
        discover_schema: typing.Callable[[], T_Result],
        get_spec: typing.Callable[[], T_Result],
        sync: typing.Callable[[], T_Result],
        reset_connection: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobConfigType.CHECK_CONNECTION_SOURCE:
            return check_connection_source()
        if self is JobConfigType.CHECK_CONNECTION_DESTINATION:
            return check_connection_destination()
        if self is JobConfigType.DISCOVER_SCHEMA:
            return discover_schema()
        if self is JobConfigType.GET_SPEC:
            return get_spec()
        if self is JobConfigType.SYNC:
            return sync()
        if self is JobConfigType.RESET_CONNECTION:
            return reset_connection()
