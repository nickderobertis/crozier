

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode(enum.StrEnum):
    NORMAL = "normal"
    MULTIPLY = "multiply"
    SCREEN = "screen"
    OVERLAY = "overlay"
    DARKEN = "darken"
    LIGHTEN = "lighten"
    COLOR_DODGE = "color-dodge"
    COLOR_BURN = "color-burn"
    HARD_LIGHT = "hard-light"
    SOFT_LIGHT = "soft-light"
    DIFFERENCE = "difference"
    EXCLUSION = "exclusion"
    HUE = "hue"
    SATURATION = "saturation"
    COLOR = "color"
    LUMINOSITY = "luminosity"

    def visit(
        self,
        normal: typing.Callable[[], T_Result],
        multiply: typing.Callable[[], T_Result],
        screen: typing.Callable[[], T_Result],
        overlay: typing.Callable[[], T_Result],
        darken: typing.Callable[[], T_Result],
        lighten: typing.Callable[[], T_Result],
        color_dodge: typing.Callable[[], T_Result],
        color_burn: typing.Callable[[], T_Result],
        hard_light: typing.Callable[[], T_Result],
        soft_light: typing.Callable[[], T_Result],
        difference: typing.Callable[[], T_Result],
        exclusion: typing.Callable[[], T_Result],
        hue: typing.Callable[[], T_Result],
        saturation: typing.Callable[[], T_Result],
        color: typing.Callable[[], T_Result],
        luminosity: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode.NORMAL:
            return normal()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode.MULTIPLY:
            return multiply()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode.SCREEN:
            return screen()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode.OVERLAY:
            return overlay()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode.DARKEN:
            return darken()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode.LIGHTEN:
            return lighten()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode.COLOR_DODGE:
            return color_dodge()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode.COLOR_BURN:
            return color_burn()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode.HARD_LIGHT:
            return hard_light()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode.SOFT_LIGHT:
            return soft_light()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode.DIFFERENCE:
            return difference()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode.EXCLUSION:
            return exclusion()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode.HUE:
            return hue()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode.SATURATION:
            return saturation()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode.COLOR:
            return color()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode.LUMINOSITY:
            return luminosity()
