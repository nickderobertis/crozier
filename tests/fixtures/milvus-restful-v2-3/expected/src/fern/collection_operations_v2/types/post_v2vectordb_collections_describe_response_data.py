

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_v2vectordb_collections_describe_response_data_fields_item import (
    PostV2VectordbCollectionsDescribeResponseDataFieldsItem,
)
from .post_v2vectordb_collections_describe_response_data_indexes_item import (
    PostV2VectordbCollectionsDescribeResponseDataIndexesItem,
)


class PostV2VectordbCollectionsDescribeResponseData(UniversalBaseModel):
    collection_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="collectionName"),
        pydantic.Field(alias="collectionName", description="The name of the current collection."),
    ]
    """
    The name of the current collection.
    """

    auto_id: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="autoID"),
        pydantic.Field(
            alias="autoID", description="Whether the primary key of this collection automatically increments."
        ),
    ]
    """
    Whether the primary key of this collection automatically increments.
    """

    description: str = pydantic.Field()
    """
    The description of the collection.
    """

    enable_dynamic_field: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="enableDynamicField"),
        pydantic.Field(
            alias="enableDynamicField",
            description="Whether the reserved dynamic field named $meta is enabled to save non-schema-defined fields and their values in key-value pairs.",
        ),
    ]
    """
    Whether the reserved dynamic field named $meta is enabled to save non-schema-defined fields and their values in key-value pairs.
    """

    fields: typing.List[PostV2VectordbCollectionsDescribeResponseDataFieldsItem] = pydantic.Field()
    """
    The collection fields in an array
    """

    indexes: typing.List[PostV2VectordbCollectionsDescribeResponseDataIndexesItem] = pydantic.Field()
    """
    The created indexes in an array
    """

    load: str = pydantic.Field()
    """
    The load status of the current collection.
    """

    shards_num: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="shardsNum"),
        pydantic.Field(alias="shardsNum", description="The number of shards created along with the collection."),
    ]
    """
    The number of shards created along with the collection.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
