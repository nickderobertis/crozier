

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .capability import Capability
from .notification_arn import NotificationArn
from .output import Output
from .parameter import Parameter
from .stack_drift_information import StackDriftInformation
from .stack_rollback_configuration import StackRollbackConfiguration
from .stack_stack_status import StackStackStatus
from .tag import Tag


class Stack(UniversalBaseModel):
    """
    The Stack data type.
    """

    stack_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackId")] = pydantic.Field(
        default=None
    )
    """
    Unique identifier of the stack.
    """

    stack_name: typing_extensions.Annotated[str, FieldMetadata(alias="StackName")] = pydantic.Field()
    """
    The name associated with the stack.
    """

    change_set_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ChangeSetId")] = (
        pydantic.Field(default=None)
    )
    """
    The unique ID of the change set.
    """

    description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Description")] = pydantic.Field(
        default=None
    )
    """
    A user-defined description associated with the stack.
    """

    parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[Parameter]], FieldMetadata(alias="Parameters")
    ] = pydantic.Field(default=None)
    """
    A list of <code>Parameter</code> structures.
    """

    creation_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="CreationTime")] = pydantic.Field()
    """
    The time at which the stack was created.
    """

    deletion_time: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="DeletionTime")] = (
        pydantic.Field(default=None)
    )
    """
    The time the stack was deleted.
    """

    last_updated_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="LastUpdatedTime")
    ] = pydantic.Field(default=None)
    """
    The time the stack was last updated. This field will only be returned if the stack has been updated at least once.
    """

    rollback_configuration: typing_extensions.Annotated[
        typing.Optional[StackRollbackConfiguration], FieldMetadata(alias="RollbackConfiguration")
    ] = pydantic.Field(default=None)
    """
    The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.
    """

    stack_status: typing_extensions.Annotated[StackStackStatus, FieldMetadata(alias="StackStatus")] = pydantic.Field()
    """
    Current status of the stack.
    """

    stack_status_reason: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackStatusReason")] = (
        pydantic.Field(default=None)
    )
    """
    Success/failure message associated with the stack status.
    """

    disable_rollback: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="DisableRollback")] = (
        pydantic.Field(default=None)
    )
    """
    <p>Boolean to enable or disable rollback on stack creation failures:</p> <ul> <li> <p> <code>true</code>: disable rollback.</p> </li> <li> <p> <code>false</code>: enable rollback.</p> </li> </ul>
    """

    notification_ar_ns: typing_extensions.Annotated[
        typing.Optional[typing.List[NotificationArn]], FieldMetadata(alias="NotificationARNs")
    ] = pydantic.Field(default=None)
    """
    Amazon SNS topic Amazon Resource Names (ARNs) to which stack related events are published.
    """

    timeout_in_minutes: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="TimeoutInMinutes")] = (
        pydantic.Field(default=None)
    )
    """
    The amount of time within which stack creation should complete.
    """

    capabilities: typing_extensions.Annotated[
        typing.Optional[typing.List[Capability]], FieldMetadata(alias="Capabilities")
    ] = pydantic.Field(default=None)
    """
    The capabilities allowed in the stack.
    """

    outputs: typing_extensions.Annotated[typing.Optional[typing.List[Output]], FieldMetadata(alias="Outputs")] = (
        pydantic.Field(default=None)
    )
    """
    A list of output structures.
    """

    role_arn: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="RoleARN")] = pydantic.Field(
        default=None
    )
    """
    The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that's associated with the stack. During a stack operation, CloudFormation uses this role's credentials to make calls on your behalf.
    """

    tags: typing_extensions.Annotated[typing.Optional[typing.List[Tag]], FieldMetadata(alias="Tags")] = pydantic.Field(
        default=None
    )
    """
    A list of <code>Tag</code>s that specify information about the stack.
    """

    enable_termination_protection: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="EnableTerminationProtection")
    ] = pydantic.Field(default=None)
    """
    <p>Whether termination protection is enabled for the stack.</p> <p>For <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">nested stacks</a>, termination protection is set on the root stack and can't be changed directly on the nested stack. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html">Protecting a Stack From Being Deleted</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    parent_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ParentId")] = pydantic.Field(
        default=None
    )
    """
    <p>For nested stacks--stacks created as resources for another stack--the stack ID of the direct parent of this stack. For the first level of nested stacks, the root stack is also the parent stack.</p> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">Working with Nested Stacks</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    root_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="RootId")] = pydantic.Field(
        default=None
    )
    """
    <p>For nested stacks--stacks created as resources for another stack--the stack ID of the top-level stack to which the nested stack ultimately belongs.</p> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">Working with Nested Stacks</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    drift_information: typing_extensions.Annotated[
        typing.Optional[StackDriftInformation], FieldMetadata(alias="DriftInformation")
    ] = pydantic.Field(default=None)
    """
    Information about whether a stack's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
