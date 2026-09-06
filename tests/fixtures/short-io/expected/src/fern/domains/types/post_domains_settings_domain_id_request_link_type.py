

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostDomainsSettingsDomainIdRequestLinkType(enum.StrEnum):
    INCREMENT = "increment"
    RANDOM = "random"
    SECURE = "secure"
    FOUR_CHAR = "four-char"
    EIGHT_CHAR = "eight-char"
    TEN_CHAR = "ten-char"

    def visit(
        self,
        increment: typing.Callable[[], T_Result],
        random: typing.Callable[[], T_Result],
        secure: typing.Callable[[], T_Result],
        four_char: typing.Callable[[], T_Result],
        eight_char: typing.Callable[[], T_Result],
        ten_char: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostDomainsSettingsDomainIdRequestLinkType.INCREMENT:
            return increment()
        if self is PostDomainsSettingsDomainIdRequestLinkType.RANDOM:
            return random()
        if self is PostDomainsSettingsDomainIdRequestLinkType.SECURE:
            return secure()
        if self is PostDomainsSettingsDomainIdRequestLinkType.FOUR_CHAR:
            return four_char()
        if self is PostDomainsSettingsDomainIdRequestLinkType.EIGHT_CHAR:
            return eight_char()
        if self is PostDomainsSettingsDomainIdRequestLinkType.TEN_CHAR:
            return ten_char()
