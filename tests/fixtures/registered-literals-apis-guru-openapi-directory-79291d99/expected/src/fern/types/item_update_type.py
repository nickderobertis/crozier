

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ItemUpdateType(enum.StrEnum):
    """
    Indicates whether an Item requires user interaction to be updated, which can be the case for Items with some forms of two-factor authentication.

    `background` - Item can be updated in the background

    `user_present_required` - Item requires user interaction to be updated
    """

    BACKGROUND = "background"
    USER_PRESENT_REQUIRED = "user_present_required"

    def visit(
        self, background: typing.Callable[[], T_Result], user_present_required: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ItemUpdateType.BACKGROUND:
            return background()
        if self is ItemUpdateType.USER_PRESENT_REQUIRED:
            return user_present_required()
