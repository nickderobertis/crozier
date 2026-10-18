

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateRunStatusBodyDeploy(enum.StrEnum):
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
        if self is UpdateRunStatusBodyDeploy.CREATED:
            return created()
        if self is UpdateRunStatusBodyDeploy.DEAD:
            return dead()
        if self is UpdateRunStatusBodyDeploy.EXITED:
            return exited()
        if self is UpdateRunStatusBodyDeploy.PAUSED:
            return paused()
        if self is UpdateRunStatusBodyDeploy.REMOVING:
            return removing()
        if self is UpdateRunStatusBodyDeploy.RESTARTING:
            return restarting()
        if self is UpdateRunStatusBodyDeploy.RUNNING:
            return running()
