

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CapabilityAccountRequirementRequirement(enum.StrEnum):
    NONE = "none"
    OPTIONAL = "optional"
    REQUIRED = "required"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        optional: typing.Callable[[], T_Result],
        required: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CapabilityAccountRequirementRequirement.NONE:
            return none()
        if self is CapabilityAccountRequirementRequirement.OPTIONAL:
            return optional()
        if self is CapabilityAccountRequirementRequirement.REQUIRED:
            return required()
