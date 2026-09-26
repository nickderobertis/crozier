

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GenerationOutputCreateOutputKind(enum.StrEnum):
    PRODUCT_MAIN = "product_main"
    WHITE_BG = "white_bg"
    SOLID_BG = "solid_bg"
    BANNER = "banner"
    POSTER = "poster"
    HERO = "hero"
    DETAIL = "detail"
    CUSTOM = "custom"

    def visit(
        self,
        product_main: typing.Callable[[], T_Result],
        white_bg: typing.Callable[[], T_Result],
        solid_bg: typing.Callable[[], T_Result],
        banner: typing.Callable[[], T_Result],
        poster: typing.Callable[[], T_Result],
        hero: typing.Callable[[], T_Result],
        detail: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GenerationOutputCreateOutputKind.PRODUCT_MAIN:
            return product_main()
        if self is GenerationOutputCreateOutputKind.WHITE_BG:
            return white_bg()
        if self is GenerationOutputCreateOutputKind.SOLID_BG:
            return solid_bg()
        if self is GenerationOutputCreateOutputKind.BANNER:
            return banner()
        if self is GenerationOutputCreateOutputKind.POSTER:
            return poster()
        if self is GenerationOutputCreateOutputKind.HERO:
            return hero()
        if self is GenerationOutputCreateOutputKind.DETAIL:
            return detail()
        if self is GenerationOutputCreateOutputKind.CUSTOM:
            return custom()
