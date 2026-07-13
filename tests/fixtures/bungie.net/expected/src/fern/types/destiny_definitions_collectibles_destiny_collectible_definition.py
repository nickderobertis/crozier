

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_collectibles_destiny_collectible_acquisition_block import (
    DestinyDefinitionsCollectiblesDestinyCollectibleAcquisitionBlock,
)
from .destiny_definitions_collectibles_destiny_collectible_state_block import (
    DestinyDefinitionsCollectiblesDestinyCollectibleStateBlock,
)
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_presentation_destiny_presentation_child_block import (
    DestinyDefinitionsPresentationDestinyPresentationChildBlock,
)


class DestinyDefinitionsCollectiblesDestinyCollectibleDefinition(UniversalBaseModel):
    """
    Defines a
    """

    acquisition_info: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCollectiblesDestinyCollectibleAcquisitionBlock],
        FieldMetadata(alias="acquisitionInfo"),
    ] = None
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

    item_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="itemHash")] = None
    parent_node_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="parentNodeHashes")
    ] = pydantic.Field(default=None)
    """
    A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
    """

    presentation_info: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsPresentationDestinyPresentationChildBlock],
        FieldMetadata(alias="presentationInfo"),
    ] = None
    presentation_node_type: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="presentationNodeType")
    ] = None
    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    scope: typing.Optional[int] = pydantic.Field(default=None)
    """
    Indicates whether the state of this Collectible is determined on a per-character or on an account-wide basis.
    """

    source_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="sourceHash")] = pydantic.Field(
        default=None
    )
    """
    This is a hash identifier we are building on the BNet side in an attempt to let people group collectibles by similar sources.
    I can't promise that it's going to be 100% accurate, but if the designers were consistent in assigning the same source strings to items with the same sources, it *ought to* be. No promises though.
    This hash also doesn't relate to an actual definition, just to note: we've got nothing useful other than the source string for this data.
    """

    source_string: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="sourceString")] = (
        pydantic.Field(default=None)
    )
    """
    A human readable string for a hint about how to acquire the item.
    """

    state_info: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCollectiblesDestinyCollectibleStateBlock], FieldMetadata(alias="stateInfo")
    ] = None
    trait_hashes: typing_extensions.Annotated[typing.Optional[typing.List[int]], FieldMetadata(alias="traitHashes")] = (
        None
    )
    trait_ids: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="traitIds")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
