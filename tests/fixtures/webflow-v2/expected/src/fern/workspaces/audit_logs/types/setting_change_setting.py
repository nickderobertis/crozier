

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class SettingChangeSetting(enum.StrEnum):
    AI_TOGGLE = "ai_toggle"

    def visit(self, ai_toggle: typing.Callable[[], T_Result]) -> T_Result:
        if self is SettingChangeSetting.AI_TOGGLE:
            return ai_toggle()
