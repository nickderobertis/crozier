

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entity_schema import EntitySchema


class EntitySchemasPaginatedList(UniversalBaseModel):
    entity_schemas: typing_extensions.Annotated[
        typing.Optional[typing.List[EntitySchema]],
        FieldMetadata(alias="entitySchemas"),
        pydantic.Field(alias="entitySchemas"),
    ] = None
    next_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nextToken"), pydantic.Field(alias="nextToken")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
