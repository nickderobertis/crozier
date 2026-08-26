

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SetConfigType(enum.StrEnum):
    SET_CONFIG = "set-config"

    def visit(self, set_config: typing.Callable[[], T_Result]) -> T_Result:
        if self is SetConfigType.SET_CONFIG:
            return set_config()
