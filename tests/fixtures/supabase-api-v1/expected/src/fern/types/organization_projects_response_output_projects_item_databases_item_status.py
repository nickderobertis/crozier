

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrganizationProjectsResponseOutputProjectsItemDatabasesItemStatus(enum.StrEnum):
    ACTIVE_HEALTHY = "ACTIVE_HEALTHY"
    ACTIVE_UNHEALTHY = "ACTIVE_UNHEALTHY"
    COMING_UP = "COMING_UP"
    GOING_DOWN = "GOING_DOWN"
    INIT_FAILED = "INIT_FAILED"
    REMOVED = "REMOVED"
    RESTORING = "RESTORING"
    UNKNOWN = "UNKNOWN"
    INIT_READ_REPLICA = "INIT_READ_REPLICA"
    INIT_READ_REPLICA_FAILED = "INIT_READ_REPLICA_FAILED"
    RESTARTING = "RESTARTING"
    RESIZING = "RESIZING"

    def visit(
        self,
        active_healthy: typing.Callable[[], T_Result],
        active_unhealthy: typing.Callable[[], T_Result],
        coming_up: typing.Callable[[], T_Result],
        going_down: typing.Callable[[], T_Result],
        init_failed: typing.Callable[[], T_Result],
        removed: typing.Callable[[], T_Result],
        restoring: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        init_read_replica: typing.Callable[[], T_Result],
        init_read_replica_failed: typing.Callable[[], T_Result],
        restarting: typing.Callable[[], T_Result],
        resizing: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemStatus.ACTIVE_HEALTHY:
            return active_healthy()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemStatus.ACTIVE_UNHEALTHY:
            return active_unhealthy()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemStatus.COMING_UP:
            return coming_up()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemStatus.GOING_DOWN:
            return going_down()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemStatus.INIT_FAILED:
            return init_failed()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemStatus.REMOVED:
            return removed()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemStatus.RESTORING:
            return restoring()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemStatus.UNKNOWN:
            return unknown()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemStatus.INIT_READ_REPLICA:
            return init_read_replica()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemStatus.INIT_READ_REPLICA_FAILED:
            return init_read_replica_failed()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemStatus.RESTARTING:
            return restarting()
        if self is OrganizationProjectsResponseOutputProjectsItemDatabasesItemStatus.RESIZING:
            return resizing()
