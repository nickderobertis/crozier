

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SpellingCorrection(UniversalBaseModel):
    """
    Defines spelling correction (fuzzy search) and dictionary generation settings for an index.
    """

    max_dictionary_edit_distance: int = pydantic.Field()
    """
    The edit distance thresholds for suggestions: 1..2 recommended; higher values increase latency and memory consumption.
    """

    term_length_threshold: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Term length thresholds for each edit distance.
      None:    max_dictionary_edit_distance for all terms lengths
      Some(\\[4\\]):    max_dictionary_edit_distance for all terms lengths >= 4,
      Some(\\[2,8\\]):    max_dictionary_edit_distance for all terms lengths >=2, max_dictionary_edit_distance +1 for all terms for lengths>=8
    """

    count_threshold: int = pydantic.Field()
    """
    The minimum frequency count for dictionary words to be considered eligible for spelling correction.
    Depends on the corpus size, 1..20 recommended.
    If count_threshold is too high, some correct words might be missed from the dictionary and deemed misspelled,
    if count_threshold is too low, some misspelled words from the corpus might be considered correct and added to the dictionary.
    Dictionary terms eligible for spelling correction (frequency count >= count_threshold) consume much more RAM, than the candidates (frequency count < count_threshold),
    but the terms below count_threshold will be included in dictionary.csv too.
    """

    max_dictionary_entries: int = pydantic.Field()
    """
    Limits the maximum number of dictionary entries (terms >= count_threshold) to generate during indexing, preventing excessive RAM consumption.
    The number of terms in dictionary.csv will be higher, because it contains also the terms < count_threshold, to become eligible in the future during incremental dictionary updates.
    Dictionary terms eligible for spelling correction (frequency count >= count_threshold) consume much more RAM, than the candidates (frequency count < count_threshold).
    ⚠️ Above this threshold no new terms are added to the dictionary, causing them to be deemed incorrect during spelling correction and possibly changed to similar terms that are in the dictionary.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
