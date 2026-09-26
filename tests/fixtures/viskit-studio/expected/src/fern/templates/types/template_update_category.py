

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TemplateUpdateCategory(enum.StrEnum):
    HERO = "hero"
    DETAIL_M3 = "detail_m3"
    LIFESTYLE = "lifestyle"
    SHORT_VIDEO = "short_video"
    AMAZON_HERO = "amazon_hero"

    def visit(
        self,
        hero: typing.Callable[[], T_Result],
        detail_m3: typing.Callable[[], T_Result],
        lifestyle: typing.Callable[[], T_Result],
        short_video: typing.Callable[[], T_Result],
        amazon_hero: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TemplateUpdateCategory.HERO:
            return hero()
        if self is TemplateUpdateCategory.DETAIL_M3:
            return detail_m3()
        if self is TemplateUpdateCategory.LIFESTYLE:
            return lifestyle()
        if self is TemplateUpdateCategory.SHORT_VIDEO:
            return short_video()
        if self is TemplateUpdateCategory.AMAZON_HERO:
            return amazon_hero()
