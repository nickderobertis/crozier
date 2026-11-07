

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_workflow_metadata_request_updates_item_action import UpdateWorkflowMetadataRequestUpdatesItemAction


class UpdateWorkflowMetadataRequestUpdatesItem(UniversalBaseModel):
    action: UpdateWorkflowMetadataRequestUpdatesItemAction = pydantic.Field()
    """
    The type of action you'd like to take on an existing attribute (read-only fields cannot be updated). Use the remove action to clear values. If using the remove action, the attribute cannot be required by the workflow.
    """

    path: str = pydantic.Field()
    """
    The workflow attribute id that you'd like to make a change to. Workflow attribute IDs and values can be retrieved using the [Retrieve a Workflow](https://developer.ironcladapp.com/reference/retrieve-a-workflow) endpoint.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value to change the attribute to. Only required when the `action` property is `set` and not `remove`. The value's format must conform to the field type (e.g., `"someString"` for strings, `true` or `false` for booleans, etc.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
