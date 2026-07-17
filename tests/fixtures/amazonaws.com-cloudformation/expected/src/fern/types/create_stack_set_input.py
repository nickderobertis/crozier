

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .capability import Capability
from .create_stack_set_input_auto_deployment import CreateStackSetInputAutoDeployment
from .create_stack_set_input_call_as import CreateStackSetInputCallAs
from .create_stack_set_input_managed_execution import CreateStackSetInputManagedExecution
from .create_stack_set_input_permission_model import CreateStackSetInputPermissionModel
from .parameter import Parameter
from .tag import Tag


class CreateStackSetInput(UniversalBaseModel):
    stack_set_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StackSetName"),
        pydantic.Field(
            alias="StackSetName",
            description="<p>The name to associate with the stack set. The name must be unique in the Region where you create your stack set.</p> <note> <p>A stack name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and can't be longer than 128 characters.</p> </note>",
        ),
    ]
    """
    <p>The name to associate with the stack set. The name must be unique in the Region where you create your stack set.</p> <note> <p>A stack name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and can't be longer than 128 characters.</p> </note>
    """

    description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Description"),
        pydantic.Field(
            alias="Description",
            description="A description of the stack set. You can use the description to identify the stack set's purpose or other important information.",
        ),
    ] = None
    """
    A description of the stack set. You can use the description to identify the stack set's purpose or other important information.
    """

    template_body: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TemplateBody"),
        pydantic.Field(
            alias="TemplateBody",
            description='<p>The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.</p>',
        ),
    ] = None
    """
    <p>The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.</p>
    """

    template_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TemplateURL"),
        pydantic.Field(
            alias="TemplateURL",
            description='<p>The location of the file that contains the template body. The URL must point to a template (maximum size: 460,800 bytes) that\'s located in an Amazon S3 bucket or a Systems Manager document. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.</p>',
        ),
    ] = None
    """
    <p>The location of the file that contains the template body. The URL must point to a template (maximum size: 460,800 bytes) that's located in an Amazon S3 bucket or a Systems Manager document. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.</p>
    """

    stack_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StackId"),
        pydantic.Field(
            alias="StackId",
            description="The stack ID you are importing into a new stack set. Specify the Amazon Resource Name (ARN) of the stack.",
        ),
    ] = None
    """
    The stack ID you are importing into a new stack set. Specify the Amazon Resource Name (ARN) of the stack.
    """

    parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[Parameter]],
        FieldMetadata(alias="Parameters"),
        pydantic.Field(alias="Parameters", description="The input parameters for the stack set template."),
    ] = None
    """
    The input parameters for the stack set template.
    """

    capabilities: typing_extensions.Annotated[
        typing.Optional[typing.List[Capability]],
        FieldMetadata(alias="Capabilities"),
        pydantic.Field(
            alias="Capabilities",
            description='<p>In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for CloudFormation to create the stack set and related stack instances.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stack sets, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don\'t specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some templates reference macros. If your stack set template references one or more macros, you must create the stack set directly from the processed template, without first reviewing the resulting changes in a change set. To create the stack set directly, you must acknowledge this capability. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation Macros to Perform Custom Processing on Templates</a>.</p> <important> <p>Stack sets with service-managed permissions don\'t currently support the use of macros in templates. (This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.) Even if you specify this capability for a stack set with service-managed permissions, if you reference a macro in your template the stack set operation will fail.</p> </important> </li> </ul>',
        ),
    ] = None
    """
    <p>In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for CloudFormation to create the stack set and related stack instances.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stack sets, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some templates reference macros. If your stack set template references one or more macros, you must create the stack set directly from the processed template, without first reviewing the resulting changes in a change set. To create the stack set directly, you must acknowledge this capability. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation Macros to Perform Custom Processing on Templates</a>.</p> <important> <p>Stack sets with service-managed permissions don't currently support the use of macros in templates. (This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.) Even if you specify this capability for a stack set with service-managed permissions, if you reference a macro in your template the stack set operation will fail.</p> </important> </li> </ul>
    """

    tags: typing_extensions.Annotated[
        typing.Optional[typing.List[Tag]],
        FieldMetadata(alias="Tags"),
        pydantic.Field(
            alias="Tags",
            description="<p>The key-value pairs to associate with this stack set and the stacks created from it. CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.</p> <p>If you specify tags as part of a <code>CreateStackSet</code> action, CloudFormation checks to see if you have the required IAM permission to tag resources. If you don't, the entire <code>CreateStackSet</code> action fails with an <code>access denied</code> error, and the stack set is not created.</p>",
        ),
    ] = None
    """
    <p>The key-value pairs to associate with this stack set and the stacks created from it. CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.</p> <p>If you specify tags as part of a <code>CreateStackSet</code> action, CloudFormation checks to see if you have the required IAM permission to tag resources. If you don't, the entire <code>CreateStackSet</code> action fails with an <code>access denied</code> error, and the stack set is not created.</p>
    """

    administration_role_arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AdministrationRoleARN"),
        pydantic.Field(
            alias="AdministrationRoleARN",
            description='<p>The Amazon Resource Name (ARN) of the IAM role to use to create this stack set.</p> <p>Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html">Prerequisites: Granting Permissions for Stack Set Operations</a> in the <i>CloudFormation User Guide</i>.</p>',
        ),
    ] = None
    """
    <p>The Amazon Resource Name (ARN) of the IAM role to use to create this stack set.</p> <p>Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html">Prerequisites: Granting Permissions for Stack Set Operations</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    execution_role_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ExecutionRoleName"),
        pydantic.Field(
            alias="ExecutionRoleName",
            description="<p>The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, CloudFormation uses the <code>AWSCloudFormationStackSetExecutionRole</code> role for the stack set operation.</p> <p>Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their stack sets.</p>",
        ),
    ] = None
    """
    <p>The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, CloudFormation uses the <code>AWSCloudFormationStackSetExecutionRole</code> role for the stack set operation.</p> <p>Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their stack sets.</p>
    """

    permission_model: typing_extensions.Annotated[
        typing.Optional[CreateStackSetInputPermissionModel],
        FieldMetadata(alias="PermissionModel"),
        pydantic.Field(
            alias="PermissionModel",
            description='<p>Describes how the IAM roles required for stack set operations are created. By default, <code>SELF-MANAGED</code> is specified.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant Self-Managed Stack Set Permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-service-managed.html">Grant Service-Managed Stack Set Permissions</a>.</p> </li> </ul>',
        ),
    ] = None
    """
    <p>Describes how the IAM roles required for stack set operations are created. By default, <code>SELF-MANAGED</code> is specified.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant Self-Managed Stack Set Permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-service-managed.html">Grant Service-Managed Stack Set Permissions</a>.</p> </li> </ul>
    """

    auto_deployment: typing_extensions.Annotated[
        typing.Optional[CreateStackSetInputAutoDeployment],
        FieldMetadata(alias="AutoDeployment"),
        pydantic.Field(
            alias="AutoDeployment",
            description="Describes whether StackSets automatically deploys to Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if <code>PermissionModel</code> is <code>SERVICE_MANAGED</code>.",
        ),
    ] = None
    """
    Describes whether StackSets automatically deploys to Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if <code>PermissionModel</code> is <code>SERVICE_MANAGED</code>.
    """

    call_as: typing_extensions.Annotated[
        typing.Optional[CreateStackSetInputCallAs],
        FieldMetadata(alias="CallAs"),
        pydantic.Field(
            alias="CallAs",
            description='<p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization\'s management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>To create a stack set with service-managed permissions while signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>To create a stack set with service-managed permissions while signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated admin in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul> <p>Stack sets with service-managed permissions are created in the management account, including stack sets that are created by delegated administrators.</p>',
        ),
    ] = None
    """
    <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>To create a stack set with service-managed permissions while signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>To create a stack set with service-managed permissions while signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated admin in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul> <p>Stack sets with service-managed permissions are created in the management account, including stack sets that are created by delegated administrators.</p>
    """

    client_request_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ClientRequestToken"),
        pydantic.Field(
            alias="ClientRequestToken",
            description="<p>A unique identifier for this <code>CreateStackSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create another stack set with the same name. You might retry <code>CreateStackSet</code> requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p>",
        ),
    ] = None
    """
    <p>A unique identifier for this <code>CreateStackSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create another stack set with the same name. You might retry <code>CreateStackSet</code> requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p>
    """

    managed_execution: typing_extensions.Annotated[
        typing.Optional[CreateStackSetInputManagedExecution],
        FieldMetadata(alias="ManagedExecution"),
        pydantic.Field(
            alias="ManagedExecution",
            description="Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.",
        ),
    ] = None
    """
    Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
