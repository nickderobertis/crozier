

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .battles_list_response_dto_output_battles_item import BattlesListResponseDtoOutputBattlesItem
from .battles_list_response_dto_output_meta import BattlesListResponseDtoOutputMeta
from .battles_list_response_dto_output_pagination import BattlesListResponseDtoOutputPagination


class BattlesListResponseDtoOutput(UniversalBaseModel):
    battles: typing.List[BattlesListResponseDtoOutputBattlesItem]
    pagination: BattlesListResponseDtoOutputPagination
    meta: BattlesListResponseDtoOutputMeta

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
