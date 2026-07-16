

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .describe_stack_drift_detection_status_output_detection_status import (
    DescribeStackDriftDetectionStatusOutputDetectionStatus,
)
from .describe_stack_drift_detection_status_output_stack_drift_status import (
    DescribeStackDriftDetectionStatusOutputStackDriftStatus,
)


class DescribeStackDriftDetectionStatusOutput(UniversalBaseModel):
    stack_id: typing_extensions.Annotated[str, FieldMetadata(alias="StackId")] = pydantic.Field()
    """
    The ID of the stack.
    """

    stack_drift_detection_id: typing_extensions.Annotated[str, FieldMetadata(alias="StackDriftDetectionId")] = (
        pydantic.Field()
    )
    """
    <p>The ID of the drift detection results of this operation.</p> <p>CloudFormation generates new results, with a new drift detection ID, each time this operation is run. However, the number of reports CloudFormation retains for any given stack, and for how long, may vary.</p>
    """

    stack_drift_status: typing_extensions.Annotated[
        typing.Optional[DescribeStackDriftDetectionStatusOutputStackDriftStatus],
        FieldMetadata(alias="StackDriftStatus"),
    ] = pydantic.Field(default=None)
    """
    <p>Status of the stack's actual configuration compared to its expected configuration.</p> <ul> <li> <p> <code>DRIFTED</code>: The stack differs from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation hasn't checked if the stack differs from its expected template configuration.</p> </li> <li> <p> <code>IN_SYNC</code>: The stack's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>UNKNOWN</code>: This value is reserved for future use.</p> </li> </ul>
    """

    detection_status: typing_extensions.Annotated[
        DescribeStackDriftDetectionStatusOutputDetectionStatus, FieldMetadata(alias="DetectionStatus")
    ] = pydantic.Field()
    """
    <p>The status of the stack drift detection operation.</p> <ul> <li> <p> <code>DETECTION_COMPLETE</code>: The stack drift detection operation has successfully completed for all resources in the stack that support drift detection. (Resources that don't currently support stack detection remain unchecked.)</p> <p>If you specified logical resource IDs for CloudFormation to use as a filter for the stack drift detection operation, only the resources with those logical IDs are checked for drift.</p> </li> <li> <p> <code>DETECTION_FAILED</code>: The stack drift detection operation has failed for at least one resource in the stack. Results will be available for resources on which CloudFormation successfully completed drift detection.</p> </li> <li> <p> <code>DETECTION_IN_PROGRESS</code>: The stack drift detection operation is currently in progress.</p> </li> </ul>
    """

    detection_status_reason: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="DetectionStatusReason")
    ] = pydantic.Field(default=None)
    """
    The reason the stack drift detection operation has its current status.
    """

    drifted_stack_resource_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="DriftedStackResourceCount")
    ] = pydantic.Field(default=None)
    """
    Total number of stack resources that have drifted. This is NULL until the drift detection operation reaches a status of <code>DETECTION_COMPLETE</code>. This value will be 0 for stacks whose drift status is <code>IN_SYNC</code>.
    """

    timestamp: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="Timestamp")] = pydantic.Field()
    """
    Time at which the stack drift detection operation was initiated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
