

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .collection_node import CollectionNode


class SchemaNode(UniversalBaseModel):
    name: typing.Optional[str] = None
    collections: typing.Optional[typing.List[CollectionNode]] = None
    collection_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="collectionCount"), pydantic.Field(alias="collectionCount")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
