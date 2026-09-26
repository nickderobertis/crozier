

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostV2VectordbCollectionsCreateRequestParams(UniversalBaseModel):
    """
    Extra parameters for the collection.
    """

    max_length: typing.Optional[str] = pydantic.Field(default=None)
    """
    The maximum number of characters in a VarChar field. This parameter is mandatory when the current field type is VarChar.
    """

    enable_dynamic_field: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="enableDynamicField"),
        pydantic.Field(
            alias="enableDynamicField",
            description="Whether to enable the reserved dynamic field. If set to true, non-schema-defined fields are saved in the reserved dynamic field as key-value pairs.",
        ),
    ] = None
    """
    Whether to enable the reserved dynamic field. If set to true, non-schema-defined fields are saved in the reserved dynamic field as key-value pairs.
    """

    shards_num: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="shardsNum"),
        pydantic.Field(
            alias="shardsNum", description="The number of shards to create along with the current collection."
        ),
    ] = None
    """
    The number of shards to create along with the current collection.
    """

    consistency_level: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="consistencyLevel"),
        pydantic.Field(
            alias="consistencyLevel",
            description="The consistency level of the collection. Possible values are __STRONG__, __BOUNDED__, __SESSION__, and __EVENTUALLY__.",
        ),
    ] = None
    """
    The consistency level of the collection. Possible values are __STRONG__, __BOUNDED__, __SESSION__, and __EVENTUALLY__.
    """

    partitions_num: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="partitionsNum"),
        pydantic.Field(
            alias="partitionsNum",
            description="The number of partitions to create along with the current collection. This parameter is mandatory if one field of the collection has been designated as the partition key.",
        ),
    ] = None
    """
    The number of partitions to create along with the current collection. This parameter is mandatory if one field of the collection has been designated as the partition key.
    """

    ttl_seconds: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ttlSeconds"),
        pydantic.Field(
            alias="ttlSeconds",
            description="The time-to-live (TTL) period of the collection. If set, the collection is to be dropped once the period ends.",
        ),
    ] = None
    """
    The time-to-live (TTL) period of the collection. If set, the collection is to be dropped once the period ends.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
