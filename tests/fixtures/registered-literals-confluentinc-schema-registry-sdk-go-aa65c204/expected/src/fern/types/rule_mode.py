

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RuleMode(enum.StrEnum):
    """
    Rule mode
    """

    UPGRADE = "UPGRADE"
    DOWNGRADE = "DOWNGRADE"
    UPDOWN = "UPDOWN"
    WRITE = "WRITE"
    READ = "READ"
    WRITEREAD = "WRITEREAD"

    def visit(
        self,
        upgrade: typing.Callable[[], T_Result],
        downgrade: typing.Callable[[], T_Result],
        updown: typing.Callable[[], T_Result],
        write: typing.Callable[[], T_Result],
        read: typing.Callable[[], T_Result],
        writeread: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RuleMode.UPGRADE:
            return upgrade()
        if self is RuleMode.DOWNGRADE:
            return downgrade()
        if self is RuleMode.UPDOWN:
            return updown()
        if self is RuleMode.WRITE:
            return write()
        if self is RuleMode.READ:
            return read()
        if self is RuleMode.WRITEREAD:
            return writeread()
