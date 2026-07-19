

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SummarizedReasoningContentPart(UniversalBaseModel):
    index: int = pydantic.Field()
    """
    The index of the summary part.
    """

    text: str = pydantic.Field()
    """
    The text of the summary part.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
