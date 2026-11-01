

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .track_metadata_meta_data import TrackMetadataMetaData


class TrackMetadata(UniversalBaseModel):
    meta_data: typing_extensions.Annotated[
        typing.Optional[TrackMetadataMetaData], FieldMetadata(alias="metaData"), pydantic.Field(alias="metaData")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
