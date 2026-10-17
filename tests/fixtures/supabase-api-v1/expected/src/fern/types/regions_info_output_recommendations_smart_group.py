

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .regions_info_output_recommendations_smart_group_code import RegionsInfoOutputRecommendationsSmartGroupCode
from .regions_info_output_recommendations_smart_group_type import RegionsInfoOutputRecommendationsSmartGroupType


class RegionsInfoOutputRecommendationsSmartGroup(UniversalBaseModel):
    name: str
    code: RegionsInfoOutputRecommendationsSmartGroupCode
    type: RegionsInfoOutputRecommendationsSmartGroupType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
