

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .capability import Capability
from .change import Change
from .describe_change_set_output_execution_status import DescribeChangeSetOutputExecutionStatus
from .describe_change_set_output_rollback_configuration import DescribeChangeSetOutputRollbackConfiguration
from .describe_change_set_output_status import DescribeChangeSetOutputStatus
from .notification_arn import NotificationArn
from .parameter import Parameter
from .tag import Tag


class DescribeChangeSetOutput(UniversalBaseModel):
    """
    The output for the <a>DescribeChangeSet</a> action.
    """

    change_set_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ChangeSetName")] = (
        pydantic.Field(default=None)
    )
    """
    The name of the change set.
    """

    change_set_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ChangeSetId")] = (
        pydantic.Field(default=None)
    )
    """
    The Amazon Resource Name (ARN) of the change set.
    """

    stack_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackId")] = pydantic.Field(
        default=None
    )
    """
    The Amazon Resource Name (ARN) of the stack that's associated with the change set.
    """

    stack_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackName")] = pydantic.Field(
        default=None
    )
    """
    The name of the stack that's associated with the change set.
    """

    description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Description")] = pydantic.Field(
        default=None
    )
    """
    Information about the change set.
    """

    parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[Parameter]], FieldMetadata(alias="Parameters")
    ] = pydantic.Field(default=None)
    """
    A list of <code>Parameter</code> structures that describes the input parameters and their values used to create the change set. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html">Parameter</a> data type.
    """

    creation_time: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="CreationTime")] = (
        pydantic.Field(default=None)
    )
    """
    The start time when the change set was created, in UTC.
    """

    execution_status: typing_extensions.Annotated[
        typing.Optional[DescribeChangeSetOutputExecutionStatus], FieldMetadata(alias="ExecutionStatus")
    ] = pydantic.Field(default=None)
    """
    If the change set execution status is <code>AVAILABLE</code>, you can execute the change set. If you can't execute the change set, the status indicates why. For example, a change set might be in an <code>UNAVAILABLE</code> state because CloudFormation is still creating it or in an <code>OBSOLETE</code> state because the stack was already updated.
    """

    status: typing_extensions.Annotated[
        typing.Optional[DescribeChangeSetOutputStatus], FieldMetadata(alias="Status")
    ] = pydantic.Field(default=None)
    """
    The current status of the change set, such as <code>CREATE_IN_PROGRESS</code>, <code>CREATE_COMPLETE</code>, or <code>FAILED</code>.
    """

    status_reason: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StatusReason")] = (
        pydantic.Field(default=None)
    )
    """
    A description of the change set's status. For example, if your attempt to create a change set failed, CloudFormation shows the error message.
    """

    notification_ar_ns: typing_extensions.Annotated[
        typing.Optional[typing.List[NotificationArn]], FieldMetadata(alias="NotificationARNs")
    ] = pydantic.Field(default=None)
    """
    The ARNs of the Amazon Simple Notification Service (Amazon SNS) topics that will be associated with the stack if you execute the change set.
    """

    rollback_configuration: typing_extensions.Annotated[
        typing.Optional[DescribeChangeSetOutputRollbackConfiguration], FieldMetadata(alias="RollbackConfiguration")
    ] = pydantic.Field(default=None)
    """
    The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.
    """

    capabilities: typing_extensions.Annotated[
        typing.Optional[typing.List[Capability]], FieldMetadata(alias="Capabilities")
    ] = pydantic.Field(default=None)
    """
    If you execute the change set, the list of capabilities that were explicitly acknowledged when the change set was created.
    """

    tags: typing_extensions.Annotated[typing.Optional[typing.List[Tag]], FieldMetadata(alias="Tags")] = pydantic.Field(
        default=None
    )
    """
    If you execute the change set, the tags that will be associated with the stack.
    """

    changes: typing_extensions.Annotated[typing.Optional[typing.List[Change]], FieldMetadata(alias="Changes")] = (
        pydantic.Field(default=None)
    )
    """
    A list of <code>Change</code> structures that describes the resources CloudFormation changes if you execute the change set.
    """

    next_token: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="NextToken")] = pydantic.Field(
        default=None
    )
    """
    If the output exceeds 1 MB, a string that identifies the next page of changes. If there is no additional page, this value is null.
    """

    include_nested_stacks: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="IncludeNestedStacks")
    ] = pydantic.Field(default=None)
    """
    Verifies if <code>IncludeNestedStacks</code> is set to <code>True</code>.
    """

    parent_change_set_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ParentChangeSetId")
    ] = pydantic.Field(default=None)
    """
    Specifies the change set ID of the parent change set in the current nested change set hierarchy.
    """

    root_change_set_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="RootChangeSetId")] = (
        pydantic.Field(default=None)
    )
    """
    Specifies the change set ID of the root change set in the current nested change set hierarchy.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
