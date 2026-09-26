

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode(enum.StrEnum):
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
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode.NORMAL:
            return normal()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode.MULTIPLY:
            return multiply()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode.SCREEN:
            return screen()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode.OVERLAY:
            return overlay()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode.DARKEN:
            return darken()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode.LIGHTEN:
            return lighten()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode.COLOR_DODGE:
            return color_dodge()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode.COLOR_BURN:
            return color_burn()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode.HARD_LIGHT:
            return hard_light()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode.SOFT_LIGHT:
            return soft_light()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode.DIFFERENCE:
            return difference()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode.EXCLUSION:
            return exclusion()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode.HUE:
            return hue()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode.SATURATION:
            return saturation()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode.COLOR:
            return color()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode.LUMINOSITY:
            return luminosity()
