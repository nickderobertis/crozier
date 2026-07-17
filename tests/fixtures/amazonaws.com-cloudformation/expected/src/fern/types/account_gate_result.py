

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_gate_result_status import AccountGateResultStatus


class AccountGateResult(UniversalBaseModel):
    """
    <p>Structure that contains the results of the account gate function which CloudFormation invokes, if present, before proceeding with a stack set operation in an account and Region.</p> <p>For each account and Region, CloudFormation lets you specify a Lambda function that encapsulates any requirements that must be met before CloudFormation can proceed with a stack set operation in that account and Region. CloudFormation invokes the function each time a stack set operation is requested for that account and Region; if the function returns <code>FAILED</code>, CloudFormation cancels the operation in that account and Region, and sets the stack set operation result status for that account and Region to <code>FAILED</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-account-gating.html">Configuring a target account gate</a>.</p>
    """

    status: typing_extensions.Annotated[
        typing.Optional[AccountGateResultStatus],
        FieldMetadata(alias="Status"),
        pydantic.Field(
            alias="Status",
            description="<p>The status of the account gate function.</p> <ul> <li> <p> <code>SUCCEEDED</code>: The account gate function has determined that the account and Region passes any requirements for a stack set operation to occur. CloudFormation proceeds with the stack operation in that account and Region.</p> </li> <li> <p> <code>FAILED</code>: The account gate function has determined that the account and Region doesn't meet the requirements for a stack set operation to occur. CloudFormation cancels the stack set operation in that account and Region, and sets the stack set operation result status for that account and Region to <code>FAILED</code>.</p> </li> <li> <p> <code>SKIPPED</code>: CloudFormation has skipped calling the account gate function for this account and Region, for one of the following reasons:</p> <ul> <li> <p>An account gate function hasn't been specified for the account and Region. CloudFormation proceeds with the stack set operation in this account and Region.</p> </li> <li> <p>The <code>AWSCloudFormationStackSetExecutionRole</code> of the stack set administration account lacks permissions to invoke the function. CloudFormation proceeds with the stack set operation in this account and Region.</p> </li> <li> <p>Either no action is necessary, or no action is possible, on the stack. CloudFormation skips the stack set operation in this account and Region.</p> </li> </ul> </li> </ul>",
        ),
    ] = None
    """
    <p>The status of the account gate function.</p> <ul> <li> <p> <code>SUCCEEDED</code>: The account gate function has determined that the account and Region passes any requirements for a stack set operation to occur. CloudFormation proceeds with the stack operation in that account and Region.</p> </li> <li> <p> <code>FAILED</code>: The account gate function has determined that the account and Region doesn't meet the requirements for a stack set operation to occur. CloudFormation cancels the stack set operation in that account and Region, and sets the stack set operation result status for that account and Region to <code>FAILED</code>.</p> </li> <li> <p> <code>SKIPPED</code>: CloudFormation has skipped calling the account gate function for this account and Region, for one of the following reasons:</p> <ul> <li> <p>An account gate function hasn't been specified for the account and Region. CloudFormation proceeds with the stack set operation in this account and Region.</p> </li> <li> <p>The <code>AWSCloudFormationStackSetExecutionRole</code> of the stack set administration account lacks permissions to invoke the function. CloudFormation proceeds with the stack set operation in this account and Region.</p> </li> <li> <p>Either no action is necessary, or no action is possible, on the stack. CloudFormation skips the stack set operation in this account and Region.</p> </li> </ul> </li> </ul>
    """

    status_reason: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StatusReason"),
        pydantic.Field(
            alias="StatusReason",
            description="The reason for the account gate status assigned to this account and Region for the stack set operation.",
        ),
    ] = None
    """
    The reason for the account gate status assigned to this account and Region for the stack set operation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
