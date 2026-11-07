

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenizerType(enum.StrEnum):
    """
    Defines tokenizer behavior:
    AsciiAlphabetic
    - Mainly for for benchmark compatibility
    - Only ASCII alphabetic chars are recognized as token.

    UnicodeAlphanumeric
    - All Unicode alphanumeric chars are recognized as token.
    - Allows '+' '-' '#' in middle or end of a token: c++, c#, block-max.

    UnicodeAlphanumericFolded
    - All Unicode alphanumeric chars are recognized as token.
    - Allows '+' '-' '#' in middle or end of a token: c++, c#, block-max.
    - Diacritics, accents, zalgo text, umlaut, bold, italic, full-width UTF-8 characters are converted into its basic representation.
    - Apostroph handling prevents that short term parts preceding or following the apostroph get indexed (e.g. "s" in "someone's").
    - Tokenizing might be slower due to folding and apostroph processing.

    UnicodeAlphanumericZH
    - Implements Chinese word segmentation to segment continuous Chinese text into tokens for indexing and search.
    - Supports mixed Latin and Chinese texts
    - Supports Chinese sentence boundary chars for KWIC snippets ahd highlighting.
    - Requires feature #[cfg(feature = "zh")]
    """

    ASCII_ALPHABETIC = "AsciiAlphabetic"
    UNICODE_ALPHANUMERIC = "UnicodeAlphanumeric"
    UNICODE_ALPHANUMERIC_FOLDED = "UnicodeAlphanumericFolded"
    WHITESPACE = "Whitespace"
    WHITESPACE_LOWERCASE = "WhitespaceLowercase"
    UNICODE_ALPHANUMERIC_ZH = "UnicodeAlphanumericZH"

    def visit(
        self,
        ascii_alphabetic: typing.Callable[[], T_Result],
        unicode_alphanumeric: typing.Callable[[], T_Result],
        unicode_alphanumeric_folded: typing.Callable[[], T_Result],
        whitespace: typing.Callable[[], T_Result],
        whitespace_lowercase: typing.Callable[[], T_Result],
        unicode_alphanumeric_zh: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TokenizerType.ASCII_ALPHABETIC:
            return ascii_alphabetic()
        if self is TokenizerType.UNICODE_ALPHANUMERIC:
            return unicode_alphanumeric()
        if self is TokenizerType.UNICODE_ALPHANUMERIC_FOLDED:
            return unicode_alphanumeric_folded()
        if self is TokenizerType.WHITESPACE:
            return whitespace()
        if self is TokenizerType.WHITESPACE_LOWERCASE:
            return whitespace_lowercase()
        if self is TokenizerType.UNICODE_ALPHANUMERIC_ZH:
            return unicode_alphanumeric_zh()
