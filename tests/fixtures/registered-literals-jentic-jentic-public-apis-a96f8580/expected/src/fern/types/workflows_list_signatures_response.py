

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflows_list_signatures_response_signers_item import WorkflowsListSignaturesResponseSignersItem


class WorkflowsListSignaturesResponse(UniversalBaseModel):
    title: typing.Optional[str] = None
    workflow_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="workflowId"), pydantic.Field(alias="workflowId")
    ] = None
    signers: typing.Optional[typing.List[WorkflowsListSignaturesResponseSignersItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
