

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostV2VectordbCollectionsDescribeResponseDataFieldsItem(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    The name of the current field.
    """

    type: str = pydantic.Field()
    """
    The data type of the field.
    """

    description: str = pydantic.Field()
    """
    The description of the field.
    """

    auto_id: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="autoId"),
        pydantic.Field(alias="autoId", description="Whether this field automatically increments its value."),
    ]
    """
    Whether this field automatically increments its value.
    """

    partition_key: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="partitionKey"),
        pydantic.Field(alias="partitionKey", description="Whether this field serves as a partition key."),
    ]
    """
    Whether this field serves as a partition key.
    """

    primary_key: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="primaryKey"),
        pydantic.Field(alias="primaryKey", description="Whether this field serves as the primary key."),
    ]
    """
    Whether this field serves as the primary key.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
