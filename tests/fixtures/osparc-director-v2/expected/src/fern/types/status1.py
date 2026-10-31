

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Status1(enum.StrEnum):
    """
    String representation of the container state. Can be one of "created",
    "running", "paused", "restarting", "removing", "exited", or "dead".
    """

    CREATED = "created"
    RUNNING = "running"
    PAUSED = "paused"
    RESTARTING = "restarting"
    REMOVING = "removing"
    EXITED = "exited"
    DEAD = "dead"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
        restarting: typing.Callable[[], T_Result],
        removing: typing.Callable[[], T_Result],
        exited: typing.Callable[[], T_Result],
        dead: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Status1.CREATED:
            return created()
        if self is Status1.RUNNING:
            return running()
        if self is Status1.PAUSED:
            return paused()
        if self is Status1.RESTARTING:
            return restarting()
        if self is Status1.REMOVING:
            return removing()
        if self is Status1.EXITED:
            return exited()
        if self is Status1.DEAD:
            return dead()
