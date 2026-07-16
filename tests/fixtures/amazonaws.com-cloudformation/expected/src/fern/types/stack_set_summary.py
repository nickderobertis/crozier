

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_set_summary_auto_deployment import StackSetSummaryAutoDeployment
from .stack_set_summary_drift_status import StackSetSummaryDriftStatus
from .stack_set_summary_managed_execution import StackSetSummaryManagedExecution
from .stack_set_summary_permission_model import StackSetSummaryPermissionModel
from .stack_set_summary_status import StackSetSummaryStatus


class StackSetSummary(UniversalBaseModel):
    """
    The structures that contain summary information about the specified stack set.
    """

    stack_set_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StackSetName"),
        pydantic.Field(alias="StackSetName", description="The name of the stack set."),
    ] = None
    """
    The name of the stack set.
    """

    stack_set_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StackSetId"),
        pydantic.Field(alias="StackSetId", description="The ID of the stack set."),
    ] = None
    """
    The ID of the stack set.
    """

    description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Description"),
        pydantic.Field(
            alias="Description",
            description="A description of the stack set that you specify when the stack set is created or updated.",
        ),
    ] = None
    """
    A description of the stack set that you specify when the stack set is created or updated.
    """

    status: typing_extensions.Annotated[
        typing.Optional[StackSetSummaryStatus],
        FieldMetadata(alias="Status"),
        pydantic.Field(alias="Status", description="The status of the stack set."),
    ] = None
    """
    The status of the stack set.
    """

    auto_deployment: typing_extensions.Annotated[
        typing.Optional[StackSetSummaryAutoDeployment],
        FieldMetadata(alias="AutoDeployment"),
        pydantic.Field(
            alias="AutoDeployment",
            description="[Service-managed permissions] Describes whether StackSets automatically deploys to Organizations accounts that are added to a target organizational unit (OU).",
        ),
    ] = None
    """
    [Service-managed permissions] Describes whether StackSets automatically deploys to Organizations accounts that are added to a target organizational unit (OU).
    """

    permission_model: typing_extensions.Annotated[
        typing.Optional[StackSetSummaryPermissionModel],
        FieldMetadata(alias="PermissionModel"),
        pydantic.Field(
            alias="PermissionModel",
            description='<p>Describes how the IAM roles required for stack set operations are created.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant Self-Managed Stack Set Permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-service-managed.html">Grant Service-Managed Stack Set Permissions</a>.</p> </li> </ul>',
        ),
    ] = None
    """
    <p>Describes how the IAM roles required for stack set operations are created.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant Self-Managed Stack Set Permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-service-managed.html">Grant Service-Managed Stack Set Permissions</a>.</p> </li> </ul>
    """

    drift_status: typing_extensions.Annotated[
        typing.Optional[StackSetSummaryDriftStatus],
        FieldMetadata(alias="DriftStatus"),
        pydantic.Field(
            alias="DriftStatus",
            description="<p>Status of the stack set's actual configuration compared to its expected template and parameter configuration. A stack set is considered to have drifted if one or more of its stack instances have drifted from their expected template and parameter configuration.</p> <ul> <li> <p> <code>DRIFTED</code>: One or more of the stack instances belonging to the stack set stack differs from the expected template and parameter configuration. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation hasn't checked the stack set for drift.</p> </li> <li> <p> <code>IN_SYNC</code>: All the stack instances belonging to the stack set stack match from the expected template and parameter configuration.</p> </li> <li> <p> <code>UNKNOWN</code>: This value is reserved for future use.</p> </li> </ul>",
        ),
    ] = None
    """
    <p>Status of the stack set's actual configuration compared to its expected template and parameter configuration. A stack set is considered to have drifted if one or more of its stack instances have drifted from their expected template and parameter configuration.</p> <ul> <li> <p> <code>DRIFTED</code>: One or more of the stack instances belonging to the stack set stack differs from the expected template and parameter configuration. A stack instance is considered to have drifted if one or more of the resources in the associated stack have drifted.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation hasn't checked the stack set for drift.</p> </li> <li> <p> <code>IN_SYNC</code>: All the stack instances belonging to the stack set stack match from the expected template and parameter configuration.</p> </li> <li> <p> <code>UNKNOWN</code>: This value is reserved for future use.</p> </li> </ul>
    """

    last_drift_check_timestamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="LastDriftCheckTimestamp"),
        pydantic.Field(
            alias="LastDriftCheckTimestamp",
            description="Most recent time when CloudFormation performed a drift detection operation on the stack set. This value will be <code>NULL</code> for any stack set on which drift detection hasn't yet been performed.",
        ),
    ] = None
    """
    Most recent time when CloudFormation performed a drift detection operation on the stack set. This value will be <code>NULL</code> for any stack set on which drift detection hasn't yet been performed.
    """

    managed_execution: typing_extensions.Annotated[
        typing.Optional[StackSetSummaryManagedExecution],
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
