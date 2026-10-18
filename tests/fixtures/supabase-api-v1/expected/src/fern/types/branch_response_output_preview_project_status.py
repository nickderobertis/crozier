

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BranchResponseOutputPreviewProjectStatus(enum.StrEnum):
    INACTIVE = "INACTIVE"
    ACTIVE_HEALTHY = "ACTIVE_HEALTHY"
    ACTIVE_UNHEALTHY = "ACTIVE_UNHEALTHY"
    COMING_UP = "COMING_UP"
    UNKNOWN = "UNKNOWN"
    GOING_DOWN = "GOING_DOWN"
    INIT_FAILED = "INIT_FAILED"
    REMOVED = "REMOVED"
    RESTORING = "RESTORING"
    UPGRADING = "UPGRADING"
    PAUSING = "PAUSING"
    RESTORE_FAILED = "RESTORE_FAILED"
    RESTARTING = "RESTARTING"
    PAUSE_FAILED = "PAUSE_FAILED"
    RESIZING = "RESIZING"

    def visit(
        self,
        inactive: typing.Callable[[], T_Result],
        active_healthy: typing.Callable[[], T_Result],
        active_unhealthy: typing.Callable[[], T_Result],
        coming_up: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        going_down: typing.Callable[[], T_Result],
        init_failed: typing.Callable[[], T_Result],
        removed: typing.Callable[[], T_Result],
        restoring: typing.Callable[[], T_Result],
        upgrading: typing.Callable[[], T_Result],
        pausing: typing.Callable[[], T_Result],
        restore_failed: typing.Callable[[], T_Result],
        restarting: typing.Callable[[], T_Result],
        pause_failed: typing.Callable[[], T_Result],
        resizing: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BranchResponseOutputPreviewProjectStatus.INACTIVE:
            return inactive()
        if self is BranchResponseOutputPreviewProjectStatus.ACTIVE_HEALTHY:
            return active_healthy()
        if self is BranchResponseOutputPreviewProjectStatus.ACTIVE_UNHEALTHY:
            return active_unhealthy()
        if self is BranchResponseOutputPreviewProjectStatus.COMING_UP:
            return coming_up()
        if self is BranchResponseOutputPreviewProjectStatus.UNKNOWN:
            return unknown()
        if self is BranchResponseOutputPreviewProjectStatus.GOING_DOWN:
            return going_down()
        if self is BranchResponseOutputPreviewProjectStatus.INIT_FAILED:
            return init_failed()
        if self is BranchResponseOutputPreviewProjectStatus.REMOVED:
            return removed()
        if self is BranchResponseOutputPreviewProjectStatus.RESTORING:
            return restoring()
        if self is BranchResponseOutputPreviewProjectStatus.UPGRADING:
            return upgrading()
        if self is BranchResponseOutputPreviewProjectStatus.PAUSING:
            return pausing()
        if self is BranchResponseOutputPreviewProjectStatus.RESTORE_FAILED:
            return restore_failed()
        if self is BranchResponseOutputPreviewProjectStatus.RESTARTING:
            return restarting()
        if self is BranchResponseOutputPreviewProjectStatus.PAUSE_FAILED:
            return pause_failed()
        if self is BranchResponseOutputPreviewProjectStatus.RESIZING:
            return resizing()
