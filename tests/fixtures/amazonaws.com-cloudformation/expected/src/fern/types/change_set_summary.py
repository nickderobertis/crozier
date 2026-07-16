

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .change_set_summary_execution_status import ChangeSetSummaryExecutionStatus
from .change_set_summary_status import ChangeSetSummaryStatus


class ChangeSetSummary(UniversalBaseModel):
    """
    The <code>ChangeSetSummary</code> structure describes a change set, its status, and the stack with which it's associated.
    """

    stack_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackId")] = pydantic.Field(
        default=None
    )
    """
    The ID of the stack with which the change set is associated.
    """

    stack_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackName")] = pydantic.Field(
        default=None
    )
    """
    The name of the stack with which the change set is associated.
    """

    change_set_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ChangeSetId")] = (
        pydantic.Field(default=None)
    )
    """
    The ID of the change set.
    """

    change_set_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ChangeSetName")] = (
        pydantic.Field(default=None)
    )
    """
    The name of the change set.
    """

    execution_status: typing_extensions.Annotated[
        typing.Optional[ChangeSetSummaryExecutionStatus], FieldMetadata(alias="ExecutionStatus")
    ] = pydantic.Field(default=None)
    """
    If the change set execution status is <code>AVAILABLE</code>, you can execute the change set. If you can't execute the change set, the status indicates why. For example, a change set might be in an <code>UNAVAILABLE</code> state because CloudFormation is still creating it or in an <code>OBSOLETE</code> state because the stack was already updated.
    """

    status: typing_extensions.Annotated[typing.Optional[ChangeSetSummaryStatus], FieldMetadata(alias="Status")] = (
        pydantic.Field(default=None)
    )
    """
    The state of the change set, such as <code>CREATE_IN_PROGRESS</code>, <code>CREATE_COMPLETE</code>, or <code>FAILED</code>.
    """

    status_reason: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StatusReason")] = (
        pydantic.Field(default=None)
    )
    """
    A description of the change set's status. For example, if your change set is in the <code>FAILED</code> state, CloudFormation shows the error message.
    """

    creation_time: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="CreationTime")] = (
        pydantic.Field(default=None)
    )
    """
    The start time when the change set was created, in UTC.
    """

    description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Description")] = pydantic.Field(
        default=None
    )
    """
    Descriptive information about the change set.
    """

    include_nested_stacks: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="IncludeNestedStacks")
    ] = pydantic.Field(default=None)
    """
    Specifies the current setting of <code>IncludeNestedStacks</code> for the change set.
    """

    parent_change_set_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ParentChangeSetId")
    ] = pydantic.Field(default=None)
    """
    The parent change set ID.
    """

    root_change_set_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="RootChangeSetId")] = (
        pydantic.Field(default=None)
    )
    """
    The root change set ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
