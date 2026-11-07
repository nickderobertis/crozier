

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflows_get_workflow_schema_response_schema_amount import WorkflowsGetWorkflowSchemaResponseSchemaAmount
from .workflows_get_workflow_schema_response_schema_counterparty_name import (
    WorkflowsGetWorkflowSchemaResponseSchemaCounterpartyName,
)
from .workflows_get_workflow_schema_response_schema_draft import WorkflowsGetWorkflowSchemaResponseSchemaDraft
from .workflows_get_workflow_schema_response_schema_fee import WorkflowsGetWorkflowSchemaResponseSchemaFee
from .workflows_get_workflow_schema_response_schema_line_items import WorkflowsGetWorkflowSchemaResponseSchemaLineItems


class WorkflowsGetWorkflowSchemaResponseSchema(UniversalBaseModel):
    counterparty_name: typing_extensions.Annotated[
        typing.Optional[WorkflowsGetWorkflowSchemaResponseSchemaCounterpartyName],
        FieldMetadata(alias="counterpartyName"),
        pydantic.Field(alias="counterpartyName"),
    ] = None
    amount: typing.Optional[WorkflowsGetWorkflowSchemaResponseSchemaAmount] = None
    fee: typing.Optional[WorkflowsGetWorkflowSchemaResponseSchemaFee] = None
    draft: typing.Optional[WorkflowsGetWorkflowSchemaResponseSchemaDraft] = None
    line_items: typing_extensions.Annotated[
        typing.Optional[WorkflowsGetWorkflowSchemaResponseSchemaLineItems],
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
