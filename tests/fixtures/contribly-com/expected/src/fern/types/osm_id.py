

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OsmId(UniversalBaseModel):
    osm_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="osmId"), pydantic.Field(alias="osmId")
    ] = None
    osm_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="osmType"), pydantic.Field(alias="osmType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
