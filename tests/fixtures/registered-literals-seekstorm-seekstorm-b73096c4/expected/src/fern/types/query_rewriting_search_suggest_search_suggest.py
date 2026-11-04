

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class QueryRewritingSearchSuggestSearchSuggest(UniversalBaseModel):
    """
    Query rewriting disabled, returns query results for original query string, returns suggestions for corrected or completed query.
    Additional latency for spelling suggestions.
    """

    correct: typing.Optional[int] = pydantic.Field(default=None)
    """
    Enable query correction, for queries with query string length >= threshold
    A minimum length of 2 is advised to prevent irrelevant suggestions and results.
    """

    distance: int = pydantic.Field()
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

    complete: typing.Optional[int] = pydantic.Field(default=None)
    """
    Enable query completions, for queries with query string length >= threshold, in addition to spelling corrections
    A minimum length of 2 is advised to prevent irrelevant suggestions and results.
    """

    length: typing.Optional[int] = pydantic.Field(default=None)
    """
    An option to limit maximum number of returned suggestions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
