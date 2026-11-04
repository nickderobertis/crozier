

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceRequirementForUserRequirementType(enum.StrEnum):
    """
    Whether this service is required or optional for the agent
    """

    MANDATORY = "mandatory"
    OPTIONAL = "optional"

    def visit(self, mandatory: typing.Callable[[], T_Result], optional: typing.Callable[[], T_Result]) -> T_Result:
        if self is ServiceRequirementForUserRequirementType.MANDATORY:
            return mandatory()
        if self is ServiceRequirementForUserRequirementType.OPTIONAL:
            return optional()
