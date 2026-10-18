

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProtocolErrorError(enum.StrEnum):
    INVALID_ARGUMENT = "invalid_argument"
    UNKNOWN_COMMAND = "unknown_command"
    UNKNOWN_ERROR = "unknown_error"
    NO_SUCH_RUN = "no_such_run"
    NO_SUCH_SUBSCRIPTION = "no_such_subscription"
    NO_SUCH_NAMESPACE = "no_such_namespace"
    NO_SUCH_INTERRUPT = "no_such_interrupt"
    NO_SUCH_CHECKPOINT = "no_such_checkpoint"
    PERMISSION_DENIED = "permission_denied"
    NOT_SUPPORTED = "not_supported"

    def visit(
        self,
        invalid_argument: typing.Callable[[], T_Result],
        unknown_command: typing.Callable[[], T_Result],
        unknown_error: typing.Callable[[], T_Result],
        no_such_run: typing.Callable[[], T_Result],
        no_such_subscription: typing.Callable[[], T_Result],
        no_such_namespace: typing.Callable[[], T_Result],
        no_such_interrupt: typing.Callable[[], T_Result],
        no_such_checkpoint: typing.Callable[[], T_Result],
        permission_denied: typing.Callable[[], T_Result],
        not_supported: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProtocolErrorError.INVALID_ARGUMENT:
            return invalid_argument()
        if self is ProtocolErrorError.UNKNOWN_COMMAND:
            return unknown_command()
        if self is ProtocolErrorError.UNKNOWN_ERROR:
            return unknown_error()
        if self is ProtocolErrorError.NO_SUCH_RUN:
            return no_such_run()
        if self is ProtocolErrorError.NO_SUCH_SUBSCRIPTION:
            return no_such_subscription()
        if self is ProtocolErrorError.NO_SUCH_NAMESPACE:
            return no_such_namespace()
        if self is ProtocolErrorError.NO_SUCH_INTERRUPT:
            return no_such_interrupt()
        if self is ProtocolErrorError.NO_SUCH_CHECKPOINT:
            return no_such_checkpoint()
        if self is ProtocolErrorError.PERMISSION_DENIED:
            return permission_denied()
        if self is ProtocolErrorError.NOT_SUPPORTED:
            return not_supported()
