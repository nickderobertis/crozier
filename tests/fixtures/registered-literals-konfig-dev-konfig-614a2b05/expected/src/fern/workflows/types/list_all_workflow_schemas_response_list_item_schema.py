

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_all_workflow_schemas_response_list_item_schema_amount import (
    ListAllWorkflowSchemasResponseListItemSchemaAmount,
)
from .list_all_workflow_schemas_response_list_item_schema_counterparty_name import (
    ListAllWorkflowSchemasResponseListItemSchemaCounterpartyName,
)
from .list_all_workflow_schemas_response_list_item_schema_draft import ListAllWorkflowSchemasResponseListItemSchemaDraft
from .list_all_workflow_schemas_response_list_item_schema_fee import ListAllWorkflowSchemasResponseListItemSchemaFee
from .list_all_workflow_schemas_response_list_item_schema_line_items import (
    ListAllWorkflowSchemasResponseListItemSchemaLineItems,
)


class ListAllWorkflowSchemasResponseListItemSchema(UniversalBaseModel):
    counterparty_name: typing_extensions.Annotated[
        typing.Optional[ListAllWorkflowSchemasResponseListItemSchemaCounterpartyName],
        FieldMetadata(alias="counterpartyName"),
        pydantic.Field(alias="counterpartyName"),
    ] = None
    amount: typing.Optional[ListAllWorkflowSchemasResponseListItemSchemaAmount] = None
    fee: typing.Optional[ListAllWorkflowSchemasResponseListItemSchemaFee] = None
    draft: typing.Optional[ListAllWorkflowSchemasResponseListItemSchemaDraft] = None
    line_items: typing_extensions.Annotated[
        typing.Optional[ListAllWorkflowSchemasResponseListItemSchemaLineItems],
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
