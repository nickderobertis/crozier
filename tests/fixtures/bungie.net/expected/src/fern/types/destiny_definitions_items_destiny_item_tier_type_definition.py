

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_items_destiny_item_tier_type_infusion_block import (
    DestinyDefinitionsItemsDestinyItemTierTypeInfusionBlock,
)


class DestinyDefinitionsItemsDestinyItemTierTypeDefinition(UniversalBaseModel):
    """
    Defines the tier type of an item. Mostly this provides human readable properties for types like Common, Rare, etc...
    It also provides some base data for infusion that could be useful.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(alias="displayProperties"),
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

    infusion_process: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsItemsDestinyItemTierTypeInfusionBlock],
        FieldMetadata(alias="infusionProcess"),
        pydantic.Field(
            alias="infusionProcess",
            description="If this tier defines infusion properties, they will be contained here.",
        ),
    ] = None
    """
    If this tier defines infusion properties, they will be contained here.
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
