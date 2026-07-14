

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_reference import ApiReference


class Damage(UniversalBaseModel):
    """
    `Damage`
    """

    damage_dice: typing.Optional[str] = None
    damage_type: typing.Optional[ApiReference] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
