

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account import Account
from .delete_stack_instances_input_call_as import DeleteStackInstancesInputCallAs
from .delete_stack_instances_input_deployment_targets import DeleteStackInstancesInputDeploymentTargets
from .delete_stack_instances_input_operation_preferences import DeleteStackInstancesInputOperationPreferences
from .region import Region


class DeleteStackInstancesInput(UniversalBaseModel):
    stack_set_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StackSetName"),
        pydantic.Field(
            alias="StackSetName",
            description="The name or unique ID of the stack set that you want to delete stack instances for.",
        ),
    ]
    """
    The name or unique ID of the stack set that you want to delete stack instances for.
    """

    accounts: typing_extensions.Annotated[
        typing.Optional[typing.List[Account]],
        FieldMetadata(alias="Accounts"),
        pydantic.Field(
            alias="Accounts",
            description="<p>[Self-managed permissions] The names of the Amazon Web Services accounts that you want to delete stack instances for.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>",
        ),
    ] = None
    """
    <p>[Self-managed permissions] The names of the Amazon Web Services accounts that you want to delete stack instances for.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
    """

    deployment_targets: typing_extensions.Annotated[
        typing.Optional[DeleteStackInstancesInputDeploymentTargets],
        FieldMetadata(alias="DeploymentTargets"),
        pydantic.Field(
            alias="DeploymentTargets",
            description="<p>[Service-managed permissions] The Organizations accounts from which to delete stack instances.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>",
        ),
    ] = None
    """
    <p>[Service-managed permissions] The Organizations accounts from which to delete stack instances.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
    """

    regions: typing_extensions.Annotated[
        typing.List[Region],
        FieldMetadata(alias="Regions"),
        pydantic.Field(
            alias="Regions", description="The Amazon Web Services Regions where you want to delete stack set instances."
        ),
    ]
    """
    The Amazon Web Services Regions where you want to delete stack set instances.
    """

    operation_preferences: typing_extensions.Annotated[
        typing.Optional[DeleteStackInstancesInputOperationPreferences],
        FieldMetadata(alias="OperationPreferences"),
        pydantic.Field(
            alias="OperationPreferences",
            description="Preferences for how CloudFormation performs this stack set operation.",
        ),
    ] = None
    """
    Preferences for how CloudFormation performs this stack set operation.
    """

    retain_stacks: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="RetainStacks"),
        pydantic.Field(
            alias="RetainStacks",
            description="<p>Removes the stack instances from the specified stack set, but doesn't delete the stacks. You can't reassociate a retained stack or add an existing, saved stack to a new stack set.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options\">Stack set operation options</a>.</p>",
        ),
    ]
    """
    <p>Removes the stack instances from the specified stack set, but doesn't delete the stacks. You can't reassociate a retained stack or add an existing, saved stack to a new stack set.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options">Stack set operation options</a>.</p>
    """

    operation_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OperationId"),
        pydantic.Field(
            alias="OperationId",
            description="<p>The unique identifier for this stack set operation.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You can retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>Repeating this stack set operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>",
        ),
    ] = None
    """
    <p>The unique identifier for this stack set operation.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You can retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>Repeating this stack set operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>
    """

    call_as: typing_extensions.Annotated[
        typing.Optional[DeleteStackInstancesInputCallAs],
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
