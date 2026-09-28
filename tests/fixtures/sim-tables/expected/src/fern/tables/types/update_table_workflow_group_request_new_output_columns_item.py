

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_table_workflow_group_request_new_output_columns_item_type import (
    UpdateTableWorkflowGroupRequestNewOutputColumnsItemType,
)


class UpdateTableWorkflowGroupRequestNewOutputColumnsItem(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Output column name.
    """

    type: UpdateTableWorkflowGroupRequestNewOutputColumnsItemType = pydantic.Field()
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
