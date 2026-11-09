

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .timestamp import Timestamp


class AutoHighlightResult(UniversalBaseModel):
    count: int = pydantic.Field()
    """
    The total number of times the key phrase appears in the audio file
    """

    rank: float = pydantic.Field()
    """
    The total relevancy to the overall audio file of this key phrase - a greater number means more relevant
    """

    text: str = pydantic.Field()
    """
    The text itself of the key phrase
    """

    timestamps: typing.List[Timestamp] = pydantic.Field()
    """
    The timestamp of the of the key phrase
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
