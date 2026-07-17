

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_set_operation_preferences import StackSetOperationPreferences
from .stack_set_operation_summary_action import StackSetOperationSummaryAction
from .stack_set_operation_summary_status import StackSetOperationSummaryStatus
from .stack_set_operation_summary_status_details import StackSetOperationSummaryStatusDetails


class StackSetOperationSummary(UniversalBaseModel):
    """
    The structures that contain summary information about the specified operation.
    """

    operation_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OperationId"),
        pydantic.Field(alias="OperationId", description="The unique ID of the stack set operation."),
    ] = None
    """
    The unique ID of the stack set operation.
    """

    action: typing_extensions.Annotated[
        typing.Optional[StackSetOperationSummaryAction],
        FieldMetadata(alias="Action"),
        pydantic.Field(
            alias="Action",
            description="The type of operation: <code>CREATE</code>, <code>UPDATE</code>, or <code>DELETE</code>. Create and delete operations affect only the specified stack instances that are associated with the specified stack set. Update operations affect both the stack set itself and <i>all</i> associated stack set instances.",
        ),
    ] = None
    """
    The type of operation: <code>CREATE</code>, <code>UPDATE</code>, or <code>DELETE</code>. Create and delete operations affect only the specified stack instances that are associated with the specified stack set. Update operations affect both the stack set itself and <i>all</i> associated stack set instances.
    """

    status: typing_extensions.Annotated[
        typing.Optional[StackSetOperationSummaryStatus],
        FieldMetadata(alias="Status"),
        pydantic.Field(
            alias="Status",
            description='<p>The overall status of the operation.</p> <ul> <li> <p> <code>FAILED</code>: The operation exceeded the specified failure tolerance. The failure tolerance value that you\'ve set for an operation is applied for each Region during stack create and update operations. If the number of failed stacks within a Region exceeds the failure tolerance, the status of the operation in the Region is set to <code>FAILED</code>. This in turn sets the status of the operation as a whole to <code>FAILED</code>, and CloudFormation cancels the operation in any remaining Regions.</p> </li> <li> <p> <code>QUEUED</code>: [Service-managed permissions] For automatic deployments that require a sequence of operations, the operation is queued to be performed. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-status-codes">stack set operation status codes</a> in the CloudFormation User Guide.</p> </li> <li> <p> <code>RUNNING</code>: The operation is currently being performed.</p> </li> <li> <p> <code>STOPPED</code>: The user has canceled the operation.</p> </li> <li> <p> <code>STOPPING</code>: The operation is in the process of stopping, at user request.</p> </li> <li> <p> <code>SUCCEEDED</code>: The operation completed creating or updating all the specified stacks without exceeding the failure tolerance for the operation.</p> </li> </ul>',
        ),
    ] = None
    """
    <p>The overall status of the operation.</p> <ul> <li> <p> <code>FAILED</code>: The operation exceeded the specified failure tolerance. The failure tolerance value that you've set for an operation is applied for each Region during stack create and update operations. If the number of failed stacks within a Region exceeds the failure tolerance, the status of the operation in the Region is set to <code>FAILED</code>. This in turn sets the status of the operation as a whole to <code>FAILED</code>, and CloudFormation cancels the operation in any remaining Regions.</p> </li> <li> <p> <code>QUEUED</code>: [Service-managed permissions] For automatic deployments that require a sequence of operations, the operation is queued to be performed. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-status-codes">stack set operation status codes</a> in the CloudFormation User Guide.</p> </li> <li> <p> <code>RUNNING</code>: The operation is currently being performed.</p> </li> <li> <p> <code>STOPPED</code>: The user has canceled the operation.</p> </li> <li> <p> <code>STOPPING</code>: The operation is in the process of stopping, at user request.</p> </li> <li> <p> <code>SUCCEEDED</code>: The operation completed creating or updating all the specified stacks without exceeding the failure tolerance for the operation.</p> </li> </ul>
    """

    creation_timestamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="CreationTimestamp"),
        pydantic.Field(
            alias="CreationTimestamp",
            description="The time at which the operation was initiated. Note that the creation times for the stack set operation might differ from the creation time of the individual stacks themselves. This is because CloudFormation needs to perform preparatory work for the operation, such as dispatching the work to the requested Regions, before actually creating the first stacks.",
        ),
    ] = None
    """
    The time at which the operation was initiated. Note that the creation times for the stack set operation might differ from the creation time of the individual stacks themselves. This is because CloudFormation needs to perform preparatory work for the operation, such as dispatching the work to the requested Regions, before actually creating the first stacks.
    """

    end_timestamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="EndTimestamp"),
        pydantic.Field(
            alias="EndTimestamp",
            description="The time at which the stack set operation ended, across all accounts and Regions specified. Note that this doesn't necessarily mean that the stack set operation was successful, or even attempted, in each account or Region.",
        ),
    ] = None
    """
    The time at which the stack set operation ended, across all accounts and Regions specified. Note that this doesn't necessarily mean that the stack set operation was successful, or even attempted, in each account or Region.
    """

    status_reason: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StatusReason"),
        pydantic.Field(alias="StatusReason", description="The status of the operation in details."),
    ] = None
    """
    The status of the operation in details.
    """

    status_details: typing_extensions.Annotated[
        typing.Optional[StackSetOperationSummaryStatusDetails],
        FieldMetadata(alias="StatusDetails"),
        pydantic.Field(alias="StatusDetails", description="Detailed information about the stack set operation."),
    ] = None
    """
    Detailed information about the stack set operation.
    """

    operation_preferences: typing_extensions.Annotated[
        typing.Optional[StackSetOperationPreferences],
        FieldMetadata(alias="OperationPreferences"),
        pydantic.Field(alias="OperationPreferences"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
