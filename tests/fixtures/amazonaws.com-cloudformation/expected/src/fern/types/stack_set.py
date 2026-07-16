

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .capability import Capability
from .organizational_unit_id import OrganizationalUnitId
from .parameter import Parameter
from .region_list import RegionList
from .stack_set_auto_deployment import StackSetAutoDeployment
from .stack_set_managed_execution import StackSetManagedExecution
from .stack_set_permission_model import StackSetPermissionModel
from .stack_set_stack_set_drift_detection_details import StackSetStackSetDriftDetectionDetails
from .stack_set_status import StackSetStatus
from .tag import Tag


class StackSet(UniversalBaseModel):
    """
    A structure that contains information about a stack set. A stack set enables you to provision stacks into Amazon Web Services accounts and across Regions by using a single CloudFormation template. In the stack set, you specify the template to use, in addition to any parameters and capabilities that the template requires.
    """

    stack_set_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackSetName")] = (
        pydantic.Field(default=None)
    )
    """
    The name that's associated with the stack set.
    """

    stack_set_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackSetId")] = pydantic.Field(
        default=None
    )
    """
    The ID of the stack set.
    """

    description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Description")] = pydantic.Field(
        default=None
    )
    """
    A description of the stack set that you specify when the stack set is created or updated.
    """

    status: typing_extensions.Annotated[typing.Optional[StackSetStatus], FieldMetadata(alias="Status")] = (
        pydantic.Field(default=None)
    )
    """
    The status of the stack set.
    """

    template_body: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TemplateBody")] = (
        pydantic.Field(default=None)
    )
    """
    The structure that contains the body of the template that was used to create or update the stack set.
    """

    parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[Parameter]], FieldMetadata(alias="Parameters")
    ] = pydantic.Field(default=None)
    """
    A list of input parameters for a stack set.
    """

    capabilities: typing_extensions.Annotated[
        typing.Optional[typing.List[Capability]], FieldMetadata(alias="Capabilities")
    ] = pydantic.Field(default=None)
    """
    The capabilities that are allowed in the stack set. Some stack set templates might include resources that can affect permissions in your Amazon Web Services account—for example, by creating new Identity and Access Management (IAM) users. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates.</a> 
    """

    tags: typing_extensions.Annotated[typing.Optional[typing.List[Tag]], FieldMetadata(alias="Tags")] = pydantic.Field(
        default=None
    )
    """
    A list of tags that specify information about the stack set. A maximum number of 50 tags can be specified.
    """

    stack_set_arn: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StackSetARN")] = (
        pydantic.Field(default=None)
    )
    """
    The Amazon Resource Name (ARN) of the stack set.
    """

    administration_role_arn: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="AdministrationRoleARN")
    ] = pydantic.Field(default=None)
    """
    <p>The Amazon Resource Name (ARN) of the IAM role used to create or update the stack set.</p> <p>Use customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html">Prerequisites: Granting Permissions for Stack Set Operations</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    execution_role_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ExecutionRoleName")] = (
        pydantic.Field(default=None)
    )
    """
    <p>The name of the IAM execution role used to create or update the stack set.</p> <p>Use customized execution roles to control which stack resources users and groups can include in their stack sets.</p>
    """

    stack_set_drift_detection_details: typing_extensions.Annotated[
        typing.Optional[StackSetStackSetDriftDetectionDetails], FieldMetadata(alias="StackSetDriftDetectionDetails")
    ] = pydantic.Field(default=None)
    """
    <p>Detailed information about the drift status of the stack set.</p> <p>For stack sets, contains information about the last <i>completed</i> drift operation performed on the stack set. Information about drift operations currently in progress isn't included.</p>
    """

    auto_deployment: typing_extensions.Annotated[
        typing.Optional[StackSetAutoDeployment], FieldMetadata(alias="AutoDeployment")
    ] = pydantic.Field(default=None)
    """
    [Service-managed permissions] Describes whether StackSets automatically deploys to Organizations accounts that are added to a target organization or organizational unit (OU).
    """

    permission_model: typing_extensions.Annotated[
        typing.Optional[StackSetPermissionModel], FieldMetadata(alias="PermissionModel")
    ] = pydantic.Field(default=None)
    """
    <p>Describes how the IAM roles required for stack set operations are created.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant Self-Managed Stack Set Permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-service-managed.html">Grant Service-Managed Stack Set Permissions</a>.</p> </li> </ul>
    """

    organizational_unit_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[OrganizationalUnitId]], FieldMetadata(alias="OrganizationalUnitIds")
    ] = pydantic.Field(default=None)
    """
    [Service-managed permissions] The organization root ID or organizational unit (OU) IDs that you specified for <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeploymentTargets.html">DeploymentTargets</a>.
    """

    managed_execution: typing_extensions.Annotated[
        typing.Optional[StackSetManagedExecution], FieldMetadata(alias="ManagedExecution")
    ] = pydantic.Field(default=None)
    """
    Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
    """

    regions: typing_extensions.Annotated[typing.Optional[RegionList], FieldMetadata(alias="Regions")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
