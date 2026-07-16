

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_set_operation_action import StackSetOperationAction
from .stack_set_operation_deployment_targets import StackSetOperationDeploymentTargets
from .stack_set_operation_operation_preferences import StackSetOperationOperationPreferences
from .stack_set_operation_stack_set_drift_detection_details import StackSetOperationStackSetDriftDetectionDetails
from .stack_set_operation_status import StackSetOperationStatus
from .stack_set_operation_status_details import StackSetOperationStatusDetails


class StackSetOperation(UniversalBaseModel):
    """
    The structure that contains information about a stack set operation.
    """

    operation_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="OperationId")] = (
        pydantic.Field(default=None)
    )
    """
    The unique ID of a stack set operation.
    """

    stack_set_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackSetId")] = pydantic.Field(
        default=None
    )
    """
    The ID of the stack set.
    """

    action: typing_extensions.Annotated[typing.Optional[StackSetOperationAction], FieldMetadata(alias="Action")] = (
        pydantic.Field(default=None)
    )
    """
    The type of stack set operation: <code>CREATE</code>, <code>UPDATE</code>, or <code>DELETE</code>. Create and delete operations affect only the specified stack set instances that are associated with the specified stack set. Update operations affect both the stack set itself, in addition to <i>all</i> associated stack set instances.
    """

    status: typing_extensions.Annotated[typing.Optional[StackSetOperationStatus], FieldMetadata(alias="Status")] = (
        pydantic.Field(default=None)
    )
    """
    <p>The status of the operation.</p> <ul> <li> <p> <code>FAILED</code>: The operation exceeded the specified failure tolerance. The failure tolerance value that you've set for an operation is applied for each Region during stack create and update operations. If the number of failed stacks within a Region exceeds the failure tolerance, the status of the operation in the Region is set to <code>FAILED</code>. This in turn sets the status of the operation as a whole to <code>FAILED</code>, and CloudFormation cancels the operation in any remaining Regions.</p> </li> <li> <p> <code>QUEUED</code>: [Service-managed permissions] For automatic deployments that require a sequence of operations, the operation is queued to be performed. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-status-codes">stack set operation status codes</a> in the CloudFormation User Guide.</p> </li> <li> <p> <code>RUNNING</code>: The operation is currently being performed.</p> </li> <li> <p> <code>STOPPED</code>: The user has canceled the operation.</p> </li> <li> <p> <code>STOPPING</code>: The operation is in the process of stopping, at user request.</p> </li> <li> <p> <code>SUCCEEDED</code>: The operation completed creating or updating all the specified stacks without exceeding the failure tolerance for the operation.</p> </li> </ul>
    """

    operation_preferences: typing_extensions.Annotated[
        typing.Optional[StackSetOperationOperationPreferences], FieldMetadata(alias="OperationPreferences")
    ] = pydantic.Field(default=None)
    """
    The preferences for how CloudFormation performs this stack set operation.
    """

    retain_stacks: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="RetainStacks")] = (
        pydantic.Field(default=None)
    )
    """
    For stack set operations of action type <code>DELETE</code>, specifies whether to remove the stack instances from the specified stack set, but doesn't delete the stacks. You can't re-associate a retained stack, or add an existing, saved stack to a new stack set.
    """

    administration_role_arn: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="AdministrationRoleARN")
    ] = pydantic.Field(default=None)
    """
    <p>The Amazon Resource Name (ARN) of the IAM role used to perform this stack set operation.</p> <p>Use customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html">Define Permissions for Multiple Administrators</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    execution_role_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ExecutionRoleName")] = (
        pydantic.Field(default=None)
    )
    """
    <p>The name of the IAM execution role used to create or update the stack set.</p> <p>Use customized execution roles to control which stack resources users and groups can include in their stack sets.</p>
    """

    creation_timestamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="CreationTimestamp")
    ] = pydantic.Field(default=None)
    """
    The time at which the operation was initiated. Note that the creation times for the stack set operation might differ from the creation time of the individual stacks themselves. This is because CloudFormation needs to perform preparatory work for the operation, such as dispatching the work to the requested Regions, before actually creating the first stacks.
    """

    end_timestamp: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="EndTimestamp")] = (
        pydantic.Field(default=None)
    )
    """
    The time at which the stack set operation ended, across all accounts and Regions specified. Note that this doesn't necessarily mean that the stack set operation was successful, or even attempted, in each account or Region.
    """

    deployment_targets: typing_extensions.Annotated[
        typing.Optional[StackSetOperationDeploymentTargets], FieldMetadata(alias="DeploymentTargets")
    ] = pydantic.Field(default=None)
    """
    [Service-managed permissions] The Organizations accounts affected by the stack operation.
    """

    stack_set_drift_detection_details: typing_extensions.Annotated[
        typing.Optional[StackSetOperationStackSetDriftDetectionDetails],
        FieldMetadata(alias="StackSetDriftDetectionDetails"),
    ] = pydantic.Field(default=None)
    """
    <p>Detailed information about the drift status of the stack set. This includes information about drift operations currently being performed on the stack set.</p> <p>This information will only be present for stack set operations whose <code>Action</code> type is <code>DETECT_DRIFT</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html">Detecting Unmanaged Changes in Stack Sets</a> in the CloudFormation User Guide.</p>
    """

    status_reason: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StatusReason")] = (
        pydantic.Field(default=None)
    )
    """
    The status of the operation in details.
    """

    status_details: typing_extensions.Annotated[
        typing.Optional[StackSetOperationStatusDetails], FieldMetadata(alias="StatusDetails")
    ] = pydantic.Field(default=None)
    """
    Detailed information about the StackSet operation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
