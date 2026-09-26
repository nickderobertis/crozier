

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemLineBlendMode(enum.StrEnum):
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
        if self is DocAnnotationsList200ResponseAnnotationsItemLineBlendMode.NORMAL:
            return normal()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineBlendMode.MULTIPLY:
            return multiply()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineBlendMode.SCREEN:
            return screen()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineBlendMode.OVERLAY:
            return overlay()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineBlendMode.DARKEN:
            return darken()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineBlendMode.LIGHTEN:
            return lighten()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineBlendMode.COLOR_DODGE:
            return color_dodge()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineBlendMode.COLOR_BURN:
            return color_burn()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineBlendMode.HARD_LIGHT:
            return hard_light()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineBlendMode.SOFT_LIGHT:
            return soft_light()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineBlendMode.DIFFERENCE:
            return difference()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineBlendMode.EXCLUSION:
            return exclusion()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineBlendMode.HUE:
            return hue()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineBlendMode.SATURATION:
            return saturation()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineBlendMode.COLOR:
            return color()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineBlendMode.LUMINOSITY:
            return luminosity()
