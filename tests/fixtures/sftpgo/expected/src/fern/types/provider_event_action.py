

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderEventAction(enum.StrEnum):
    ADD = "add"
    UPDATE = "update"
    DELETE = "delete"

    def visit(
        self,
        add: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProviderEventAction.ADD:
            return add()
        if self is ProviderEventAction.UPDATE:
            return update()
        if self is ProviderEventAction.DELETE:
            return delete()
