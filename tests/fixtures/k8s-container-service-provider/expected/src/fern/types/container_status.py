

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContainerStatus(enum.StrEnum):
    """
    Current status of the container instance
    """

    PENDING = "PENDING"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"
    DELETED = "DELETED"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContainerStatus.PENDING:
            return pending()
        if self is ContainerStatus.RUNNING:
            return running()
        if self is ContainerStatus.FAILED:
            return failed()
        if self is ContainerStatus.UNKNOWN:
            return unknown()
        if self is ContainerStatus.DELETED:
            return deleted()
