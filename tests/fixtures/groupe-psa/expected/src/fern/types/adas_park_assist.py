

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .adas_park_assist_front_item import AdasParkAssistFrontItem
from .adas_park_assist_rear_item import AdasParkAssistRearItem


class AdasParkAssist(UniversalBaseModel):
    front: typing.Optional[typing.List[AdasParkAssistFrontItem]] = None
    rear: typing.Optional[typing.List[AdasParkAssistRearItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
