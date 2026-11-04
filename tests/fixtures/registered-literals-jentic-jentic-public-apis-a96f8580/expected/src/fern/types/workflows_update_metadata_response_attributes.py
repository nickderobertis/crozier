

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflows_update_metadata_response_attributes_draft_item import WorkflowsUpdateMetadataResponseAttributesDraftItem
from .workflows_update_metadata_response_attributes_fee import WorkflowsUpdateMetadataResponseAttributesFee


class WorkflowsUpdateMetadataResponseAttributes(UniversalBaseModel):
    counterparty_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="counterpartyName"), pydantic.Field(alias="counterpartyName")
    ] = None
    amount: typing.Optional[int] = None
    fee: typing.Optional[WorkflowsUpdateMetadataResponseAttributesFee] = None
    draft: typing.Optional[typing.List[WorkflowsUpdateMetadataResponseAttributesDraftItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
