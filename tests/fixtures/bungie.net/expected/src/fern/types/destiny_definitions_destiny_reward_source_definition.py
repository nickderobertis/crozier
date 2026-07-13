

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)


class DestinyDefinitionsDestinyRewardSourceDefinition(UniversalBaseModel):
    """
    Represents a heuristically-determined "item source" according to Bungie.net. These item sources are non-canonical: we apply a combination of special configuration and often-fragile heuristics to attempt to discern whether an item should be part of a given "source," but we have known cases of false positives and negatives due to our imperfect heuristics.
    Still, they provide a decent approximation for people trying to figure out how an item can be obtained. DestinyInventoryItemDefinition refers to sources in the sourceDatas.sourceHashes property for all sources we determined the item could spawn from.
    An example in Destiny 1 of a Source would be "Nightfall". If an item has the "Nightfall" source associated with it, it's extremely likely that you can earn that item while playing Nightfall, either during play or as an after-completion reward.
    """

    category: typing.Optional[int] = pydantic.Field(default=None)
    """
    Sources are grouped into categories: common ways that items are provided. I hope to see this expand in Destiny 2 once we have time to generate accurate reward source data.
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
