

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .collision_details_severity import CollisionDetailsSeverity
from .collision_details_side import CollisionDetailsSide


class CollisionDetails(UniversalBaseModel):
    side: CollisionDetailsSide = pydantic.Field()
    """
    Indicates the side of the collision
    """

    severity: typing.Optional[CollisionDetailsSeverity] = pydantic.Field(default=None)
    """
    Minimal stands for no emergency system activated during the collision. Minor only pretensioner system activated. Major for airbag and prentensioner activation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
