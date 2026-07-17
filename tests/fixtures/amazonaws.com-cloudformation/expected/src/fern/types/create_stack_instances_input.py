

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account import Account
from .create_stack_instances_input_call_as import CreateStackInstancesInputCallAs
from .create_stack_instances_input_deployment_targets import CreateStackInstancesInputDeploymentTargets
from .create_stack_instances_input_operation_preferences import CreateStackInstancesInputOperationPreferences
from .parameter import Parameter
from .region import Region


class CreateStackInstancesInput(UniversalBaseModel):
    stack_set_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StackSetName"),
        pydantic.Field(
            alias="StackSetName",
            description="The name or unique ID of the stack set that you want to create stack instances from.",
        ),
    ]
    """
    The name or unique ID of the stack set that you want to create stack instances from.
    """

    accounts: typing_extensions.Annotated[
        typing.Optional[typing.List[Account]],
        FieldMetadata(alias="Accounts"),
        pydantic.Field(
            alias="Accounts",
            description="<p>[Self-managed permissions] The names of one or more Amazon Web Services accounts that you want to create stack instances in the specified Region(s) for.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>",
        ),
    ] = None
    """
    <p>[Self-managed permissions] The names of one or more Amazon Web Services accounts that you want to create stack instances in the specified Region(s) for.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
    """

    deployment_targets: typing_extensions.Annotated[
        typing.Optional[CreateStackInstancesInputDeploymentTargets],
        FieldMetadata(alias="DeploymentTargets"),
        pydantic.Field(
            alias="DeploymentTargets",
            description="<p>[Service-managed permissions] The Organizations accounts for which to create stack instances in the specified Amazon Web Services Regions.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>",
        ),
    ] = None
    """
    <p>[Service-managed permissions] The Organizations accounts for which to create stack instances in the specified Amazon Web Services Regions.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
    """

    regions: typing_extensions.Annotated[
        typing.List[Region],
        FieldMetadata(alias="Regions"),
        pydantic.Field(
            alias="Regions",
            description="The names of one or more Amazon Web Services Regions where you want to create stack instances using the specified Amazon Web Services accounts.",
        ),
    ]
    """
    The names of one or more Amazon Web Services Regions where you want to create stack instances using the specified Amazon Web Services accounts.
    """

    parameter_overrides: typing_extensions.Annotated[
        typing.Optional[typing.List[Parameter]],
        FieldMetadata(alias="ParameterOverrides"),
        pydantic.Field(
            alias="ParameterOverrides",
            description="<p>A list of stack set parameters whose values you want to override in the selected stack instances.</p> <p>Any overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions. When specifying parameters and their values, be aware of how CloudFormation sets parameter values during stack instance operations:</p> <ul> <li> <p>To override the current value for a parameter, include the parameter and specify its value.</p> </li> <li> <p>To leave an overridden parameter set to its present value, include the parameter and specify <code>UsePreviousValue</code> as <code>true</code>. (You can't specify both a value and set <code>UsePreviousValue</code> to <code>true</code>.)</p> </li> <li> <p>To set an overridden parameter back to the value specified in the stack set, specify a parameter list but don't include the parameter in the list.</p> </li> <li> <p>To leave all parameters set to their present values, don't specify this property at all.</p> </li> </ul> <p>During stack set updates, any parameter values overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only override the parameter <i>values</i> that are specified in the stack set; to add or delete a parameter itself, use <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html\">UpdateStackSet</a> to update the stack set template.</p>",
        ),
    ] = None
    """
    <p>A list of stack set parameters whose values you want to override in the selected stack instances.</p> <p>Any overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions. When specifying parameters and their values, be aware of how CloudFormation sets parameter values during stack instance operations:</p> <ul> <li> <p>To override the current value for a parameter, include the parameter and specify its value.</p> </li> <li> <p>To leave an overridden parameter set to its present value, include the parameter and specify <code>UsePreviousValue</code> as <code>true</code>. (You can't specify both a value and set <code>UsePreviousValue</code> to <code>true</code>.)</p> </li> <li> <p>To set an overridden parameter back to the value specified in the stack set, specify a parameter list but don't include the parameter in the list.</p> </li> <li> <p>To leave all parameters set to their present values, don't specify this property at all.</p> </li> </ul> <p>During stack set updates, any parameter values overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only override the parameter <i>values</i> that are specified in the stack set; to add or delete a parameter itself, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update the stack set template.</p>
    """

    operation_preferences: typing_extensions.Annotated[
        typing.Optional[CreateStackInstancesInputOperationPreferences],
        FieldMetadata(alias="OperationPreferences"),
        pydantic.Field(
            alias="OperationPreferences",
            description="Preferences for how CloudFormation performs this stack set operation.",
        ),
    ] = None
    """
    Preferences for how CloudFormation performs this stack set operation.
    """

    operation_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OperationId"),
        pydantic.Field(
            alias="OperationId",
            description="<p>The unique identifier for this stack set operation.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p> <p>Repeating this stack set operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>",
        ),
    ] = None
    """
    <p>The unique identifier for this stack set operation.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p> <p>Repeating this stack set operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>
    """

    call_as: typing_extensions.Annotated[
        typing.Optional[CreateStackInstancesInputCallAs],
        FieldMetadata(alias="CallAs"),
        pydantic.Field(
            alias="CallAs",
            description='<p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization\'s management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>',
        ),
    ] = None
    """
    <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
