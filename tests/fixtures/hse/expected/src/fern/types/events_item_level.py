

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventsItemLevel(enum.StrEnum):
    EMERG = "EMERG"
    ALERT = "ALERT"
    CRIT = "CRIT"
    ERR = "ERR"
    WARNING = "WARNING"
    NOTICE = "NOTICE"
    INFO = "INFO"
    DEBUG = "DEBUG"

    def visit(
        self,
        emerg: typing.Callable[[], T_Result],
        alert: typing.Callable[[], T_Result],
        crit: typing.Callable[[], T_Result],
        err: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        notice: typing.Callable[[], T_Result],
        info: typing.Callable[[], T_Result],
        debug: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EventsItemLevel.EMERG:
            return emerg()
        if self is EventsItemLevel.ALERT:
            return alert()
        if self is EventsItemLevel.CRIT:
            return crit()
        if self is EventsItemLevel.ERR:
            return err()
        if self is EventsItemLevel.WARNING:
            return warning()
        if self is EventsItemLevel.NOTICE:
            return notice()
        if self is EventsItemLevel.INFO:
            return info()
        if self is EventsItemLevel.DEBUG:
            return debug()
