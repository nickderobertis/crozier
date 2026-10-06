

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .battle_warriors_search_response_dto_output_warriors_item import BattleWarriorsSearchResponseDtoOutputWarriorsItem


class BattleWarriorsSearchResponseDtoOutput(UniversalBaseModel):
    warriors: typing.List[BattleWarriorsSearchResponseDtoOutputWarriorsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
