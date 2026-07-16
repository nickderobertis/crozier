

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyItemInvestmentStatDefinition(UniversalBaseModel):
    """
    Represents a "raw" investment stat, before calculated stats are calculated and before any DestinyStatGroupDefinition is applied to transform the stat into something closer to what you see in-game.
    Because these won't match what you see in-game, consider carefully whether you really want to use these stats. I have left them in case someone can do something useful or interesting with the pre-processed statistics.
    """

    is_conditionally_active: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isConditionallyActive"),
        pydantic.Field(
            alias="isConditionallyActive",
            description='If this is true, the stat will only be applied on the item in certain game state conditions, and we can\'t know statically whether or not this stat will be applied. Check the "live" API data instead for whether this value is being applied on a specific instance of the item in question, and you can use this to decide whether you want to show the stat on the generic view of the item, or whether you want to show some kind of caveat or warning about the stat value being conditional on game state.',
        ),
    ] = None
    """
    If this is true, the stat will only be applied on the item in certain game state conditions, and we can't know statically whether or not this stat will be applied. Check the "live" API data instead for whether this value is being applied on a specific instance of the item in question, and you can use this to decide whether you want to show the stat on the generic view of the item, or whether you want to show some kind of caveat or warning about the stat value being conditional on game state.
    """

    stat_type_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="statTypeHash"),
        pydantic.Field(
            alias="statTypeHash", description="The hash identifier for the DestinyStatDefinition defining this stat."
        ),
    ] = None
    """
    The hash identifier for the DestinyStatDefinition defining this stat.
    """

    value: typing.Optional[int] = pydantic.Field(default=None)
    """
    The raw "Investment" value for the stat, before transformations are performed to turn this raw stat into stats that are displayed in the game UI.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
