

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2ExtractMetadataRangeUnits(enum.StrEnum):
    """
    Units of every `range` offset in the response. Always `"unicode_codepoints"` (Unicode code points into `markdown`). Declared explicitly so consumers know how to slice the string — e.g. JavaScript strings are UTF-16, so a naive `.slice()` drifts when the markdown contains astral characters.
    """

    UNICODE_CODEPOINTS = "unicode_codepoints"

    def visit(self, unicode_codepoints: typing.Callable[[], T_Result]) -> T_Result:
        if self is V2ExtractMetadataRangeUnits.UNICODE_CODEPOINTS:
            return unicode_codepoints()
