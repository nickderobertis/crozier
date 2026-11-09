

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .table_config_dto import TableConfigDto


class SchemaConfigDto(UniversalBaseModel):
    id: typing.Optional[str] = None
    schema_name: typing_extensions.Annotated[str, FieldMetadata(alias="schemaName"), pydantic.Field(alias="schemaName")]
    tables: typing.List[TableConfigDto]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
