

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .field_mapping_type import FieldMappingType


class GetFieldMappingsResponse(UniversalBaseModel):
    tp_id: typing_extensions.Annotated[str, FieldMetadata(alias="tpId"), pydantic.Field(alias="tpId")]
    mappings: typing.List[FieldMappingType]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
