

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RemotePreconditioningAirConditioningProgramsItemActionsType(enum.StrEnum):
    """
    Action type to apply for this program:

    * Delete: Delete this air conditioning program entry. Need only the slot number of the program to remove.
    * Set: Create a new programe o update it if existing. Need to provide all field correctly set.
    """

    DELETE = "Delete"
    SET = "Set"

    def visit(self, delete: typing.Callable[[], T_Result], set_: typing.Callable[[], T_Result]) -> T_Result:
        if self is RemotePreconditioningAirConditioningProgramsItemActionsType.DELETE:
            return delete()
        if self is RemotePreconditioningAirConditioningProgramsItemActionsType.SET:
            return set_()
