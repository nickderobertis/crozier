

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrganizationProjectsResponseOutputProjectsItemStatus(enum.StrEnum):
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
        if self is OrganizationProjectsResponseOutputProjectsItemStatus.INACTIVE:
            return inactive()
        if self is OrganizationProjectsResponseOutputProjectsItemStatus.ACTIVE_HEALTHY:
            return active_healthy()
        if self is OrganizationProjectsResponseOutputProjectsItemStatus.ACTIVE_UNHEALTHY:
            return active_unhealthy()
        if self is OrganizationProjectsResponseOutputProjectsItemStatus.COMING_UP:
            return coming_up()
        if self is OrganizationProjectsResponseOutputProjectsItemStatus.UNKNOWN:
            return unknown()
        if self is OrganizationProjectsResponseOutputProjectsItemStatus.GOING_DOWN:
            return going_down()
        if self is OrganizationProjectsResponseOutputProjectsItemStatus.INIT_FAILED:
            return init_failed()
        if self is OrganizationProjectsResponseOutputProjectsItemStatus.REMOVED:
            return removed()
        if self is OrganizationProjectsResponseOutputProjectsItemStatus.RESTORING:
            return restoring()
        if self is OrganizationProjectsResponseOutputProjectsItemStatus.UPGRADING:
            return upgrading()
        if self is OrganizationProjectsResponseOutputProjectsItemStatus.PAUSING:
            return pausing()
        if self is OrganizationProjectsResponseOutputProjectsItemStatus.RESTORE_FAILED:
            return restore_failed()
        if self is OrganizationProjectsResponseOutputProjectsItemStatus.RESTARTING:
            return restarting()
        if self is OrganizationProjectsResponseOutputProjectsItemStatus.PAUSE_FAILED:
            return pause_failed()
        if self is OrganizationProjectsResponseOutputProjectsItemStatus.RESIZING:
            return resizing()
