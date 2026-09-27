

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatTurnRequestSelectedPlatformsItem(enum.StrEnum):
    TELEGRAM = "telegram"
    VK = "vk"
    YANDEX_BUSINESS = "yandex_business"

    def visit(
        self,
        telegram: typing.Callable[[], T_Result],
        vk: typing.Callable[[], T_Result],
        yandex_business: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatTurnRequestSelectedPlatformsItem.TELEGRAM:
            return telegram()
        if self is ChatTurnRequestSelectedPlatformsItem.VK:
            return vk()
        if self is ChatTurnRequestSelectedPlatformsItem.YANDEX_BUSINESS:
            return yandex_business()
