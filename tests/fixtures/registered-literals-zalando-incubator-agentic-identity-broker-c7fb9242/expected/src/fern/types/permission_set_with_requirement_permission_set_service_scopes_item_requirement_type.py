

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PermissionSetWithRequirementPermissionSetServiceScopesItemRequirementType(enum.StrEnum):
    """
    Whether this service is mandatory or optional within the permission set. Raw scopes are intentionally omitted; the frontend uses this field to determine lock status (FR-007).
    """

    MANDATORY = "mandatory"
    OPTIONAL = "optional"

    def visit(self, mandatory: typing.Callable[[], T_Result], optional: typing.Callable[[], T_Result]) -> T_Result:
        if self is PermissionSetWithRequirementPermissionSetServiceScopesItemRequirementType.MANDATORY:
            return mandatory()
        if self is PermissionSetWithRequirementPermissionSetServiceScopesItemRequirementType.OPTIONAL:
            return optional()
