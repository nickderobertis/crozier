

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyPerksDestinyPerkReference(UniversalBaseModel):
    """
    The list of perks to display in an item tooltip - and whether or not they have been activated.
    Perks apply a variety of effects to a character, and are generally either intrinsic to the item or provided in activated talent nodes or sockets.
    """

    icon_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="iconPath"),
        pydantic.Field(alias="iconPath", description="The icon for the perk."),
    ] = None
    """
    The icon for the perk.
    """

    is_active: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isActive"),
        pydantic.Field(
            alias="isActive",
            description="Whether this perk is currently active. (We may return perks that you have not actually activated yet: these represent perks that you should show in the item's tooltip, but that the user has not yet activated.)",
        ),
    ] = None
    """
    Whether this perk is currently active. (We may return perks that you have not actually activated yet: these represent perks that you should show in the item's tooltip, but that the user has not yet activated.)
    """

    perk_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="perkHash"),
        pydantic.Field(
            alias="perkHash",
            description="The hash identifier for the perk, which can be used to look up DestinySandboxPerkDefinition if it exists. Be warned, perks frequently do not have user-viewable information. You should examine whether you actually found a name/description in the perk's definition before you show it to the user.",
        ),
    ] = None
    """
    The hash identifier for the perk, which can be used to look up DestinySandboxPerkDefinition if it exists. Be warned, perks frequently do not have user-viewable information. You should examine whether you actually found a name/description in the perk's definition before you show it to the user.
    """

    visible: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Some perks provide benefits, but aren't visible in the UI. This value will let you know if this is perk should be shown in your UI.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
