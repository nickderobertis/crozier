

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .collection_schema_fields_item_element_type_params import CollectionSchemaFieldsItemElementTypeParams


class CollectionSchemaFieldsItem(UniversalBaseModel):
    """
    The name of the field to create in the target collection
    """

    field_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fieldName"),
        pydantic.Field(alias="fieldName", description="The name of the field to create in the target collection"),
    ]
    """
    The name of the field to create in the target collection
    """

    data_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="dataType"),
        pydantic.Field(alias="dataType", description="The data type of the field values."),
    ]
    """
    The data type of the field values.
    """

    element_data_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="elementDataType"),
        pydantic.Field(alias="elementDataType", description="The data type of the elements in an array field."),
    ] = None
    """
    The data type of the elements in an array field.
    """

    is_primary: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isPrimary"),
        pydantic.Field(
            alias="isPrimary",
            description="Whether the current field is the primary field. Setting this to True makes the current field the primary field.",
        ),
    ] = None
    """
    Whether the current field is the primary field. Setting this to True makes the current field the primary field.
    """

    is_partition_key: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isPartitionKey"),
        pydantic.Field(
            alias="isPartitionKey",
            description="Whether the current field serves as the partition key. Setting this to True makes the current field serve as the partition key. In this case, MilvusZilliz Cloud manages all partitions in the current collection.",
        ),
    ] = None
    """
    Whether the current field serves as the partition key. Setting this to True makes the current field serve as the partition key. In this case, MilvusZilliz Cloud manages all partitions in the current collection.
    """

    element_type_params: typing_extensions.Annotated[
        typing.Optional[CollectionSchemaFieldsItemElementTypeParams],
        FieldMetadata(alias="elementTypeParams"),
        pydantic.Field(alias="elementTypeParams", description="Extra field parameters."),
    ] = None
    """
    Extra field parameters.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
