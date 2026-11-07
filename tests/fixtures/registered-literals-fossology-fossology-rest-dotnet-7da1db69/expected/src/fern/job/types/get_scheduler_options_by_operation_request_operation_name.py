

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSchedulerOptionsByOperationRequestOperationName(enum.StrEnum):
    STATUS = "status"
    DATABASE = "database"
    RELOAD = "reload"
    AGENTS = "agents"
    VERBOSE = "verbose"
    STOP = "stop"
    RESTART = "restart"
    PAUSE = "pause"
    PRIORITY = "priority"

    def visit(
        self,
        status: typing.Callable[[], T_Result],
        database: typing.Callable[[], T_Result],
        reload: typing.Callable[[], T_Result],
        agents: typing.Callable[[], T_Result],
        verbose: typing.Callable[[], T_Result],
        stop: typing.Callable[[], T_Result],
        restart: typing.Callable[[], T_Result],
        pause: typing.Callable[[], T_Result],
        priority: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSchedulerOptionsByOperationRequestOperationName.STATUS:
            return status()
        if self is GetSchedulerOptionsByOperationRequestOperationName.DATABASE:
            return database()
        if self is GetSchedulerOptionsByOperationRequestOperationName.RELOAD:
            return reload()
        if self is GetSchedulerOptionsByOperationRequestOperationName.AGENTS:
            return agents()
        if self is GetSchedulerOptionsByOperationRequestOperationName.VERBOSE:
            return verbose()
        if self is GetSchedulerOptionsByOperationRequestOperationName.STOP:
            return stop()
        if self is GetSchedulerOptionsByOperationRequestOperationName.RESTART:
            return restart()
        if self is GetSchedulerOptionsByOperationRequestOperationName.PAUSE:
            return pause()
        if self is GetSchedulerOptionsByOperationRequestOperationName.PRIORITY:
            return priority()
