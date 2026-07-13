

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_components_collectibles_destiny_collectible_component import (
    DestinyComponentsCollectiblesDestinyCollectibleComponent,
)


class DestinyComponentsCollectiblesDestinyCollectiblesComponent(UniversalBaseModel):
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
