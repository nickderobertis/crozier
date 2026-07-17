

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyProgressionRewardItemQuantity(UniversalBaseModel):
    acquisition_behavior: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="acquisitionBehavior"), pydantic.Field(alias="acquisitionBehavior")
    ] = None
    claim_unlock_display_strings: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="claimUnlockDisplayStrings"),
        pydantic.Field(alias="claimUnlockDisplayStrings"),
    ] = None
    has_conditional_visibility: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasConditionalVisibility"),
        pydantic.Field(
            alias="hasConditionalVisibility",
            description="Indicates that this item quantity may be conditionally shown or hidden, based on various sources of state. For example: server flags, account state, or character progress.",
        ),
    ] = None
    """
    Indicates that this item quantity may be conditionally shown or hidden, based on various sources of state. For example: server flags, account state, or character progress.
    """

    item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemHash"),
        pydantic.Field(
            alias="itemHash",
            description="The hash identifier for the item in question. Use it to look up the item's DestinyInventoryItemDefinition.",
        ),
    ] = None
    """
    The hash identifier for the item in question. Use it to look up the item's DestinyInventoryItemDefinition.
    """

    item_instance_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemInstanceId"),
        pydantic.Field(
            alias="itemInstanceId",
            description="If this quantity is referring to a specific instance of an item, this will have the item's instance ID. Normally, this will be null.",
        ),
    ] = None
    """
    If this quantity is referring to a specific instance of an item, this will have the item's instance ID. Normally, this will be null.
    """

    quantity: typing.Optional[int] = pydantic.Field(default=None)
    """
    The amount of the item needed/available depending on the context of where DestinyItemQuantity is being used.
    """

    rewarded_at_progression_level: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="rewardedAtProgressionLevel"),
        pydantic.Field(alias="rewardedAtProgressionLevel"),
    ] = None
    ui_display_style: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uiDisplayStyle"), pydantic.Field(alias="uiDisplayStyle")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
