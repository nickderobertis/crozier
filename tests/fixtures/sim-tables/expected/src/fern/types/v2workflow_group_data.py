

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2table_workflow_group import V2TableWorkflowGroup
from .v2workflow_group_data_columns_item import V2WorkflowGroupDataColumnsItem


class V2WorkflowGroupData(UniversalBaseModel):
    """
    A workflow group and the resulting table columns.
    """

    group: V2TableWorkflowGroup = pydantic.Field()
    """
    The created or updated workflow group.
    """

    columns: typing.List[V2WorkflowGroupDataColumnsItem] = pydantic.Field()
    """
    Current table columns after the mutation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
