

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateUserConfigCommandType(enum.StrEnum):
    UPDATE_USER_CONFIG = "update-user-config"

    def visit(self, update_user_config: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateUserConfigCommandType.UPDATE_USER_CONFIG:
            return update_user_config()
