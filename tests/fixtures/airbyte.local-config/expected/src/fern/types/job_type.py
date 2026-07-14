

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class JobType(str, enum.Enum):
    """
    enum that describes the different types of jobs that the platform runs.
    """

    GET_SPEC = "get_spec"
    CHECK_CONNECTION = "check_connection"
    DISCOVER_SCHEMA = "discover_schema"
    SYNC = "sync"
    RESET_CONNECTION = "reset_connection"
    CONNECTION_UPDATER = "connection_updater"
    REPLICATE = "replicate"

    def visit(
        self,
        get_spec: typing.Callable[[], T_Result],
        check_connection: typing.Callable[[], T_Result],
        discover_schema: typing.Callable[[], T_Result],
        sync: typing.Callable[[], T_Result],
        reset_connection: typing.Callable[[], T_Result],
        connection_updater: typing.Callable[[], T_Result],
        replicate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobType.GET_SPEC:
            return get_spec()
        if self is JobType.CHECK_CONNECTION:
            return check_connection()
        if self is JobType.DISCOVER_SCHEMA:
            return discover_schema()
        if self is JobType.SYNC:
            return sync()
        if self is JobType.RESET_CONNECTION:
            return reset_connection()
        if self is JobType.CONNECTION_UPDATER:
            return connection_updater()
        if self is JobType.REPLICATE:
            return replicate()
