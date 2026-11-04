

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflow_response_model_schema_amount import WorkflowResponseModelSchemaAmount
from .workflow_response_model_schema_counterparty_name import WorkflowResponseModelSchemaCounterpartyName
from .workflow_response_model_schema_draft import WorkflowResponseModelSchemaDraft
from .workflow_response_model_schema_fee import WorkflowResponseModelSchemaFee
from .workflow_response_model_schema_line_items import WorkflowResponseModelSchemaLineItems


class WorkflowResponseModelSchema(UniversalBaseModel):
    counterparty_name: typing_extensions.Annotated[
        typing.Optional[WorkflowResponseModelSchemaCounterpartyName],
        FieldMetadata(alias="counterpartyName"),
        pydantic.Field(alias="counterpartyName"),
    ] = None
    amount: typing.Optional[WorkflowResponseModelSchemaAmount] = None
    fee: typing.Optional[WorkflowResponseModelSchemaFee] = None
    draft: typing.Optional[WorkflowResponseModelSchemaDraft] = None
    line_items: typing_extensions.Annotated[
        typing.Optional[WorkflowResponseModelSchemaLineItems],
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
