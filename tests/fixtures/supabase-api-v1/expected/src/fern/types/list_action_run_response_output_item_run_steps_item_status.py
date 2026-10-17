

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListActionRunResponseOutputItemRunStepsItemStatus(enum.StrEnum):
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
        if self is ListActionRunResponseOutputItemRunStepsItemStatus.CREATED:
            return created()
        if self is ListActionRunResponseOutputItemRunStepsItemStatus.DEAD:
            return dead()
        if self is ListActionRunResponseOutputItemRunStepsItemStatus.EXITED:
            return exited()
        if self is ListActionRunResponseOutputItemRunStepsItemStatus.PAUSED:
            return paused()
        if self is ListActionRunResponseOutputItemRunStepsItemStatus.REMOVING:
            return removing()
        if self is ListActionRunResponseOutputItemRunStepsItemStatus.RESTARTING:
            return restarting()
        if self is ListActionRunResponseOutputItemRunStepsItemStatus.RUNNING:
            return running()
