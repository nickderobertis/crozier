

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doors_state_base_opening_item_identifier import DoorsStateBaseOpeningItemIdentifier
from .doors_state_base_opening_item_state import DoorsStateBaseOpeningItemState


class DoorsStateBaseOpeningItem(UniversalBaseModel):
    """
    Opening state per door.
    """

    identifier: typing.Optional[DoorsStateBaseOpeningItemIdentifier] = None
    state: typing.Optional[DoorsStateBaseOpeningItemState] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
