

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetListTypesRequestProvisioningType(str, enum.Enum):
    NON_PROVISIONABLE = "NON_PROVISIONABLE"
    IMMUTABLE = "IMMUTABLE"
    FULLY_MUTABLE = "FULLY_MUTABLE"

    def visit(
        self,
        non_provisionable: typing.Callable[[], T_Result],
        immutable: typing.Callable[[], T_Result],
        fully_mutable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetListTypesRequestProvisioningType.NON_PROVISIONABLE:
            return non_provisionable()
        if self is GetListTypesRequestProvisioningType.IMMUTABLE:
            return immutable()
        if self is GetListTypesRequestProvisioningType.FULLY_MUTABLE:
            return fully_mutable()
