

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateRunStatusBodyHealth(enum.StrEnum):
    CREATED = "CREATED"
    DEAD = "DEAD"
    EXITED = "EXITED"
    PAUSED = "PAUSED"
    REMOVING = "REMOVING"
    RESTARTING = "RESTARTING"
    RUNNING = "RUNNING"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        dead: typing.Callable[[], T_Result],
        exited: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
        removing: typing.Callable[[], T_Result],
        restarting: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateRunStatusBodyHealth.CREATED:
            return created()
        if self is UpdateRunStatusBodyHealth.DEAD:
            return dead()
        if self is UpdateRunStatusBodyHealth.EXITED:
            return exited()
        if self is UpdateRunStatusBodyHealth.PAUSED:
            return paused()
        if self is UpdateRunStatusBodyHealth.REMOVING:
            return removing()
        if self is UpdateRunStatusBodyHealth.RESTARTING:
            return restarting()
        if self is UpdateRunStatusBodyHealth.RUNNING:
            return running()
