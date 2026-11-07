

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_all_workflow_schemas_response_list_item_schema_line_items_element_type_schema import (
    ListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchema,
)


class ListAllWorkflowSchemasResponseListItemSchemaLineItemsElementType(UniversalBaseModel):
    type: typing.Optional[str] = None
    display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[ListAllWorkflowSchemasResponseListItemSchemaLineItemsElementTypeSchema],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
