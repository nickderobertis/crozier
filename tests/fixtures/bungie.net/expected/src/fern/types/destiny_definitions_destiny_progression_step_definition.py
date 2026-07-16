

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_item_quantity import DestinyDestinyItemQuantity


class DestinyDefinitionsDestinyProgressionStepDefinition(UniversalBaseModel):
    """
    This defines a single Step in a progression (which roughly equates to a level. See DestinyProgressionDefinition for caveats).
    """

    display_effect_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="displayEffectType"),
        pydantic.Field(
            alias="displayEffectType",
            description='This appears to be, when you "level up", whether a visual effect will display and on what entity. See DestinyProgressionStepDisplayEffect for slightly more info.',
        ),
    ] = None
    """
    This appears to be, when you "level up", whether a visual effect will display and on what entity. See DestinyProgressionStepDisplayEffect for slightly more info.
    """

    icon: typing.Optional[str] = pydantic.Field(default=None)
    """
    If this progression step has a specific icon related to it, this is the icon to show.
    """

    progress_total: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="progressTotal"),
        pydantic.Field(
            alias="progressTotal",
            description='The total amount of progression points/"experience" you will need to initially reach this step. If this is the last step and the progression is repeating indefinitely (DestinyProgressionDefinition.repeatLastStep), this will also be the progress needed to level it up further by repeating this step again.',
        ),
    ] = None
    """
    The total amount of progression points/"experience" you will need to initially reach this step. If this is the last step and the progression is repeating indefinitely (DestinyProgressionDefinition.repeatLastStep), this will also be the progress needed to level it up further by repeating this step again.
    """

    reward_items: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDestinyItemQuantity]],
        FieldMetadata(alias="rewardItems"),
        pydantic.Field(
            alias="rewardItems", description="A listing of items rewarded as a result of reaching this level."
        ),
    ] = None
    """
    A listing of items rewarded as a result of reaching this level.
    """

    step_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="stepName"),
        pydantic.Field(
            alias="stepName",
            description="Very rarely, Progressions will have localized text describing the Level of the progression. This will be that localized text, if it exists. Otherwise, the standard appears to be to simply show the level numerically.",
        ),
    ] = None
    """
    Very rarely, Progressions will have localized text describing the Level of the progression. This will be that localized text, if it exists. Otherwise, the standard appears to be to simply show the level numerically.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
