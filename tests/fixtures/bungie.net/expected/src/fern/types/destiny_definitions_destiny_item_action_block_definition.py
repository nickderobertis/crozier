

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_item_action_required_item_definition import (
    DestinyDefinitionsDestinyItemActionRequiredItemDefinition,
)
from .destiny_definitions_destiny_progression_reward_definition import (
    DestinyDefinitionsDestinyProgressionRewardDefinition,
)


class DestinyDefinitionsDestinyItemActionBlockDefinition(UniversalBaseModel):
    """
    If an item can have an action performed on it (like "Dismantle"), it will be defined here if you care.
    """

    action_type_label: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="actionTypeLabel"),
        pydantic.Field(alias="actionTypeLabel", description="The internal identifier for the action."),
    ] = None
    """
    The internal identifier for the action.
    """

    consume_entire_stack: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="consumeEntireStack"),
        pydantic.Field(
            alias="consumeEntireStack", description="If true, the entire stack is deleted when the action completes."
        ),
    ] = None
    """
    If true, the entire stack is deleted when the action completes.
    """

    delete_on_action: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="deleteOnAction"),
        pydantic.Field(alias="deleteOnAction", description="If true, the item is deleted when the action completes."),
    ] = None
    """
    If true, the item is deleted when the action completes.
    """

    is_positive: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isPositive"),
        pydantic.Field(
            alias="isPositive",
            description="The content has this property, however it's not entirely clear how it is used.",
        ),
    ] = None
    """
    The content has this property, however it's not entirely clear how it is used.
    """

    overlay_icon: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="overlayIcon"),
        pydantic.Field(
            alias="overlayIcon", description="The icon associated with the overlay screen for the action, if any."
        ),
    ] = None
    """
    The icon associated with the overlay screen for the action, if any.
    """

    overlay_screen_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="overlayScreenName"),
        pydantic.Field(
            alias="overlayScreenName",
            description="If the action has an overlay screen associated with it, this is the name of that screen. Unfortunately, we cannot return the screen's data itself.",
        ),
    ] = None
    """
    If the action has an overlay screen associated with it, this is the name of that screen. Unfortunately, we cannot return the screen's data itself.
    """

    progression_rewards: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyProgressionRewardDefinition]],
        FieldMetadata(alias="progressionRewards"),
        pydantic.Field(
            alias="progressionRewards",
            description="If performing this action earns you Progression, this is the list of progressions and values granted for those progressions by performing this action.",
        ),
    ] = None
    """
    If performing this action earns you Progression, this is the list of progressions and values granted for those progressions by performing this action.
    """

    required_cooldown_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="requiredCooldownHash"),
        pydantic.Field(
            alias="requiredCooldownHash",
            description="The identifier hash for the Cooldown associated with this action. We have not pulled this data yet for you to have more data to use for cooldowns.",
        ),
    ] = None
    """
    The identifier hash for the Cooldown associated with this action. We have not pulled this data yet for you to have more data to use for cooldowns.
    """

    required_cooldown_seconds: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="requiredCooldownSeconds"),
        pydantic.Field(
            alias="requiredCooldownSeconds",
            description="The number of seconds to delay before allowing this action to be performed again.",
        ),
    ] = None
    """
    The number of seconds to delay before allowing this action to be performed again.
    """

    required_items: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyItemActionRequiredItemDefinition]],
        FieldMetadata(alias="requiredItems"),
        pydantic.Field(
            alias="requiredItems",
            description="If the action requires other items to exist or be destroyed, this is the list of those items and requirements.",
        ),
    ] = None
    """
    If the action requires other items to exist or be destroyed, this is the list of those items and requirements.
    """

    required_location: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="requiredLocation"),
        pydantic.Field(
            alias="requiredLocation",
            description="Theoretically, an item could have a localized string for a hint about the location in which the action should be performed. In practice, no items yet have this property.",
        ),
    ] = None
    """
    Theoretically, an item could have a localized string for a hint about the location in which the action should be performed. In practice, no items yet have this property.
    """

    use_on_acquire: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="useOnAcquire"),
        pydantic.Field(
            alias="useOnAcquire",
            description="If true, this action will be performed as soon as you earn this item. Some rewards work this way, providing you a single item to pick up from a reward-granting vendor in-game and then immediately consuming itself to provide you multiple items.",
        ),
    ] = None
    """
    If true, this action will be performed as soon as you earn this item. Some rewards work this way, providing you a single item to pick up from a reward-granting vendor in-game and then immediately consuming itself to provide you multiple items.
    """

    verb_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="verbDescription"),
        pydantic.Field(alias="verbDescription", description="Localized text describing the action being performed."),
    ] = None
    """
    Localized text describing the action being performed.
    """

    verb_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="verbName"),
        pydantic.Field(alias="verbName", description="Localized text for the verb of the action being performed."),
    ] = None
    """
    Localized text for the verb of the action being performed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
