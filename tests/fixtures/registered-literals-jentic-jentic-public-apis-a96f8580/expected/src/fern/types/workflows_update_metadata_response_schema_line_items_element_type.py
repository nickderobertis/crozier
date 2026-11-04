

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflows_update_metadata_response_schema_line_items_element_type_schema import (
    WorkflowsUpdateMetadataResponseSchemaLineItemsElementTypeSchema,
)


class WorkflowsUpdateMetadataResponseSchemaLineItemsElementType(UniversalBaseModel):
    type: typing.Optional[str] = None
    display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[WorkflowsUpdateMetadataResponseSchemaLineItemsElementTypeSchema],
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
