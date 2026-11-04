

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workflows_revert_to_review_response_code import WorkflowsRevertToReviewResponseCode
from .workflows_revert_to_review_response_message import WorkflowsRevertToReviewResponseMessage


class WorkflowsRevertToReviewResponse(UniversalBaseModel):
    code: typing.Optional[WorkflowsRevertToReviewResponseCode] = None
    message: typing.Optional[WorkflowsRevertToReviewResponseMessage] = None
    param: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
