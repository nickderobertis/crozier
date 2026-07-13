

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_sockets_destiny_item_plug import DestinySocketsDestinyItemPlug


class DestinyComponentsPlugSetsDestinyPlugSetsComponent(UniversalBaseModel):
    """
    Sockets may refer to a "Plug Set": a set of reusable plugs that may be shared across multiple sockets (or even, in theory, multiple sockets over multiple items).
    This is the set of those plugs that we came across in the users' inventory, along with the values for plugs in the set. Any given set in this component may be represented in Character and Profile-level, as some plugs may be Profile-level restricted, and some character-level restricted. (note that the ones that are even more specific will remain on the actual socket component itself, as they cannot be reused)
    """

    plugs: typing.Optional[typing.Dict[str, typing.List[DestinySocketsDestinyItemPlug]]] = pydantic.Field(default=None)
    """
    The shared list of plugs for each relevant PlugSet, keyed by the hash identifier of the PlugSet (DestinyPlugSetDefinition).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
