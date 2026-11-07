

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflows_list_all_workflow_schemas_response_list_item_schema_amount import (
    WorkflowsListAllWorkflowSchemasResponseListItemSchemaAmount,
)
from .workflows_list_all_workflow_schemas_response_list_item_schema_counterparty_name import (
    WorkflowsListAllWorkflowSchemasResponseListItemSchemaCounterpartyName,
)
from .workflows_list_all_workflow_schemas_response_list_item_schema_draft import (
    WorkflowsListAllWorkflowSchemasResponseListItemSchemaDraft,
)
from .workflows_list_all_workflow_schemas_response_list_item_schema_fee import (
    WorkflowsListAllWorkflowSchemasResponseListItemSchemaFee,
)
from .workflows_list_all_workflow_schemas_response_list_item_schema_line_items import (
    WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItems,
)


class WorkflowsListAllWorkflowSchemasResponseListItemSchema(UniversalBaseModel):
    counterparty_name: typing_extensions.Annotated[
        typing.Optional[WorkflowsListAllWorkflowSchemasResponseListItemSchemaCounterpartyName],
        FieldMetadata(alias="counterpartyName"),
        pydantic.Field(alias="counterpartyName"),
    ] = None
    amount: typing.Optional[WorkflowsListAllWorkflowSchemasResponseListItemSchemaAmount] = None
    fee: typing.Optional[WorkflowsListAllWorkflowSchemasResponseListItemSchemaFee] = None
    draft: typing.Optional[WorkflowsListAllWorkflowSchemasResponseListItemSchemaDraft] = None
    line_items: typing_extensions.Annotated[
        typing.Optional[WorkflowsListAllWorkflowSchemasResponseListItemSchemaLineItems],
        FieldMetadata(alias="lineItems"),
        pydantic.Field(alias="lineItems"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
