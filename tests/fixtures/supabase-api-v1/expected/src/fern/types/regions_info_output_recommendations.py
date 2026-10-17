

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .regions_info_output_recommendations_smart_group import RegionsInfoOutputRecommendationsSmartGroup
from .regions_info_output_recommendations_specific_item import RegionsInfoOutputRecommendationsSpecificItem


class RegionsInfoOutputRecommendations(UniversalBaseModel):
    smart_group: typing_extensions.Annotated[
        RegionsInfoOutputRecommendationsSmartGroup,
        FieldMetadata(alias="smartGroup"),
        pydantic.Field(alias="smartGroup"),
    ]
    specific: typing.List[RegionsInfoOutputRecommendationsSpecificItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
