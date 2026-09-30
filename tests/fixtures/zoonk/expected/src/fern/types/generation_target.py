

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .generation_target_type import GenerationTargetType


class GenerationTarget(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Course prompt, chapter, or lesson ID to generate
    """

    type: GenerationTargetType = pydantic.Field()
    """
    Resource type to generate
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
