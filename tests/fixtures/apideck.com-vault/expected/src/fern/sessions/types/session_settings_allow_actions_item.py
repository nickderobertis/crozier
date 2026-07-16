

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SessionSettingsAllowActionsItem(enum.StrEnum):
    DELETE = "delete"
    DISCONNECT = "disconnect"
    REAUTHORIZE = "reauthorize"
    DISABLE = "disable"

    def visit(
        self,
        delete: typing.Callable[[], T_Result],
        disconnect: typing.Callable[[], T_Result],
        reauthorize: typing.Callable[[], T_Result],
        disable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SessionSettingsAllowActionsItem.DELETE:
            return delete()
        if self is SessionSettingsAllowActionsItem.DISCONNECT:
            return disconnect()
        if self is SessionSettingsAllowActionsItem.REAUTHORIZE:
            return reauthorize()
        if self is SessionSettingsAllowActionsItem.DISABLE:
            return disable()
