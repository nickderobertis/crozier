

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lighting_base_light_item import LightingBaseLightItem
from .lighting_base_turn_item import LightingBaseTurnItem


class LightingBase(UniversalBaseModel):
    """
    Depricated lighting system model. Use LightingSystem instead.
    """

    turn: typing.Optional[typing.List[LightingBaseTurnItem]] = None
    light: typing.Optional[typing.List[LightingBaseLightItem]] = None
    status: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
