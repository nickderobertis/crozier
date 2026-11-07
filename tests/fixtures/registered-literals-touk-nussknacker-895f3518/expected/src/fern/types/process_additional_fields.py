

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .map_string import MapString


class ProcessAdditionalFields(UniversalBaseModel):
    description: typing.Optional[str] = None
    properties: MapString
    meta_data_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="metaDataType"), pydantic.Field(alias="metaDataType")
    ]
    show_description: typing_extensions.Annotated[
        bool, FieldMetadata(alias="showDescription"), pydantic.Field(alias="showDescription")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
