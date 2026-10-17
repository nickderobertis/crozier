

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateRunStatusBodyConfigure(enum.StrEnum):
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
        if self is UpdateRunStatusBodyConfigure.CREATED:
            return created()
        if self is UpdateRunStatusBodyConfigure.DEAD:
            return dead()
        if self is UpdateRunStatusBodyConfigure.EXITED:
            return exited()
        if self is UpdateRunStatusBodyConfigure.PAUSED:
            return paused()
        if self is UpdateRunStatusBodyConfigure.REMOVING:
            return removing()
        if self is UpdateRunStatusBodyConfigure.RESTARTING:
            return restarting()
        if self is UpdateRunStatusBodyConfigure.RUNNING:
            return running()
