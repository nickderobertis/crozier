

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .field_config_dto import FieldConfigDto


class TableConfigDto(UniversalBaseModel):
    table_name: typing_extensions.Annotated[str, FieldMetadata(alias="tableName"), pydantic.Field(alias="tableName")]
    metadata_class_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="metadataClassId"), pydantic.Field(alias="metadataClassId")
    ]
    uniformed_path: typing_extensions.Annotated[
        str, FieldMetadata(alias="uniformedPath"), pydantic.Field(alias="uniformedPath")
    ]
    fields: typing.List[FieldConfigDto]
    hidden: bool
    model_update_date: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="modelUpdateDate"), pydantic.Field(alias="modelUpdateDate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
