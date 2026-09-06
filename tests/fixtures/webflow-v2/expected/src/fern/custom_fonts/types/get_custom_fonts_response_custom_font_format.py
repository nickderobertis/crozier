

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCustomFontsResponseCustomFontFormat(enum.StrEnum):
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
        if self is GetCustomFontsResponseCustomFontFormat.WOFF2:
            return woff2()
        if self is GetCustomFontsResponseCustomFontFormat.WOFF:
            return woff()
        if self is GetCustomFontsResponseCustomFontFormat.TRUETYPE:
            return truetype()
        if self is GetCustomFontsResponseCustomFontFormat.OPENTYPE:
            return opentype()
        if self is GetCustomFontsResponseCustomFontFormat.EMBEDDED_OPENTYPE:
            return embedded_opentype()
        if self is GetCustomFontsResponseCustomFontFormat.SVG:
            return svg()
