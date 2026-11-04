

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflow_response_model_attributes_draft_item import WorkflowResponseModelAttributesDraftItem
from .workflow_response_model_attributes_fee import WorkflowResponseModelAttributesFee


class WorkflowResponseModelAttributes(UniversalBaseModel):
    counterparty_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="counterpartyName"), pydantic.Field(alias="counterpartyName")
    ] = None
    amount: typing.Optional[int] = None
    fee: typing.Optional[WorkflowResponseModelAttributesFee] = None
    draft: typing.Optional[typing.List[WorkflowResponseModelAttributesDraftItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
