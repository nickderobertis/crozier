

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .word_search_timestamp import WordSearchTimestamp


class WordSearchMatch(UniversalBaseModel):
    text: str = pydantic.Field()
    """
    The matched word
    """

    count: int = pydantic.Field()
    """
    The total amount of times the word is in the transcript
    """

    timestamps: typing.List[WordSearchTimestamp] = pydantic.Field()
    """
    An array of timestamps
    """

    indexes: typing.List[int] = pydantic.Field()
    """
    An array of all index locations for that word within the `words` array of the completed transcript
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
