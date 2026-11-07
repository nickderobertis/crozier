

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .retrieve_a_workflow_schema_response_schema_amount import RetrieveAWorkflowSchemaResponseSchemaAmount
from .retrieve_a_workflow_schema_response_schema_counterparty_name import (
    RetrieveAWorkflowSchemaResponseSchemaCounterpartyName,
)
from .retrieve_a_workflow_schema_response_schema_draft import RetrieveAWorkflowSchemaResponseSchemaDraft
from .retrieve_a_workflow_schema_response_schema_fee import RetrieveAWorkflowSchemaResponseSchemaFee
from .retrieve_a_workflow_schema_response_schema_line_items import RetrieveAWorkflowSchemaResponseSchemaLineItems


class RetrieveAWorkflowSchemaResponseSchema(UniversalBaseModel):
    counterparty_name: typing_extensions.Annotated[
        typing.Optional[RetrieveAWorkflowSchemaResponseSchemaCounterpartyName],
        FieldMetadata(alias="counterpartyName"),
        pydantic.Field(alias="counterpartyName"),
    ] = None
    amount: typing.Optional[RetrieveAWorkflowSchemaResponseSchemaAmount] = None
    fee: typing.Optional[RetrieveAWorkflowSchemaResponseSchemaFee] = None
    draft: typing.Optional[RetrieveAWorkflowSchemaResponseSchemaDraft] = None
    line_items: typing_extensions.Annotated[
        typing.Optional[RetrieveAWorkflowSchemaResponseSchemaLineItems],
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
