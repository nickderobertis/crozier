

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_item_component_set_ofuint32 import DestinyItemComponentSetOfuint32
from .single_component_response_of_destiny_collectibles_component import (
    SingleComponentResponseOfDestinyCollectiblesComponent,
)


class DestinyResponsesDestinyCollectibleNodeDetailResponse(UniversalBaseModel):
    """
    Returns the detailed information about a Collectible Presentation Node and any Collectibles that are direct descendants.
    """

    collectible_item_components: typing_extensions.Annotated[
        typing.Optional[DestinyItemComponentSetOfuint32],
        FieldMetadata(alias="collectibleItemComponents"),
        pydantic.Field(
            alias="collectibleItemComponents",
            description="Item components, keyed by the item hash of the items pointed at collectibles found under the requested Presentation Node.\r\nNOTE: I had a lot of hemming and hawing about whether these should be keyed by collectible hash or item hash... but ultimately having it be keyed by item hash meant that UI that already uses DestinyItemComponentSet data wouldn't have to have a special override to do the collectible -> item lookup once you delve into an item's details, and it also meant that you didn't have to remember that the Hash being used as the key for plugSets was different from the Hash being used for the other Dictionaries. As a result, using the Item Hash felt like the least crappy solution.\r\nWe may all come to regret this decision. We will see.\r\nCOMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]",
        ),
    ] = None
    """
    Item components, keyed by the item hash of the items pointed at collectibles found under the requested Presentation Node.
    NOTE: I had a lot of hemming and hawing about whether these should be keyed by collectible hash or item hash... but ultimately having it be keyed by item hash meant that UI that already uses DestinyItemComponentSet data wouldn't have to have a special override to do the collectible -> item lookup once you delve into an item's details, and it also meant that you didn't have to remember that the Hash being used as the key for plugSets was different from the Hash being used for the other Dictionaries. As a result, using the Item Hash felt like the least crappy solution.
    We may all come to regret this decision. We will see.
    COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]
    """

    collectibles: typing.Optional[SingleComponentResponseOfDestinyCollectiblesComponent] = pydantic.Field(default=None)
    """
    COMPONENT TYPE: Collectibles
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
