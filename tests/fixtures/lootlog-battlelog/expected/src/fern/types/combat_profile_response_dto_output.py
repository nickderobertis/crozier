

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .combat_profile_response_dto_output_damage_mix_item import CombatProfileResponseDtoOutputDamageMixItem
from .combat_profile_response_dto_output_highlights_item import CombatProfileResponseDtoOutputHighlightsItem
from .combat_profile_response_dto_output_matchup_by_profession_item import (
    CombatProfileResponseDtoOutputMatchupByProfessionItem,
)
from .combat_profile_response_dto_output_mitigation_mix_item import CombatProfileResponseDtoOutputMitigationMixItem
from .combat_profile_response_dto_output_ph_trend_item import CombatProfileResponseDtoOutputPhTrendItem
from .combat_profile_response_dto_output_rating_trend_item import CombatProfileResponseDtoOutputRatingTrendItem
from .combat_profile_response_dto_output_spell_usage_item import CombatProfileResponseDtoOutputSpellUsageItem
from .combat_profile_response_dto_output_summary import CombatProfileResponseDtoOutputSummary


class CombatProfileResponseDtoOutput(UniversalBaseModel):
    summary: CombatProfileResponseDtoOutputSummary
    damage_mix: typing_extensions.Annotated[
        typing.List[CombatProfileResponseDtoOutputDamageMixItem],
        FieldMetadata(alias="damageMix"),
        pydantic.Field(alias="damageMix"),
    ]
    mitigation_mix: typing_extensions.Annotated[
        typing.List[CombatProfileResponseDtoOutputMitigationMixItem],
        FieldMetadata(alias="mitigationMix"),
        pydantic.Field(alias="mitigationMix"),
    ]
    spell_usage: typing_extensions.Annotated[
        typing.List[CombatProfileResponseDtoOutputSpellUsageItem],
        FieldMetadata(alias="spellUsage"),
        pydantic.Field(alias="spellUsage"),
    ]
    matchup_by_profession: typing_extensions.Annotated[
        typing.List[CombatProfileResponseDtoOutputMatchupByProfessionItem],
        FieldMetadata(alias="matchupByProfession"),
        pydantic.Field(alias="matchupByProfession"),
    ]
    ph_trend: typing_extensions.Annotated[
        typing.List[CombatProfileResponseDtoOutputPhTrendItem],
        FieldMetadata(alias="phTrend"),
        pydantic.Field(alias="phTrend"),
    ]
    rating_trend: typing_extensions.Annotated[
        typing.List[CombatProfileResponseDtoOutputRatingTrendItem],
        FieldMetadata(alias="ratingTrend"),
        pydantic.Field(alias="ratingTrend"),
    ]
    highlights: typing.List[CombatProfileResponseDtoOutputHighlightsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
