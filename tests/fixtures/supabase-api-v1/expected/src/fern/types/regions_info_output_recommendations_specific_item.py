

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .regions_info_output_recommendations_specific_item_code import RegionsInfoOutputRecommendationsSpecificItemCode
from .regions_info_output_recommendations_specific_item_provider import (
    RegionsInfoOutputRecommendationsSpecificItemProvider,
)
from .regions_info_output_recommendations_specific_item_status import RegionsInfoOutputRecommendationsSpecificItemStatus
from .regions_info_output_recommendations_specific_item_type import RegionsInfoOutputRecommendationsSpecificItemType


class RegionsInfoOutputRecommendationsSpecificItem(UniversalBaseModel):
    name: str
    code: RegionsInfoOutputRecommendationsSpecificItemCode
    type: RegionsInfoOutputRecommendationsSpecificItemType
    provider: RegionsInfoOutputRecommendationsSpecificItemProvider
    status: typing.Optional[RegionsInfoOutputRecommendationsSpecificItemStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
