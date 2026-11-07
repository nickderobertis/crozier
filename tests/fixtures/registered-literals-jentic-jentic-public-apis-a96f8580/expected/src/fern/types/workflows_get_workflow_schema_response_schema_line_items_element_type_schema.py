

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflows_get_workflow_schema_response_schema_line_items_element_type_schema_another_child_attribute import (
    WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementTypeSchemaAnotherChildAttribute,
)
from .workflows_get_workflow_schema_response_schema_line_items_element_type_schema_child_attribute import (
    WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementTypeSchemaChildAttribute,
)


class WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementTypeSchema(UniversalBaseModel):
    child_attribute: typing_extensions.Annotated[
        typing.Optional[WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementTypeSchemaChildAttribute],
        FieldMetadata(alias="childAttribute"),
        pydantic.Field(alias="childAttribute"),
    ] = None
    another_child_attribute: typing_extensions.Annotated[
        typing.Optional[WorkflowsGetWorkflowSchemaResponseSchemaLineItemsElementTypeSchemaAnotherChildAttribute],
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
