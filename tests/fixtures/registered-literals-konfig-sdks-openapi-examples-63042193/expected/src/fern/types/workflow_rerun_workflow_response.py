

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WorkflowRerunWorkflowResponse(UniversalBaseModel):
    """
    A response to rerunning a workflow
    """

    workflow_id: str = pydantic.Field()
    """
    The ID of the newly-created workflow.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
