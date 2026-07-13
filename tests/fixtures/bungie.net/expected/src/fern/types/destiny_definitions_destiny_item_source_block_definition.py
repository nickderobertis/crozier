

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_item_vendor_source_reference import DestinyDefinitionsDestinyItemVendorSourceReference
from .destiny_definitions_sources_destiny_item_source_definition import (
    DestinyDefinitionsSourcesDestinyItemSourceDefinition,
)


class DestinyDefinitionsDestinyItemSourceBlockDefinition(UniversalBaseModel):
    """
    Data about an item's "sources": ways that the item can be obtained.
    """

    exclusive: typing.Optional[int] = pydantic.Field(default=None)
    """
    If we found that this item is exclusive to a specific platform, this will be set to the BungieMembershipType enumeration that matches that platform.
    """

    source_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="sourceHashes")
    ] = pydantic.Field(default=None)
    """
    The list of hash identifiers for Reward Sources that hint where the item can be found (DestinyRewardSourceDefinition).
    """

    sources: typing.Optional[typing.List[DestinyDefinitionsSourcesDestinyItemSourceDefinition]] = pydantic.Field(
        default=None
    )
    """
    A collection of details about the stats that were computed for the ways we found that the item could be spawned.
    """

    vendor_sources: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyItemVendorSourceReference]],
        FieldMetadata(alias="vendorSources"),
    ] = pydantic.Field(default=None)
    """
    A denormalized reference back to vendors that potentially sell this item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
