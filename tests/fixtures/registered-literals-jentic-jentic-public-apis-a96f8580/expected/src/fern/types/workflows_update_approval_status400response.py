

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workflows_update_approval_status400response_message import WorkflowsUpdateApprovalStatus400ResponseMessage


class WorkflowsUpdateApprovalStatus400Response(UniversalBaseModel):
    code: typing.Optional[str] = None
    message: typing.Optional[WorkflowsUpdateApprovalStatus400ResponseMessage] = None
    param: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
