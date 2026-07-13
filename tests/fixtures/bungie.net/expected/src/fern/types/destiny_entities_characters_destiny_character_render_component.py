

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_character_destiny_character_customization import DestinyCharacterDestinyCharacterCustomization
from .destiny_character_destiny_character_peer_view import DestinyCharacterDestinyCharacterPeerView
from .destiny_dye_reference import DestinyDyeReference


class DestinyEntitiesCharactersDestinyCharacterRenderComponent(UniversalBaseModel):
    """
    Only really useful if you're attempting to render the character's current appearance in 3D, this returns a bare minimum of information, pre-aggregated, that you'll need to perform that rendering. Note that you need to combine this with other 3D assets and data from our servers.
    Examine the Javascript returned by https://bungie.net/sharedbundle/spasm to see how we use this data, but be warned: the rabbit hole goes pretty deep.
    """

    custom_dyes: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDyeReference]], FieldMetadata(alias="customDyes")
    ] = pydantic.Field(default=None)
    """
    Custom dyes, calculated by iterating over the character's equipped items. Useful for pre-fetching all of the dye data needed from our server.
    """

    customization: typing.Optional[DestinyCharacterDestinyCharacterCustomization] = pydantic.Field(default=None)
    """
    This is actually something that Spasm.js *doesn't* do right now, and that we don't return assets for yet. This is the data about what character customization options you picked. You can combine this with DestinyCharacterCustomizationOptionDefinition to show some cool info, and hopefully someday to actually render a user's face in 3D. We'll see if we ever end up with time for that.
    """

    peer_view: typing_extensions.Annotated[
        typing.Optional[DestinyCharacterDestinyCharacterPeerView], FieldMetadata(alias="peerView")
    ] = pydantic.Field(default=None)
    """
    A minimal view of:
    - Equipped items
    - The rendering-related custom options on those equipped items
    Combined, that should be enough to render all of the items on the equipped character.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
