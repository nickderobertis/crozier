

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doors_state_base_locked_states_item import DoorsStateBaseLockedStatesItem
from .doors_state_base_opening_item import DoorsStateBaseOpeningItem


class DoorsStateBase(UniversalBaseModel):
    locked_states: typing_extensions.Annotated[
        typing.Optional[typing.List[DoorsStateBaseLockedStatesItem]],
        FieldMetadata(alias="lockedStates"),
        pydantic.Field(alias="lockedStates", description="List of all known doors' states"),
    ] = None
    """
    List of all known doors' states
    """

    opening: typing.Optional[typing.List[DoorsStateBaseOpeningItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
