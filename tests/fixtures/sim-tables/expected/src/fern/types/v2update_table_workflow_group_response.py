

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2workflow_group_data import V2WorkflowGroupData


class V2UpdateTableWorkflowGroupResponse(UniversalBaseModel):
    """
    The workflow group and complete resulting table columns.
    """

    data: V2WorkflowGroupData = pydantic.Field()
    """
    Response data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
