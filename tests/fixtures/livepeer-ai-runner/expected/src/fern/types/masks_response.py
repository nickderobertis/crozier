

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MasksResponse(UniversalBaseModel):
    """
    Response model for object segmentation.
    """

    masks: str = pydantic.Field()
    """
    The generated masks.
    """

    scores: str = pydantic.Field()
    """
    The model's confidence scores for each generated mask.
    """

    logits: str = pydantic.Field()
    """
    The raw, unnormalized predictions (logits) for the masks.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
