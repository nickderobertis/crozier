

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_v2vectordb_collections_create_request_schema_fields_item import (
    PostV2VectordbCollectionsCreateRequestSchemaFieldsItem,
)


class PostV2VectordbCollectionsCreateRequestSchema(UniversalBaseModel):
    """
    The schema is responsible for organizing data in the target collection. A valid schema should have multiple fields, which must include a primary key, a vector field, and several scalar fields.
    """

    auto_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="autoId"),
        pydantic.Field(
            alias="autoId",
            description="Whether allows the primary field to automatically increment. Setting this to True makes the primary field automatically increment. In this case, the primary field should not be included in the data to insert to avoid errors. Set this parameter in the field with is_primary set to True.",
        ),
    ]
    """
    Whether allows the primary field to automatically increment. Setting this to True makes the primary field automatically increment. In this case, the primary field should not be included in the data to insert to avoid errors. Set this parameter in the field with is_primary set to True.
    """

    enable_dynamic_field: typing_extensions.Annotated[
        str, FieldMetadata(alias="enableDynamicField"), pydantic.Field(alias="enableDynamicField")
    ]
    fields: typing.List[PostV2VectordbCollectionsCreateRequestSchemaFieldsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
