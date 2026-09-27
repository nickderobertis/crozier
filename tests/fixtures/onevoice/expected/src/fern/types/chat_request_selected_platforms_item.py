

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatRequestSelectedPlatformsItem(enum.StrEnum):
    TELEGRAM = "telegram"
    VK = "vk"
    YANDEX_BUSINESS = "yandex_business"

    def visit(
        self,
        telegram: typing.Callable[[], T_Result],
        vk: typing.Callable[[], T_Result],
        yandex_business: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatRequestSelectedPlatformsItem.TELEGRAM:
            return telegram()
        if self is ChatRequestSelectedPlatformsItem.VK:
            return vk()
        if self is ChatRequestSelectedPlatformsItem.YANDEX_BUSINESS:
            return yandex_business()
