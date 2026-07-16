

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .describe_stack_set_operation_output_stack_set_operation_stack_set_drift_detection_details_drift_detection_status import (
    DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftDetectionStatus,
)
from .describe_stack_set_operation_output_stack_set_operation_stack_set_drift_detection_details_drift_status import (
    DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftStatus,
)


class DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetails(UniversalBaseModel):
    """
    <p>Detailed information about the drift status of the stack set. This includes information about drift operations currently being performed on the stack set.</p> <p>This information will only be present for stack set operations whose <code>Action</code> type is <code>DETECT_DRIFT</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html">Detecting Unmanaged Changes in Stack Sets</a> in the CloudFormation User Guide.</p>
    """

    drift_status: typing_extensions.Annotated[
        typing.Optional[DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftStatus],
        FieldMetadata(alias="DriftStatus"),
    ] = pydantic.Field(default=None)
    """
    <p>Status of the stack set's actual configuration compared to its expected template and parameter configuration. A stack set is considered to have drifted if one or more of its stack instances have drifted from their expected template and parameter configuration.</p> <ul> <li> <p> <code>DRIFTED</code>: One or more of the stack instances belonging to the stack set stack differs from the expected template and parameter configuration. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation hasn't checked the stack set for drift.</p> </li> <li> <p> <code>IN_SYNC</code>: All of the stack instances belonging to the stack set stack match from the expected template and parameter configuration.</p> </li> </ul>
    """

    drift_detection_status: typing_extensions.Annotated[
        typing.Optional[
            DescribeStackSetOperationOutputStackSetOperationStackSetDriftDetectionDetailsDriftDetectionStatus
        ],
        FieldMetadata(alias="DriftDetectionStatus"),
    ] = pydantic.Field(default=None)
    """
    <p>The status of the stack set drift detection operation.</p> <ul> <li> <p> <code>COMPLETED</code>: The drift detection operation completed without failing on any stack instances.</p> </li> <li> <p> <code>FAILED</code>: The drift detection operation exceeded the specified failure tolerance.</p> </li> <li> <p> <code>PARTIAL_SUCCESS</code>: The drift detection operation completed without exceeding the failure tolerance for the operation.</p> </li> <li> <p> <code>IN_PROGRESS</code>: The drift detection operation is currently being performed.</p> </li> <li> <p> <code>STOPPED</code>: The user has canceled the drift detection operation.</p> </li> </ul>
    """

    last_drift_check_timestamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="LastDriftCheckTimestamp")
    ] = pydantic.Field(default=None)
    """
    Most recent time when CloudFormation performed a drift detection operation on the stack set. This value will be <code>NULL</code> for any stack set on which drift detection hasn't yet been performed.
    """

    total_stack_instances_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="TotalStackInstancesCount")
    ] = pydantic.Field(default=None)
    """
    <p>The total number of stack instances belonging to this stack set.</p> <p>The total number of stack instances is equal to the total of:</p> <ul> <li> <p>Stack instances that match the stack set configuration.</p> </li> <li> <p>Stack instances that have drifted from the stack set configuration.</p> </li> <li> <p>Stack instances where the drift detection operation has failed.</p> </li> <li> <p>Stack instances currently being checked for drift.</p> </li> </ul>
    """

    drifted_stack_instances_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="DriftedStackInstancesCount")
    ] = pydantic.Field(default=None)
    """
    The number of stack instances that have drifted from the expected template and parameter configuration of the stack set. A stack instance is considered to have drifted if one or more of the resources in the associated stack don't match their expected configuration.
    """

    in_sync_stack_instances_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="InSyncStackInstancesCount")
    ] = pydantic.Field(default=None)
    """
    The number of stack instances which match the expected template and parameter configuration of the stack set.
    """

    in_progress_stack_instances_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="InProgressStackInstancesCount")
    ] = pydantic.Field(default=None)
    """
    The number of stack instances that are currently being checked for drift.
    """

    failed_stack_instances_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="FailedStackInstancesCount")
    ] = pydantic.Field(default=None)
    """
    The number of stack instances for which the drift detection operation failed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
