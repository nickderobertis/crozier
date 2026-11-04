

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PermissionSetWithRequirementRequirementType(enum.StrEnum):
    """
    Whether this permission set is mandatory or optional for the agent
    """

    MANDATORY = "mandatory"
    OPTIONAL = "optional"

    def visit(self, mandatory: typing.Callable[[], T_Result], optional: typing.Callable[[], T_Result]) -> T_Result:
        if self is PermissionSetWithRequirementRequirementType.MANDATORY:
            return mandatory()
        if self is PermissionSetWithRequirementRequirementType.OPTIONAL:
            return optional()
