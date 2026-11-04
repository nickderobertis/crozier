

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .schema_node import SchemaNode


class CatalogNode(UniversalBaseModel):
    name: typing.Optional[str] = None
    schemas: typing.Optional[typing.List[SchemaNode]] = None
    total_collections: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalCollections"), pydantic.Field(alias="totalCollections")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
