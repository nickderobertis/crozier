

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateRunStatusBodyMigrate(enum.StrEnum):
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
        if self is UpdateRunStatusBodyMigrate.CREATED:
            return created()
        if self is UpdateRunStatusBodyMigrate.DEAD:
            return dead()
        if self is UpdateRunStatusBodyMigrate.EXITED:
            return exited()
        if self is UpdateRunStatusBodyMigrate.PAUSED:
            return paused()
        if self is UpdateRunStatusBodyMigrate.REMOVING:
            return removing()
        if self is UpdateRunStatusBodyMigrate.RESTARTING:
            return restarting()
        if self is UpdateRunStatusBodyMigrate.RUNNING:
            return running()
