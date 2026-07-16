

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_set_operation_result_summary_account_gate_result import StackSetOperationResultSummaryAccountGateResult
from .stack_set_operation_result_summary_status import StackSetOperationResultSummaryStatus


class StackSetOperationResultSummary(UniversalBaseModel):
    """
    The structure that contains information about a specified operation's results for a given account in a given Region.
    """

    account: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Account"),
        pydantic.Field(
            alias="Account",
            description="[Self-managed permissions] The name of the Amazon Web Services account for this operation result.",
        ),
    ] = None
    """
    [Self-managed permissions] The name of the Amazon Web Services account for this operation result.
    """

    region: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Region"),
        pydantic.Field(
            alias="Region", description="The name of the Amazon Web Services Region for this operation result."
        ),
    ] = None
    """
    The name of the Amazon Web Services Region for this operation result.
    """

    status: typing_extensions.Annotated[
        typing.Optional[StackSetOperationResultSummaryStatus],
        FieldMetadata(alias="Status"),
        pydantic.Field(
            alias="Status",
            description="<p>The result status of the stack set operation for the given account in the given Region.</p> <ul> <li> <p> <code>CANCELLED</code>: The operation in the specified account and Region has been canceled. This is either because a user has stopped the stack set operation, or because the failure tolerance of the stack set operation has been exceeded.</p> </li> <li> <p> <code>FAILED</code>: The operation in the specified account and Region failed.</p> <p>If the stack set operation fails in enough accounts within a Region, the failure tolerance for the stack set operation as a whole might be exceeded.</p> </li> <li> <p> <code>RUNNING</code>: The operation in the specified account and Region is currently in progress.</p> </li> <li> <p> <code>PENDING</code>: The operation in the specified account and Region has yet to start.</p> </li> <li> <p> <code>SUCCEEDED</code>: The operation in the specified account and Region completed successfully.</p> </li> </ul>",
        ),
    ] = None
    """
    <p>The result status of the stack set operation for the given account in the given Region.</p> <ul> <li> <p> <code>CANCELLED</code>: The operation in the specified account and Region has been canceled. This is either because a user has stopped the stack set operation, or because the failure tolerance of the stack set operation has been exceeded.</p> </li> <li> <p> <code>FAILED</code>: The operation in the specified account and Region failed.</p> <p>If the stack set operation fails in enough accounts within a Region, the failure tolerance for the stack set operation as a whole might be exceeded.</p> </li> <li> <p> <code>RUNNING</code>: The operation in the specified account and Region is currently in progress.</p> </li> <li> <p> <code>PENDING</code>: The operation in the specified account and Region has yet to start.</p> </li> <li> <p> <code>SUCCEEDED</code>: The operation in the specified account and Region completed successfully.</p> </li> </ul>
    """

    status_reason: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StatusReason"),
        pydantic.Field(alias="StatusReason", description="The reason for the assigned result status."),
    ] = None
    """
    The reason for the assigned result status.
    """

    account_gate_result: typing_extensions.Annotated[
        typing.Optional[StackSetOperationResultSummaryAccountGateResult],
        FieldMetadata(alias="AccountGateResult"),
        pydantic.Field(
            alias="AccountGateResult",
            description="The results of the account gate function CloudFormation invokes, if present, before proceeding with stack set operations in an account.",
        ),
    ] = None
    """
    The results of the account gate function CloudFormation invokes, if present, before proceeding with stack set operations in an account.
    """

    organizational_unit_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OrganizationalUnitId"),
        pydantic.Field(
            alias="OrganizationalUnitId",
            description='[Service-managed permissions] The organization root ID or organizational unit (OU) IDs that you specified for <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeploymentTargets.html">DeploymentTargets</a>.',
        ),
    ] = None
    """
    [Service-managed permissions] The organization root ID or organizational unit (OU) IDs that you specified for <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeploymentTargets.html">DeploymentTargets</a>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
