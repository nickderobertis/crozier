

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .road_section_id import RoadSectionId


class RoadSectionRestriction(UniversalBaseModel):
    road_section_id: typing_extensions.Annotated[
        typing.Optional[RoadSectionId], FieldMetadata(alias="roadSectionId"), pydantic.Field(alias="roadSectionId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
