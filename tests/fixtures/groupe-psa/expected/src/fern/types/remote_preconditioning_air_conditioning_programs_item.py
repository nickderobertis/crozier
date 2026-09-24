

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .program import Program
from .remote_preconditioning_air_conditioning_programs_item_actions_type import (
    RemotePreconditioningAirConditioningProgramsItemActionsType,
)


class RemotePreconditioningAirConditioningProgramsItem(Program):
    slot: typing.Optional[int] = pydantic.Field(default=None)
    """
    This program number. Can only be used ONE time in the same preconditioning list.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Determines whether this program is enabled or not.
    """

    actions_type: typing_extensions.Annotated[
        typing.Optional[RemotePreconditioningAirConditioningProgramsItemActionsType],
        FieldMetadata(alias="actionsType"),
        pydantic.Field(
            alias="actionsType",
            description="Action type to apply for this program:\n\n* Delete: Delete this air conditioning program entry. Need only the slot number of the program to remove.  \n* Set: Create a new programe o update it if existing. Need to provide all field correctly set.",
        ),
    ] = None
    """
    Action type to apply for this program:
    
    * Delete: Delete this air conditioning program entry. Need only the slot number of the program to remove.  
    * Set: Create a new programe o update it if existing. Need to provide all field correctly set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
