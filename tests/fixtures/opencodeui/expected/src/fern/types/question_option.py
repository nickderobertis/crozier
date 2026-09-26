

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class QuestionOption(UniversalBaseModel):
    label: str = pydantic.Field()
    """
    Display text (1-5 words, concise)
    """

    description: str = pydantic.Field()
    """
    Explanation of choice
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
