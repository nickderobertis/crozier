

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CommonStandardObject(enum.StrEnum):
    COMPANY = "company"
    CONTACT = "contact"
    DEAL = "deal"
    EVENT = "event"
    LEAD = "lead"
    NOTE = "note"
    TASK = "task"
    USER = "user"

    def visit(
        self,
        company: typing.Callable[[], T_Result],
        contact: typing.Callable[[], T_Result],
        deal: typing.Callable[[], T_Result],
        event: typing.Callable[[], T_Result],
        lead: typing.Callable[[], T_Result],
        note: typing.Callable[[], T_Result],
        task: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CommonStandardObject.COMPANY:
            return company()
        if self is CommonStandardObject.CONTACT:
            return contact()
        if self is CommonStandardObject.DEAL:
            return deal()
        if self is CommonStandardObject.EVENT:
            return event()
        if self is CommonStandardObject.LEAD:
            return lead()
        if self is CommonStandardObject.NOTE:
            return note()
        if self is CommonStandardObject.TASK:
            return task()
        if self is CommonStandardObject.USER:
            return user()
