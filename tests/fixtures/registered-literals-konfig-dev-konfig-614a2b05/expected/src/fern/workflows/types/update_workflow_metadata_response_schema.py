

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_workflow_metadata_response_schema_amount import UpdateWorkflowMetadataResponseSchemaAmount
from .update_workflow_metadata_response_schema_counterparty_name import (
    UpdateWorkflowMetadataResponseSchemaCounterpartyName,
)
from .update_workflow_metadata_response_schema_draft import UpdateWorkflowMetadataResponseSchemaDraft
from .update_workflow_metadata_response_schema_fee import UpdateWorkflowMetadataResponseSchemaFee
from .update_workflow_metadata_response_schema_line_items import UpdateWorkflowMetadataResponseSchemaLineItems


class UpdateWorkflowMetadataResponseSchema(UniversalBaseModel):
    counterparty_name: typing_extensions.Annotated[
        typing.Optional[UpdateWorkflowMetadataResponseSchemaCounterpartyName],
        FieldMetadata(alias="counterpartyName"),
        pydantic.Field(alias="counterpartyName"),
    ] = None
    amount: typing.Optional[UpdateWorkflowMetadataResponseSchemaAmount] = None
    fee: typing.Optional[UpdateWorkflowMetadataResponseSchemaFee] = None
    draft: typing.Optional[UpdateWorkflowMetadataResponseSchemaDraft] = None
    line_items: typing_extensions.Annotated[
        typing.Optional[UpdateWorkflowMetadataResponseSchemaLineItems],
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
