

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListCustomFontsResponseCustomFontsItemFormat(enum.StrEnum):
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
        if self is ListCustomFontsResponseCustomFontsItemFormat.WOFF2:
            return woff2()
        if self is ListCustomFontsResponseCustomFontsItemFormat.WOFF:
            return woff()
        if self is ListCustomFontsResponseCustomFontsItemFormat.TRUETYPE:
            return truetype()
        if self is ListCustomFontsResponseCustomFontsItemFormat.OPENTYPE:
            return opentype()
        if self is ListCustomFontsResponseCustomFontsItemFormat.EMBEDDED_OPENTYPE:
            return embedded_opentype()
        if self is ListCustomFontsResponseCustomFontsItemFormat.SVG:
            return svg()
