

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .word_search_match import WordSearchMatch


class WordSearchResponse(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The ID of the transcript
    """

    total_count: int = pydantic.Field()
    """
    The total count of all matched instances. For e.g., word 1 matched 2 times, and word 2 matched 3 times, `total_count` will equal 5.
    """

    matches: typing.List[WordSearchMatch] = pydantic.Field()
    """
    The matches of the search
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
