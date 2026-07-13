

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_character_destiny_item_peer_view import DestinyCharacterDestinyItemPeerView


class DestinyCharacterDestinyCharacterPeerView(UniversalBaseModel):
    """
    A minimal view of a character's equipped items, for the purpose of rendering a summary screen or showing the character in 3D.
    """

    equipment: typing.Optional[typing.List[DestinyCharacterDestinyItemPeerView]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
