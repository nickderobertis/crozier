

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_instance_summary_drift_status import StackInstanceSummaryDriftStatus
from .stack_instance_summary_stack_instance_status import StackInstanceSummaryStackInstanceStatus
from .stack_instance_summary_status import StackInstanceSummaryStatus


class StackInstanceSummary(UniversalBaseModel):
    """
    The structure that contains summary information about a stack instance.
    """

    stack_set_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackSetId")] = pydantic.Field(
        default=None
    )
    """
    The name or unique ID of the stack set that the stack instance is associated with.
    """

    region: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Region")] = pydantic.Field(
        default=None
    )
    """
    The name of the Amazon Web Services Region that the stack instance is associated with.
    """

    account: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Account")] = pydantic.Field(
        default=None
    )
    """
    [Self-managed permissions] The name of the Amazon Web Services account that the stack instance is associated with.
    """

    stack_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackId")] = pydantic.Field(
        default=None
    )
    """
    The ID of the stack instance.
    """

    status: typing_extensions.Annotated[typing.Optional[StackInstanceSummaryStatus], FieldMetadata(alias="Status")] = (
        pydantic.Field(default=None)
    )
    """
    <p>The status of the stack instance, in terms of its synchronization with its associated stack set.</p> <ul> <li> <p> <code>INOPERABLE</code>: A <code>DeleteStackInstances</code> operation has failed and left the stack in an unstable state. Stacks in this state are excluded from further <code>UpdateStackSet</code> operations. You might need to perform a <code>DeleteStackInstances</code> operation, with <code>RetainStacks</code> set to <code>true</code>, to delete the stack instance, and then delete the stack manually.</p> </li> <li> <p> <code>OUTDATED</code>: The stack isn't currently up to date with the stack set because:</p> <ul> <li> <p>The associated stack failed during a <code>CreateStackSet</code> or <code>UpdateStackSet</code> operation.</p> </li> <li> <p>The stack was part of a <code>CreateStackSet</code> or <code>UpdateStackSet</code> operation that failed or was stopped before the stack was created or updated.</p> </li> </ul> </li> <li> <p> <code>CURRENT</code>: The stack is currently up to date with the stack set.</p> </li> </ul>
    """

    status_reason: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StatusReason")] = (
        pydantic.Field(default=None)
    )
    """
    The explanation for the specific status code assigned to this stack instance.
    """

    stack_instance_status: typing_extensions.Annotated[
        typing.Optional[StackInstanceSummaryStackInstanceStatus], FieldMetadata(alias="StackInstanceStatus")
    ] = pydantic.Field(default=None)
    """
    The detailed status of the stack instance.
    """

    organizational_unit_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="OrganizationalUnitId")
    ] = pydantic.Field(default=None)
    """
    [Service-managed permissions] The organization root ID or organizational unit (OU) IDs that you specified for <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeploymentTargets.html">DeploymentTargets</a>.
    """

    drift_status: typing_extensions.Annotated[
        typing.Optional[StackInstanceSummaryDriftStatus], FieldMetadata(alias="DriftStatus")
    ] = pydantic.Field(default=None)
    """
    <p>Status of the stack instance's actual configuration compared to the expected template and parameter configuration of the stack set to which it belongs.</p> <ul> <li> <p> <code>DRIFTED</code>: The stack differs from the expected template and parameter configuration of the stack set to which it belongs. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation hasn't checked if the stack instance differs from its expected stack set configuration.</p> </li> <li> <p> <code>IN_SYNC</code>: The stack instance's actual configuration matches its expected stack set configuration.</p> </li> <li> <p> <code>UNKNOWN</code>: This value is reserved for future use.</p> </li> </ul>
    """

    last_drift_check_timestamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="LastDriftCheckTimestamp")
    ] = pydantic.Field(default=None)
    """
    Most recent time when CloudFormation performed a drift detection operation on the stack instance. This value will be <code>NULL</code> for any stack instance on which drift detection hasn't yet been performed.
    """

    last_operation_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="LastOperationId")] = (
        pydantic.Field(default=None)
    )
    """
    The last unique ID of a StackSet operation performed on a stack instance.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
