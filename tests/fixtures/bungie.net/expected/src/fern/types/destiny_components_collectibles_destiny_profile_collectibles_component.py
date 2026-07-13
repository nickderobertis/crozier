

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_components_collectibles_destiny_collectible_component import (
    DestinyComponentsCollectiblesDestinyCollectibleComponent,
)


class DestinyComponentsCollectiblesDestinyProfileCollectiblesComponent(UniversalBaseModel):
    collectibles: typing.Optional[typing.Dict[str, DestinyComponentsCollectiblesDestinyCollectibleComponent]] = None
    collection_badges_root_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="collectionBadgesRootNodeHash")
    ] = pydantic.Field(default=None)
    """
    The hash for the root presentation node definition of Collection Badges.
    """

    collection_categories_root_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="collectionCategoriesRootNodeHash")
    ] = pydantic.Field(default=None)
    """
    The hash for the root presentation node definition of Collection categories.
    """

    newness_flagged_collectible_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="newnessFlaggedCollectibleHashes")
    ] = pydantic.Field(default=None)
    """
    The list of collectibles determined by the game as having been "recently" acquired.
    The game client itself actually controls this data, so I personally question whether anyone will get much use out of this: because we can't edit this value through the API. But in case anyone finds it useful, here it is.
    """

    recent_collectible_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="recentCollectibleHashes")
    ] = pydantic.Field(default=None)
    """
    The list of collectibles determined by the game as having been "recently" acquired.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
