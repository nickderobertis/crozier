

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_stat_display_definition import DestinyDefinitionsDestinyStatDisplayDefinition
from .destiny_definitions_destiny_stat_override_definition import DestinyDefinitionsDestinyStatOverrideDefinition


class DestinyDefinitionsDestinyStatGroupDefinition(UniversalBaseModel):
    """
    When an inventory item (DestinyInventoryItemDefinition) has Stats (such as Attack Power), the item will refer to a Stat Group. This definition enumerates the properties used to transform the item's "Investment" stats into "Display" stats.
    See DestinyStatDefinition's documentation for information about the transformation of Stats, and the meaning of an Investment vs. a Display stat.
    If you don't want to do these calculations on your own, fear not: pulling live data from the BNet endpoints will return display stat values pre-computed and ready for you to use. I highly recommend this approach, saves a lot of time and also accounts for certain stat modifiers that can't easily be accounted for without live data (such as stat modifiers on Talent Grids and Socket Plugs)
    """

    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    maximum_value: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maximumValue"),
        pydantic.Field(
            alias="maximumValue",
            description="The maximum possible value that any stat in this group can be transformed into.\r\nThis is used by stats that *don't* have scaledStats entries below, but that still need to be displayed as a progress bar, in which case this is used as the upper bound for said progress bar. (the lower bound is always 0)",
        ),
    ] = None
    """
    The maximum possible value that any stat in this group can be transformed into.
    This is used by stats that *don't* have scaledStats entries below, but that still need to be displayed as a progress bar, in which case this is used as the upper bound for said progress bar. (the lower bound is always 0)
    """

    overrides: typing.Optional[typing.Dict[str, DestinyDefinitionsDestinyStatOverrideDefinition]] = pydantic.Field(
        default=None
    )
    """
    The game has the ability to override, based on the stat group, what the localized text is that is displayed for Stats being shown on the item.
    Mercifully, no Stat Groups use this feature currently. If they start using them, we'll all need to start using them (and those of you who are more prudent than I am can go ahead and start pre-checking for this.)
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    scaled_stats: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyStatDisplayDefinition]],
        FieldMetadata(alias="scaledStats"),
        pydantic.Field(
            alias="scaledStats",
            description='Any stat that requires scaling to be transformed from an "Investment" stat to a "Display" stat will have an entry in this list. For more information on what those types of stats mean and the transformation process, see DestinyStatDefinition.\r\nIn retrospect, I wouldn\'t mind if this was a dictionary keyed by the stat hash instead. But I\'m going to leave it be because [[After Apple Picking]].',
        ),
    ] = None
    """
    Any stat that requires scaling to be transformed from an "Investment" stat to a "Display" stat will have an entry in this list. For more information on what those types of stats mean and the transformation process, see DestinyStatDefinition.
    In retrospect, I wouldn't mind if this was a dictionary keyed by the stat hash instead. But I'm going to leave it be because [[After Apple Picking]].
    """

    ui_position: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="uiPosition"),
        pydantic.Field(
            alias="uiPosition",
            description="This apparently indicates the position of the stats in the UI? I've returned it in case anyone can use it, but it's not of any use to us on BNet. Something's being lost in translation with this value.",
        ),
    ] = None
    """
    This apparently indicates the position of the stats in the UI? I've returned it in case anyone can use it, but it's not of any use to us on BNet. Something's being lost in translation with this value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
