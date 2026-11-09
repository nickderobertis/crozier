

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class HandleSchedulerRunRequestOperation(enum.StrEnum):
    """
    Operation to be run by the scheduler
    """

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
        if self is HandleSchedulerRunRequestOperation.STATUS:
            return status()
        if self is HandleSchedulerRunRequestOperation.DATABASE:
            return database()
        if self is HandleSchedulerRunRequestOperation.RELOAD:
            return reload()
        if self is HandleSchedulerRunRequestOperation.AGENTS:
            return agents()
        if self is HandleSchedulerRunRequestOperation.VERBOSE:
            return verbose()
        if self is HandleSchedulerRunRequestOperation.STOP:
            return stop()
        if self is HandleSchedulerRunRequestOperation.RESTART:
            return restart()
        if self is HandleSchedulerRunRequestOperation.PAUSE:
            return pause()
        if self is HandleSchedulerRunRequestOperation.PRIORITY:
            return priority()
