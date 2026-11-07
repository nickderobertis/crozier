

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflows_update_metadata_response_schema_line_items_element_type_schema_another_child_attribute import (
    WorkflowsUpdateMetadataResponseSchemaLineItemsElementTypeSchemaAnotherChildAttribute,
)
from .workflows_update_metadata_response_schema_line_items_element_type_schema_child_attribute import (
    WorkflowsUpdateMetadataResponseSchemaLineItemsElementTypeSchemaChildAttribute,
)


class WorkflowsUpdateMetadataResponseSchemaLineItemsElementTypeSchema(UniversalBaseModel):
    child_attribute: typing_extensions.Annotated[
        typing.Optional[WorkflowsUpdateMetadataResponseSchemaLineItemsElementTypeSchemaChildAttribute],
        FieldMetadata(alias="childAttribute"),
        pydantic.Field(alias="childAttribute"),
    ] = None
    another_child_attribute: typing_extensions.Annotated[
        typing.Optional[WorkflowsUpdateMetadataResponseSchemaLineItemsElementTypeSchemaAnotherChildAttribute],
        FieldMetadata(alias="anotherChildAttribute"),
        pydantic.Field(alias="anotherChildAttribute"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
