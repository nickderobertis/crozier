

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode(enum.StrEnum):
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
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode.NORMAL:
            return normal()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode.MULTIPLY:
            return multiply()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode.SCREEN:
            return screen()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode.OVERLAY:
            return overlay()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode.DARKEN:
            return darken()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode.LIGHTEN:
            return lighten()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode.COLOR_DODGE:
            return color_dodge()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode.COLOR_BURN:
            return color_burn()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode.HARD_LIGHT:
            return hard_light()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode.SOFT_LIGHT:
            return soft_light()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode.DIFFERENCE:
            return difference()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode.EXCLUSION:
            return exclusion()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode.HUE:
            return hue()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode.SATURATION:
            return saturation()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode.COLOR:
            return color()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode.LUMINOSITY:
            return luminosity()
