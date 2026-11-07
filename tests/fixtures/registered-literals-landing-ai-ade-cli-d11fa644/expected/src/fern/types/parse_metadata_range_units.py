

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParseMetadataRangeUnits(enum.StrEnum):
    """
    Units of every `range` offset in the response. Always `"unicode_codepoints"` (Unicode code points into `markdown`). Declared explicitly so consumers know how to slice the string — e.g. JavaScript strings are UTF-16, so a naive `.slice()` drifts when the markdown contains astral characters; such consumers must convert code-point offsets to UTF-16 indices first.
    """

    UNICODE_CODEPOINTS = "unicode_codepoints"

    def visit(self, unicode_codepoints: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParseMetadataRangeUnits.UNICODE_CODEPOINTS:
            return unicode_codepoints()
