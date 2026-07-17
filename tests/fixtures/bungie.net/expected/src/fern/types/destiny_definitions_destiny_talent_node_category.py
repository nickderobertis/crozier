

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)


class DestinyDefinitionsDestinyTalentNodeCategory(UniversalBaseModel):
    """
    An artificial construct provided by Bungie.Net, where we attempt to group talent nodes by functionality.
    This is a single set of references to Talent Nodes that share a common trait or purpose.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(
            alias="displayProperties",
            description='Will contain at least the "name", which will be the title of the category. We will likely not have description and an icon yet, but I\'m going to keep my options open.',
        ),
    ] = None
    """
    Will contain at least the "name", which will be the title of the category. We will likely not have description and an icon yet, but I'm going to keep my options open.
    """

    identifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    Mostly just for debug purposes, but if you find it useful you can have it. This is BNet's manually created identifier for this category.
    """

    is_lore_driven: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isLoreDriven"),
        pydantic.Field(
            alias="isLoreDriven",
            description="If true, we found the localized content in a related DestinyLoreDefinition instead of local BNet localization files. This is mostly for ease of my own future investigations.",
        ),
    ] = None
    """
    If true, we found the localized content in a related DestinyLoreDefinition instead of local BNet localization files. This is mostly for ease of my own future investigations.
    """

    node_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="nodeHashes"),
        pydantic.Field(
            alias="nodeHashes",
            description="The set of all hash identifiers for Talent Nodes (DestinyTalentNodeDefinition) in this Talent Grid that are part of this Category.",
        ),
    ] = None
    """
    The set of all hash identifiers for Talent Nodes (DestinyTalentNodeDefinition) in this Talent Grid that are part of this Category.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
