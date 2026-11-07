

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .schema_entity import SchemaEntity


class SchemaTags(UniversalBaseModel):
    schema_entity: typing_extensions.Annotated[
        typing.Optional[SchemaEntity], FieldMetadata(alias="schemaEntity"), pydantic.Field(alias="schemaEntity")
    ] = None
    tags: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
