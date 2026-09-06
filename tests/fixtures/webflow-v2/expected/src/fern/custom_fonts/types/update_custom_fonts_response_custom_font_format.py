

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateCustomFontsResponseCustomFontFormat(enum.StrEnum):
    """
    The font file format, derived from the file extension. The value `svg` represents read-only legacy data; new SVG font uploads are not accepted.
    """

    WOFF2 = "woff2"
    WOFF = "woff"
    TRUETYPE = "truetype"
    OPENTYPE = "opentype"
    EMBEDDED_OPENTYPE = "embedded-opentype"
    SVG = "svg"

    def visit(
        self,
        woff2: typing.Callable[[], T_Result],
        woff: typing.Callable[[], T_Result],
        truetype: typing.Callable[[], T_Result],
        opentype: typing.Callable[[], T_Result],
        embedded_opentype: typing.Callable[[], T_Result],
        svg: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateCustomFontsResponseCustomFontFormat.WOFF2:
            return woff2()
        if self is UpdateCustomFontsResponseCustomFontFormat.WOFF:
            return woff()
        if self is UpdateCustomFontsResponseCustomFontFormat.TRUETYPE:
            return truetype()
        if self is UpdateCustomFontsResponseCustomFontFormat.OPENTYPE:
            return opentype()
        if self is UpdateCustomFontsResponseCustomFontFormat.EMBEDDED_OPENTYPE:
            return embedded_opentype()
        if self is UpdateCustomFontsResponseCustomFontFormat.SVG:
            return svg()
