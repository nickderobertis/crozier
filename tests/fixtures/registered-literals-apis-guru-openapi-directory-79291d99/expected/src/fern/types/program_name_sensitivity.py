

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProgramNameSensitivity(enum.StrEnum):
    """
    The valid name matching sensitivity configurations for a screening program. Note that while certain matching techniques may be more prevalent on less strict settings, all matching algorithms are enabled for every sensitivity.

    `coarse` - See more potential matches. This sensitivity will see more broad phonetic matches across alphabets that make missing a potential hit very unlikely. This setting is noisier and will require more manual review.

    `balanced` - A good default for most companies. This sensitivity is balanced to show high quality hits with reduced noise.

    `strict` - Aggressive false positive reduction. This sensitivity will require names to be more similar than `coarse` and `balanced` settings, relying less on phonetics, while still accounting for character transpositions, missing tokens, and other common permutations.

    `exact` - Matches must be nearly exact. This sensitivity will only show hits with exact or nearly exact name matches with only basic correction such as extraneous symbols and capitalization. This setting is generally not recommended unless you have a very specific use case.
    """

    COARSE = "coarse"
    BALANCED = "balanced"
    STRICT = "strict"
    EXACT = "exact"

    def visit(
        self,
        coarse: typing.Callable[[], T_Result],
        balanced: typing.Callable[[], T_Result],
        strict: typing.Callable[[], T_Result],
        exact: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProgramNameSensitivity.COARSE:
            return coarse()
        if self is ProgramNameSensitivity.BALANCED:
            return balanced()
        if self is ProgramNameSensitivity.STRICT:
            return strict()
        if self is ProgramNameSensitivity.EXACT:
            return exact()
