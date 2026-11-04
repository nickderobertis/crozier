

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_workflow_metadata_response_schema_line_items_element_type import (
    UpdateWorkflowMetadataResponseSchemaLineItemsElementType,
)


class UpdateWorkflowMetadataResponseSchemaLineItems(UniversalBaseModel):
    type: typing.Optional[str] = None
    element_type: typing_extensions.Annotated[
        typing.Optional[UpdateWorkflowMetadataResponseSchemaLineItemsElementType],
        FieldMetadata(alias="elementType"),
        pydantic.Field(alias="elementType"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
