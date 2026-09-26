

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2delete_workflow_group_data import V2DeleteWorkflowGroupData


class V2DeleteTableWorkflowGroupResponse(UniversalBaseModel):
    """
    Deletion acknowledgement and surviving table columns.
    """

    data: V2DeleteWorkflowGroupData = pydantic.Field()
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
