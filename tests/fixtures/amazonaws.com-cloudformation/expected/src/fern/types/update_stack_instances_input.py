

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account import Account
from .parameter import Parameter
from .region import Region
from .update_stack_instances_input_call_as import UpdateStackInstancesInputCallAs
from .update_stack_instances_input_deployment_targets import UpdateStackInstancesInputDeploymentTargets
from .update_stack_instances_input_operation_preferences import UpdateStackInstancesInputOperationPreferences


class UpdateStackInstancesInput(UniversalBaseModel):
    stack_set_name: typing_extensions.Annotated[str, FieldMetadata(alias="StackSetName")] = pydantic.Field()
    """
    The name or unique ID of the stack set associated with the stack instances.
    """

    accounts: typing_extensions.Annotated[typing.Optional[typing.List[Account]], FieldMetadata(alias="Accounts")] = (
        pydantic.Field(default=None)
    )
    """
    <p>[Self-managed permissions] The names of one or more Amazon Web Services accounts for which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
    """

    deployment_targets: typing_extensions.Annotated[
        typing.Optional[UpdateStackInstancesInputDeploymentTargets], FieldMetadata(alias="DeploymentTargets")
    ] = pydantic.Field(default=None)
    """
    <p>[Service-managed permissions] The Organizations accounts for which you want to update parameter values for stack instances. If your update targets OUs, the overridden parameter values only apply to the accounts that are currently in the target OUs and their child OUs. Accounts added to the target OUs and their child OUs in the future won't use the overridden values.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
    """

    regions: typing_extensions.Annotated[typing.List[Region], FieldMetadata(alias="Regions")] = pydantic.Field()
    """
    The names of one or more Amazon Web Services Regions in which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions.
    """

    parameter_overrides: typing_extensions.Annotated[
        typing.Optional[typing.List[Parameter]], FieldMetadata(alias="ParameterOverrides")
    ] = pydantic.Field(default=None)
    """
    <p>A list of input parameters whose values you want to update for the specified stack instances.</p> <p>Any overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions. When specifying parameters and their values, be aware of how CloudFormation sets parameter values during stack instance update operations:</p> <ul> <li> <p>To override the current value for a parameter, include the parameter and specify its value.</p> </li> <li> <p>To leave an overridden parameter set to its present value, include the parameter and specify <code>UsePreviousValue</code> as <code>true</code>. (You can't specify both a value and set <code>UsePreviousValue</code> to <code>true</code>.)</p> </li> <li> <p>To set an overridden parameter back to the value specified in the stack set, specify a parameter list but don't include the parameter in the list.</p> </li> <li> <p>To leave all parameters set to their present values, don't specify this property at all.</p> </li> </ul> <p>During stack set updates, any parameter values overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only override the parameter <i>values</i> that are specified in the stack set; to add or delete a parameter itself, use <code>UpdateStackSet</code> to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using <code>UpdateStackInstances</code>.</p>
    """

    operation_preferences: typing_extensions.Annotated[
        typing.Optional[UpdateStackInstancesInputOperationPreferences], FieldMetadata(alias="OperationPreferences")
    ] = pydantic.Field(default=None)
    """
    Preferences for how CloudFormation performs this stack set operation.
    """

    operation_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="OperationId")] = (
        pydantic.Field(default=None)
    )
    """
    <p>The unique identifier for this stack set operation.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p>
    """

    call_as: typing_extensions.Annotated[
        typing.Optional[UpdateStackInstancesInputCallAs], FieldMetadata(alias="CallAs")
    ] = pydantic.Field(default=None)
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
