

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2delete_workflow_group_data_columns_item import V2DeleteWorkflowGroupDataColumnsItem


class V2DeleteWorkflowGroupData(UniversalBaseModel):
    """
    Workflow-group deletion acknowledgement and surviving columns.
    """

    id: str = pydantic.Field()
    """
    Identifier of the deleted workflow group.
    """

    deleted: bool = pydantic.Field()
    """
    Confirms that the workflow group was deleted.
    """

    columns: typing.List[V2DeleteWorkflowGroupDataColumnsItem] = pydantic.Field()
    """
    Surviving table columns.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
