

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateRunStatusBodySeed(enum.StrEnum):
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
        if self is UpdateRunStatusBodySeed.CREATED:
            return created()
        if self is UpdateRunStatusBodySeed.DEAD:
            return dead()
        if self is UpdateRunStatusBodySeed.EXITED:
            return exited()
        if self is UpdateRunStatusBodySeed.PAUSED:
            return paused()
        if self is UpdateRunStatusBodySeed.REMOVING:
            return removing()
        if self is UpdateRunStatusBodySeed.RESTARTING:
            return restarting()
        if self is UpdateRunStatusBodySeed.RUNNING:
            return running()
