

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FilterSchemasDto(UniversalBaseModel):
    schema_id1: typing_extensions.Annotated[str, FieldMetadata(alias="schemaId1"), pydantic.Field(alias="schemaId1")]
    schema_id2: typing_extensions.Annotated[str, FieldMetadata(alias="schemaId2"), pydantic.Field(alias="schemaId2")]
    id_lvl: typing_extensions.Annotated[float, FieldMetadata(alias="idLvl"), pydantic.Field(alias="idLvl")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
