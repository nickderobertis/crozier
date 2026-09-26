

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily(enum.StrEnum):
    COURIER = "courier"
    COURIER_BOLD = "courier-bold"
    COURIER_BOLD_OBLIQUE = "courier-bold-oblique"
    COURIER_OBLIQUE = "courier-oblique"
    HELVETICA = "helvetica"
    HELVETICA_BOLD = "helvetica-bold"
    HELVETICA_BOLD_OBLIQUE = "helvetica-bold-oblique"
    HELVETICA_OBLIQUE = "helvetica-oblique"
    TIMES_ROMAN = "times-roman"
    TIMES_BOLD = "times-bold"
    TIMES_BOLD_ITALIC = "times-bold-italic"
    TIMES_ITALIC = "times-italic"
    SYMBOL = "symbol"
    ZAPF_DINGBATS = "zapf-dingbats"

    def visit(
        self,
        courier: typing.Callable[[], T_Result],
        courier_bold: typing.Callable[[], T_Result],
        courier_bold_oblique: typing.Callable[[], T_Result],
        courier_oblique: typing.Callable[[], T_Result],
        helvetica: typing.Callable[[], T_Result],
        helvetica_bold: typing.Callable[[], T_Result],
        helvetica_bold_oblique: typing.Callable[[], T_Result],
        helvetica_oblique: typing.Callable[[], T_Result],
        times_roman: typing.Callable[[], T_Result],
        times_bold: typing.Callable[[], T_Result],
        times_bold_italic: typing.Callable[[], T_Result],
        times_italic: typing.Callable[[], T_Result],
        symbol: typing.Callable[[], T_Result],
        zapf_dingbats: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily.COURIER:
            return courier()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily.COURIER_BOLD:
            return courier_bold()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily.COURIER_BOLD_OBLIQUE:
            return courier_bold_oblique()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily.COURIER_OBLIQUE:
            return courier_oblique()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily.HELVETICA:
            return helvetica()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily.HELVETICA_BOLD:
            return helvetica_bold()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily.HELVETICA_BOLD_OBLIQUE:
            return helvetica_bold_oblique()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily.HELVETICA_OBLIQUE:
            return helvetica_oblique()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily.TIMES_ROMAN:
            return times_roman()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily.TIMES_BOLD:
            return times_bold()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily.TIMES_BOLD_ITALIC:
            return times_bold_italic()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily.TIMES_ITALIC:
            return times_italic()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily.SYMBOL:
            return symbol()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily.ZAPF_DINGBATS:
            return zapf_dingbats()
