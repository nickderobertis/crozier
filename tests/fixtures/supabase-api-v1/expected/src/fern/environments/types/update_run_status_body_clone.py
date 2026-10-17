

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateRunStatusBodyClone(enum.StrEnum):
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
        if self is UpdateRunStatusBodyClone.CREATED:
            return created()
        if self is UpdateRunStatusBodyClone.DEAD:
            return dead()
        if self is UpdateRunStatusBodyClone.EXITED:
            return exited()
        if self is UpdateRunStatusBodyClone.PAUSED:
            return paused()
        if self is UpdateRunStatusBodyClone.REMOVING:
            return removing()
        if self is UpdateRunStatusBodyClone.RESTARTING:
            return restarting()
        if self is UpdateRunStatusBodyClone.RUNNING:
            return running()
