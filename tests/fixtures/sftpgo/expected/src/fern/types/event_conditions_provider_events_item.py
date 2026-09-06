

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventConditionsProviderEventsItem(enum.StrEnum):
    ADD = "add"
    UPDATE = "update"
    DELETE = "delete"

    def visit(
        self,
        add: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EventConditionsProviderEventsItem.ADD:
            return add()
        if self is EventConditionsProviderEventsItem.UPDATE:
            return update()
        if self is EventConditionsProviderEventsItem.DELETE:
            return delete()
