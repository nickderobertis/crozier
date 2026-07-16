

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)


class DestinyDefinitionsSocketsDestinySocketCategoryDefinition(UniversalBaseModel):
    """
    Sockets on an item are organized into Categories visually.
    You can find references to the socket category defined on an item's DestinyInventoryItemDefinition.sockets.socketCategories property.
    This has the display information for rendering the categories' header, and a hint for how the UI should handle showing this category.
    The shitty thing about this, however, is that the socket categories' UI style can be overridden by the item's UI style. For instance, the Socket Category used by Emote Sockets says it's "consumable," but that's a lie: they're all reusable, and overridden by the detail UI pages in ways that we can't easily account for in the API.
    As a result, I will try to compile these rules into the individual sockets on items, and provide the best hint possible there through the plugSources property. In the future, I may attempt to use this information in conjunction with the item to provide a more usable UI hint on the socket layer, but for now improving the consistency of plugSources is the best I have time to provide. (See https://github.com/Bungie-net/api/issues/522 for more info)
    """

    category_style: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="categoryStyle"),
        pydantic.Field(
            alias="categoryStyle", description="Same as uiCategoryStyle, but in a more usable enumeration form."
        ),
    ] = None
    """
    Same as uiCategoryStyle, but in a more usable enumeration form.
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

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    ui_category_style: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="uiCategoryStyle"),
        pydantic.Field(
            alias="uiCategoryStyle",
            description="A string hinting to the game's UI system about how the sockets in this category should be displayed.\r\nBNet doesn't use it: it's up to you to find valid values and make your own special UI if you want to honor this category style.",
        ),
    ] = None
    """
    A string hinting to the game's UI system about how the sockets in this category should be displayed.
    BNet doesn't use it: it's up to you to find valid values and make your own special UI if you want to honor this category style.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
