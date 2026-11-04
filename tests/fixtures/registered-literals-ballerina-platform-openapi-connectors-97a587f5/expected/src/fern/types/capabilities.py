

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scale_type import ScaleType


class Capabilities(UniversalBaseModel):
    """
    The capabilities of a base or fine tune model.
    """

    fine_tune: bool = pydantic.Field()
    """
    A value indicating whether a model can be used for fine tuning.
    """

    inference: bool = pydantic.Field()
    """
    A value indicating whether a model can be deployed.
    """

    completion: bool = pydantic.Field()
    """
    A value indicating whether a model supports completion.
    """

    embeddings: bool = pydantic.Field()
    """
    A value indicating whether a model supports embeddings.
    """

    scale_types: typing.List[ScaleType] = pydantic.Field()
    """
    The supported scale types for deployments of this model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
