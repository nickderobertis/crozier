

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .regions_info_output_all import RegionsInfoOutputAll
from .regions_info_output_recommendations import RegionsInfoOutputRecommendations


class RegionsInfoOutput(UniversalBaseModel):
    recommendations: RegionsInfoOutputRecommendations
    all_: typing_extensions.Annotated[RegionsInfoOutputAll, FieldMetadata(alias="all"), pydantic.Field(alias="all")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
