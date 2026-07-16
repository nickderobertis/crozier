

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_progression_display_properties_definition import (
    DestinyDefinitionsDestinyProgressionDisplayPropertiesDefinition,
)
from .destiny_definitions_destiny_progression_reward_item_quantity import (
    DestinyDefinitionsDestinyProgressionRewardItemQuantity,
)
from .destiny_definitions_destiny_progression_step_definition import DestinyDefinitionsDestinyProgressionStepDefinition
from .destiny_misc_destiny_color import DestinyMiscDestinyColor


class DestinyDefinitionsDestinyProgressionDefinition(UniversalBaseModel):
    """
    A "Progression" in Destiny is best explained by an example.
    A Character's "Level" is a progression: it has Experience that can be earned, levels that can be gained, and is evaluated and displayed at various points in the game. A Character's "Faction Reputation" is also a progression for much the same reason.
    Progression is used by a variety of systems, and the definition of a Progression will generally only be useful if combining with live data (such as a character's DestinyCharacterProgressionComponent.progressions property, which holds that character's live Progression states).
    Fundamentally, a Progression measures your "Level" by evaluating the thresholds in its Steps (one step per level, except for the last step which can be repeated indefinitely for "Levels" that have no ceiling) against the total earned "progression points"/experience. (for simplicity purposes, we will henceforth refer to earned progression points as experience, though it need not be a mechanic that in any way resembles Experience in a traditional sense).
    Earned experience is calculated in a variety of ways, determined by the Progression's scope. These go from looking up a stored value to performing exceedingly obtuse calculations. This is why we provide live data in DestinyCharacterProgressionComponent.progressions, so you don't have to worry about those.
    """

    color: typing.Optional[DestinyMiscDestinyColor] = pydantic.Field(default=None)
    """
    The #RGB string value for the color related to this progression, if there is one.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyProgressionDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(alias="displayProperties"),
    ] = None
    faction_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="factionHash"),
        pydantic.Field(
            alias="factionHash",
            description="If the value exists, this is the hash identifier for the Faction that owns this Progression.\r\nThis is purely for convenience, if you're looking at a progression and want to know if and who it's related to in terms of Faction Reputation.",
        ),
    ] = None
    """
    If the value exists, this is the hash identifier for the Faction that owns this Progression.
    This is purely for convenience, if you're looking at a progression and want to know if and who it's related to in terms of Faction Reputation.
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

    rank_icon: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="rankIcon"),
        pydantic.Field(
            alias="rankIcon",
            description="For progressions that have it, this is the rank icon we use in the Companion, displayed above the progressions' rank value.",
        ),
    ] = None
    """
    For progressions that have it, this is the rank icon we use in the Companion, displayed above the progressions' rank value.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    repeat_last_step: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="repeatLastStep"),
        pydantic.Field(
            alias="repeatLastStep", description="If this is True, then the progression doesn't have a maximum level."
        ),
    ] = None
    """
    If this is True, then the progression doesn't have a maximum level.
    """

    reward_items: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyProgressionRewardItemQuantity]],
        FieldMetadata(alias="rewardItems"),
        pydantic.Field(alias="rewardItems"),
    ] = None
    scope: typing.Optional[int] = pydantic.Field(default=None)
    """
    The "Scope" of the progression indicates the source of the progression's live data.
    See the DestinyProgressionScope enum for more info: but essentially, a Progression can either be backed by a stored value, or it can be a calculated derivative of other values.
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    If there's a description of how to earn this progression in the local config, this will be that localized description.
    """

    steps: typing.Optional[typing.List[DestinyDefinitionsDestinyProgressionStepDefinition]] = pydantic.Field(
        default=None
    )
    """
    Progressions are divided into Steps, which roughly equate to "Levels" in the traditional sense of a Progression. Notably, the last step can be repeated indefinitely if repeatLastStep is true, meaning that the calculation for your level is not as simple as comparing your current progress to the max progress of the steps. 
    These and more calculations are done for you if you grab live character progression data, such as in the DestinyCharacterProgressionComponent.
    """

    visible: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, the Progression is something worth showing to users.
    If false, BNet isn't going to show it. But that doesn't mean you can't. We're all friends here.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
