

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActionRunResponseOutputRunStepsItemStatus(enum.StrEnum):
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
        if self is ActionRunResponseOutputRunStepsItemStatus.CREATED:
            return created()
        if self is ActionRunResponseOutputRunStepsItemStatus.DEAD:
            return dead()
        if self is ActionRunResponseOutputRunStepsItemStatus.EXITED:
            return exited()
        if self is ActionRunResponseOutputRunStepsItemStatus.PAUSED:
            return paused()
        if self is ActionRunResponseOutputRunStepsItemStatus.REMOVING:
            return removing()
        if self is ActionRunResponseOutputRunStepsItemStatus.RESTARTING:
            return restarting()
        if self is ActionRunResponseOutputRunStepsItemStatus.RUNNING:
            return running()
