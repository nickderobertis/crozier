

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.query_next_after import QueryNextAfter
from ...types.workflow_object import WorkflowObject


class PostV1QueryWorkflowsResponse(UniversalBaseModel):
    workflows: typing.List[WorkflowObject] = pydantic.Field()
    """
    A list of workflow objects. Entries may not be unique if query included a 'projection'.
    """

    next_after: typing.Optional[QueryNextAfter] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
