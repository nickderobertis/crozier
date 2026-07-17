

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyItemTalentGridBlockDefinition(UniversalBaseModel):
    """
    This defines information that can only come from a talent grid on an item. Items mostly have negligible talent grid data these days, but instanced items still retain grids as a source for some of this common information.
    Builds/Subclasses are the only items left that still have talent grids with meaningful Nodes.
    """

    build_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="buildName"),
        pydantic.Field(
            alias="buildName",
            description='A shortcut string identifier for the "build" in question, if this talent grid has an associated build. Doesn\'t map to anything we can expose at the moment.',
        ),
    ] = None
    """
    A shortcut string identifier for the "build" in question, if this talent grid has an associated build. Doesn't map to anything we can expose at the moment.
    """

    hud_damage_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="hudDamageType"),
        pydantic.Field(
            alias="hudDamageType",
            description="If the talent grid implies a damage type, this is the enum value for that damage type.",
        ),
    ] = None
    """
    If the talent grid implies a damage type, this is the enum value for that damage type.
    """

    hud_icon: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="hudIcon"),
        pydantic.Field(
            alias="hudIcon",
            description="If the talent grid has a special icon that's shown in the game UI (like builds, funny that), this is the identifier for that icon. Sadly, we don't actually get that icon right now. I'll be looking to replace this with a path to the actual icon itself.",
        ),
    ] = None
    """
    If the talent grid has a special icon that's shown in the game UI (like builds, funny that), this is the identifier for that icon. Sadly, we don't actually get that icon right now. I'll be looking to replace this with a path to the actual icon itself.
    """

    item_detail_string: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itemDetailString"),
        pydantic.Field(
            alias="itemDetailString",
            description='This is meant to be a subtitle for looking at the talent grid. In practice, somewhat frustratingly, this always merely says the localized word for "Details". Great. Maybe it\'ll have more if talent grids ever get used for more than builds and subclasses again.',
        ),
    ] = None
    """
    This is meant to be a subtitle for looking at the talent grid. In practice, somewhat frustratingly, this always merely says the localized word for "Details". Great. Maybe it'll have more if talent grids ever get used for more than builds and subclasses again.
    """

    talent_grid_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="talentGridHash"),
        pydantic.Field(
            alias="talentGridHash",
            description="The hash identifier of the DestinyTalentGridDefinition attached to this item.",
        ),
    ] = None
    """
    The hash identifier of the DestinyTalentGridDefinition attached to this item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
