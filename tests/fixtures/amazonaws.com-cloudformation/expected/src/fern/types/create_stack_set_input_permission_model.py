

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CreateStackSetInputPermissionModel(str, enum.Enum):
    """
    <p>Describes how the IAM roles required for stack set operations are created. By default, <code>SELF-MANAGED</code> is specified.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant Self-Managed Stack Set Permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-service-managed.html">Grant Service-Managed Stack Set Permissions</a>.</p> </li> </ul>
    """

    SERVICE_MANAGED = "SERVICE_MANAGED"
    SELF_MANAGED = "SELF_MANAGED"

    def visit(
        self, service_managed: typing.Callable[[], T_Result], self_managed: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is CreateStackSetInputPermissionModel.SERVICE_MANAGED:
            return service_managed()
        if self is CreateStackSetInputPermissionModel.SELF_MANAGED:
            return self_managed()
