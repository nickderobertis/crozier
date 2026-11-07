

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflows_update_metadata_response_schema_amount import WorkflowsUpdateMetadataResponseSchemaAmount
from .workflows_update_metadata_response_schema_counterparty_name import (
    WorkflowsUpdateMetadataResponseSchemaCounterpartyName,
)
from .workflows_update_metadata_response_schema_draft import WorkflowsUpdateMetadataResponseSchemaDraft
from .workflows_update_metadata_response_schema_fee import WorkflowsUpdateMetadataResponseSchemaFee
from .workflows_update_metadata_response_schema_line_items import WorkflowsUpdateMetadataResponseSchemaLineItems


class WorkflowsUpdateMetadataResponseSchema(UniversalBaseModel):
    counterparty_name: typing_extensions.Annotated[
        typing.Optional[WorkflowsUpdateMetadataResponseSchemaCounterpartyName],
        FieldMetadata(alias="counterpartyName"),
        pydantic.Field(alias="counterpartyName"),
    ] = None
    amount: typing.Optional[WorkflowsUpdateMetadataResponseSchemaAmount] = None
    fee: typing.Optional[WorkflowsUpdateMetadataResponseSchemaFee] = None
    draft: typing.Optional[WorkflowsUpdateMetadataResponseSchemaDraft] = None
    line_items: typing_extensions.Annotated[
        typing.Optional[WorkflowsUpdateMetadataResponseSchemaLineItems],
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
