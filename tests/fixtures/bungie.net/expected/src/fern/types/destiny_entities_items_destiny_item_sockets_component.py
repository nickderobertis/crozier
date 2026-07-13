

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_entities_items_destiny_item_socket_state import DestinyEntitiesItemsDestinyItemSocketState


class DestinyEntitiesItemsDestinyItemSocketsComponent(UniversalBaseModel):
    """
    Instanced items can have sockets, which are slots on the item where plugs can be inserted.
    Sockets are a bit complex: be sure to examine the documentation on the DestinyInventoryItemDefinition's "socket" block and elsewhere on these objects for more details.
    """

    sockets: typing.Optional[typing.List[DestinyEntitiesItemsDestinyItemSocketState]] = pydantic.Field(default=None)
    """
    The list of all sockets on the item, and their status information.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
