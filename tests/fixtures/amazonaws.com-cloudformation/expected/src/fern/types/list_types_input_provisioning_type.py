

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListTypesInputProvisioningType(enum.StrEnum):
    """
    <p>For resource types, the provisioning behavior of the resource type. CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.</p> <p>Valid values include:</p> <ul> <li> <p> <code>FULLY_MUTABLE</code>: The resource type includes an update handler to process updates to the type during stack update operations.</p> </li> <li> <p> <code>IMMUTABLE</code>: The resource type doesn't include an update handler, so the type can't be updated and must instead be replaced during stack update operations.</p> </li> <li> <p> <code>NON_PROVISIONABLE</code>: The resource type doesn't include create, read, and delete handlers, and therefore can't actually be provisioned.</p> </li> </ul> <p>The default is <code>FULLY_MUTABLE</code>.</p>
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
        if self is ListTypesInputProvisioningType.NON_PROVISIONABLE:
            return non_provisionable()
        if self is ListTypesInputProvisioningType.IMMUTABLE:
            return immutable()
        if self is ListTypesInputProvisioningType.FULLY_MUTABLE:
            return fully_mutable()
