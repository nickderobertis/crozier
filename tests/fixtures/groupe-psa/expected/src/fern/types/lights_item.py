

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lights_item_direction import LightsItemDirection
from .lights_item_position import LightsItemPosition


class LightsItem(UniversalBaseModel):
    direction: typing.Optional[LightsItemDirection] = None
    position: typing.Optional[LightsItemPosition] = None
    status: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
