

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DescribeTypeOutputProvisioningType(str, enum.Enum):
    """
    <p>For resource type extensions, the provisioning behavior of the resource type. CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.</p> <p>Valid values include:</p> <ul> <li> <p> <code>FULLY_MUTABLE</code>: The resource type includes an update handler to process updates to the type during stack update operations.</p> </li> <li> <p> <code>IMMUTABLE</code>: The resource type doesn't include an update handler, so the type can't be updated and must instead be replaced during stack update operations.</p> </li> <li> <p> <code>NON_PROVISIONABLE</code>: The resource type doesn't include all the following handlers, and therefore can't actually be provisioned.</p> <ul> <li> <p>create</p> </li> <li> <p>read</p> </li> <li> <p>delete</p> </li> </ul> </li> </ul>
    """

    NON_PROVISIONABLE = "NON_PROVISIONABLE"
    IMMUTABLE = "IMMUTABLE"
    FULLY_MUTABLE = "FULLY_MUTABLE"

    def visit(
        self,
        non_provisionable: typing.Callable[[], T_Result],
        immutable: typing.Callable[[], T_Result],
        fully_mutable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DescribeTypeOutputProvisioningType.NON_PROVISIONABLE:
            return non_provisionable()
        if self is DescribeTypeOutputProvisioningType.IMMUTABLE:
            return immutable()
        if self is DescribeTypeOutputProvisioningType.FULLY_MUTABLE:
            return fully_mutable()
