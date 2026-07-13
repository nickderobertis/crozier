

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_misc_destiny_color import DestinyMiscDestinyColor


class DestinyDefinitionsSocialDestinySocialCommendationNodeDefinition(UniversalBaseModel):
    child_commendation_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="childCommendationHashes")
    ] = pydantic.Field(default=None)
    """
    A list of hashes that map to child commendations.
    """

    child_commendation_node_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="childCommendationNodeHashes")
    ] = pydantic.Field(default=None)
    """
    A list of hashes that map to child commendation nodes. Only the root commendations node is expected to have child nodes.
    """

    color: typing.Optional[DestinyMiscDestinyColor] = pydantic.Field(default=None)
    """
    The color associated with this group of commendations.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
    ] = None
    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    parent_commendation_node_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="parentCommendationNodeHash")
    ] = None
    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
