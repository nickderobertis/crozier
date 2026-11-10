

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateModerationRequestModelOne(enum.StrEnum):
    TEXT_MODERATION_LATEST = "text-moderation-latest"
    TEXT_MODERATION_STABLE = "text-moderation-stable"

    def visit(
        self,
        text_moderation_latest: typing.Callable[[], T_Result],
        text_moderation_stable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateModerationRequestModelOne.TEXT_MODERATION_LATEST:
            return text_moderation_latest()
        if self is CreateModerationRequestModelOne.TEXT_MODERATION_STABLE:
            return text_moderation_stable()
