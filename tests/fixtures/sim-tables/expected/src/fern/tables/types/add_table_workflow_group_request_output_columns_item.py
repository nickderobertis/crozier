

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .add_table_workflow_group_request_output_columns_item_type import AddTableWorkflowGroupRequestOutputColumnsItemType


class AddTableWorkflowGroupRequestOutputColumnsItem(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Output column name.
    """

    type: AddTableWorkflowGroupRequestOutputColumnsItemType = pydantic.Field()
    """
    Output column data type.
    """

    required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the output column is required.
    """

    unique: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the output column must be unique.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
