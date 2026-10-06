



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .abyss_season_response_dto_output import AbyssSeasonResponseDtoOutput
    from .bad_request_error_body import BadRequestErrorBody
    from .bad_request_error_body_message import BadRequestErrorBodyMessage
    from .bad_request_error_body_message_one_item import BadRequestErrorBodyMessageOneItem
    from .bad_request_error_body_message_one_item_path_item import BadRequestErrorBodyMessageOneItemPathItem
    from .bad_request_error_body_message_one_item_path_item_one import BadRequestErrorBodyMessageOneItemPathItemOne
    from .bad_request_error_body_message_one_item_path_item_one_one import (
        BadRequestErrorBodyMessageOneItemPathItemOneOne,
    )
    from .battle_accepted_response_dto_output import BattleAcceptedResponseDtoOutput
    from .battle_accepted_response_dto_output_status import BattleAcceptedResponseDtoOutputStatus
    from .battle_analytics_response_dto_output import BattleAnalyticsResponseDtoOutput
    from .battle_characters_response_dto_output import BattleCharactersResponseDtoOutput
    from .battle_characters_response_dto_output_characters_item import BattleCharactersResponseDtoOutputCharactersItem
    from .battle_created_response_dto_output import BattleCreatedResponseDtoOutput
    from .battle_deleted_response_dto_output import BattleDeletedResponseDtoOutput
    from .battle_duration_stats_response_dto_output import BattleDurationStatsResponseDtoOutput
    from .battle_duration_stats_response_dto_output_fastest import BattleDurationStatsResponseDtoOutputFastest
    from .battle_duration_stats_response_dto_output_longest import BattleDurationStatsResponseDtoOutputLongest
    from .battle_raw_response_dto_output import BattleRawResponseDtoOutput
    from .battle_raw_response_dto_output_raw_data import BattleRawResponseDtoOutputRawData
    from .battle_raw_response_dto_output_raw_data_events_item import BattleRawResponseDtoOutputRawDataEventsItem
    from .battle_raw_response_dto_output_raw_data_events_item_actions_item import (
        BattleRawResponseDtoOutputRawDataEventsItemActionsItem,
    )
    from .battle_response_dto_output import BattleResponseDtoOutput
    from .battle_response_dto_output_statistics import BattleResponseDtoOutputStatistics
    from .battle_response_dto_output_statistics_best_efficiency import BattleResponseDtoOutputStatisticsBestEfficiency
    from .battle_response_dto_output_statistics_critical_master import BattleResponseDtoOutputStatisticsCriticalMaster
    from .battle_response_dto_output_statistics_damage_per_turn import BattleResponseDtoOutputStatisticsDamagePerTurn
    from .battle_response_dto_output_statistics_evasion_expert import BattleResponseDtoOutputStatisticsEvasionExpert
    from .battle_response_dto_output_statistics_legendary_warrior import (
        BattleResponseDtoOutputStatisticsLegendaryWarrior,
    )
    from .battle_response_dto_output_statistics_most_active import BattleResponseDtoOutputStatisticsMostActive
    from .battle_response_dto_output_statistics_shield_wall import BattleResponseDtoOutputStatisticsShieldWall
    from .battle_response_dto_output_statistics_top_damage_dealer import (
        BattleResponseDtoOutputStatisticsTopDamageDealer,
    )
    from .battle_response_dto_output_statistics_top_tank import BattleResponseDtoOutputStatisticsTopTank
    from .battle_response_dto_output_statistics_untouchable import BattleResponseDtoOutputStatisticsUntouchable
    from .battle_response_dto_output_warriors_item import BattleResponseDtoOutputWarriorsItem
    from .battle_timeline_response_dto_output import BattleTimelineResponseDtoOutput
    from .battle_timeline_response_dto_output_timeline_item import BattleTimelineResponseDtoOutputTimelineItem
    from .battle_timeline_response_dto_output_timeline_item_actions_item import (
        BattleTimelineResponseDtoOutputTimelineItemActionsItem,
    )
    from .battle_timeline_response_dto_output_timeline_item_cumulative_value import (
        BattleTimelineResponseDtoOutputTimelineItemCumulativeValue,
    )
    from .battle_timeline_response_dto_output_timeline_item_deltas import (
        BattleTimelineResponseDtoOutputTimelineItemDeltas,
    )
    from .battle_timeline_response_dto_output_timeline_item_deltas_by_warrior_value import (
        BattleTimelineResponseDtoOutputTimelineItemDeltasByWarriorValue,
    )
    from .battle_timeline_response_dto_output_warriors_item import BattleTimelineResponseDtoOutputWarriorsItem
    from .battle_user_worlds_response_dto_output import BattleUserWorldsResponseDtoOutput
    from .battle_warriors_search_response_dto_output import BattleWarriorsSearchResponseDtoOutput
    from .battle_warriors_search_response_dto_output_warriors_item import (
        BattleWarriorsSearchResponseDtoOutputWarriorsItem,
    )
    from .battles_list_response_dto_output import BattlesListResponseDtoOutput
    from .battles_list_response_dto_output_battles_item import BattlesListResponseDtoOutputBattlesItem
    from .battles_list_response_dto_output_battles_item_statistics import (
        BattlesListResponseDtoOutputBattlesItemStatistics,
    )
    from .battles_list_response_dto_output_battles_item_statistics_best_efficiency import (
        BattlesListResponseDtoOutputBattlesItemStatisticsBestEfficiency,
    )
    from .battles_list_response_dto_output_battles_item_statistics_critical_master import (
        BattlesListResponseDtoOutputBattlesItemStatisticsCriticalMaster,
    )
    from .battles_list_response_dto_output_battles_item_statistics_damage_per_turn import (
        BattlesListResponseDtoOutputBattlesItemStatisticsDamagePerTurn,
    )
    from .battles_list_response_dto_output_battles_item_statistics_evasion_expert import (
        BattlesListResponseDtoOutputBattlesItemStatisticsEvasionExpert,
    )
    from .battles_list_response_dto_output_battles_item_statistics_legendary_warrior import (
        BattlesListResponseDtoOutputBattlesItemStatisticsLegendaryWarrior,
    )
    from .battles_list_response_dto_output_battles_item_statistics_most_active import (
        BattlesListResponseDtoOutputBattlesItemStatisticsMostActive,
    )
    from .battles_list_response_dto_output_battles_item_statistics_shield_wall import (
        BattlesListResponseDtoOutputBattlesItemStatisticsShieldWall,
    )
    from .battles_list_response_dto_output_battles_item_statistics_top_damage_dealer import (
        BattlesListResponseDtoOutputBattlesItemStatisticsTopDamageDealer,
    )
    from .battles_list_response_dto_output_battles_item_statistics_top_tank import (
        BattlesListResponseDtoOutputBattlesItemStatisticsTopTank,
    )
    from .battles_list_response_dto_output_battles_item_statistics_untouchable import (
        BattlesListResponseDtoOutputBattlesItemStatisticsUntouchable,
    )
    from .battles_list_response_dto_output_battles_item_warriors_item import (
        BattlesListResponseDtoOutputBattlesItemWarriorsItem,
    )
    from .battles_list_response_dto_output_meta import BattlesListResponseDtoOutputMeta
    from .battles_list_response_dto_output_meta_performance import BattlesListResponseDtoOutputMetaPerformance
    from .battles_list_response_dto_output_pagination import BattlesListResponseDtoOutputPagination
    from .combat_profile_response_dto_output import CombatProfileResponseDtoOutput
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
    from .forbidden_error_body import ForbiddenErrorBody
    from .head_to_head_paginated_response_dto_output import HeadToHeadPaginatedResponseDtoOutput
    from .head_to_head_paginated_response_dto_output_meta import HeadToHeadPaginatedResponseDtoOutputMeta
    from .head_to_head_paginated_response_dto_output_meta_performance import (
        HeadToHeadPaginatedResponseDtoOutputMetaPerformance,
    )
    from .head_to_head_paginated_response_dto_output_pagination import HeadToHeadPaginatedResponseDtoOutputPagination
    from .head_to_head_paginated_response_dto_output_records_item import HeadToHeadPaginatedResponseDtoOutputRecordsItem
    from .head_to_head_paginated_response_dto_output_records_item_last_battle_opponent_warrior import (
        HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleOpponentWarrior,
    )
    from .head_to_head_paginated_response_dto_output_records_item_last_battle_result import (
        HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleResult,
    )
    from .head_to_head_paginated_response_dto_output_records_item_last_battle_user_warrior import (
        HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleUserWarrior,
    )
    from .ph_growth_data_point_response_dto_output import PhGrowthDataPointResponseDtoOutput
    from .player_vs_player_paginated_response_dto_output import PlayerVsPlayerPaginatedResponseDtoOutput
    from .player_vs_player_paginated_response_dto_output_battles_item import (
        PlayerVsPlayerPaginatedResponseDtoOutputBattlesItem,
    )
    from .player_vs_player_paginated_response_dto_output_battles_item_opponent_warrior import (
        PlayerVsPlayerPaginatedResponseDtoOutputBattlesItemOpponentWarrior,
    )
    from .player_vs_player_paginated_response_dto_output_battles_item_user_warrior import (
        PlayerVsPlayerPaginatedResponseDtoOutputBattlesItemUserWarrior,
    )
    from .player_vs_player_paginated_response_dto_output_meta import PlayerVsPlayerPaginatedResponseDtoOutputMeta
    from .player_vs_player_paginated_response_dto_output_meta_performance import (
        PlayerVsPlayerPaginatedResponseDtoOutputMetaPerformance,
    )
    from .player_vs_player_paginated_response_dto_output_pagination import (
        PlayerVsPlayerPaginatedResponseDtoOutputPagination,
    )
    from .profession_win_rate_response_dto_output import ProfessionWinRateResponseDtoOutput
    from .rating_delta_by_opponent_response_dto_output import RatingDeltaByOpponentResponseDtoOutput
    from .rating_growth_data_point_response_dto_output import RatingGrowthDataPointResponseDtoOutput
    from .streak_response_dto_output import StreakResponseDtoOutput
    from .streak_response_dto_output_current import StreakResponseDtoOutputCurrent
    from .streak_response_dto_output_current_type import StreakResponseDtoOutputCurrentType
    from .streak_response_dto_output_longest import StreakResponseDtoOutputLongest
    from .too_many_requests_error_body import TooManyRequestsErrorBody
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .unauthorized_error_body_error import UnauthorizedErrorBodyError
    from .unauthorized_error_body_one import UnauthorizedErrorBodyOne
_dynamic_imports: typing.Dict[str, str] = {
    "AbyssSeasonResponseDtoOutput": ".abyss_season_response_dto_output",
    "BadRequestErrorBody": ".bad_request_error_body",
    "BadRequestErrorBodyMessage": ".bad_request_error_body_message",
    "BadRequestErrorBodyMessageOneItem": ".bad_request_error_body_message_one_item",
    "BadRequestErrorBodyMessageOneItemPathItem": ".bad_request_error_body_message_one_item_path_item",
    "BadRequestErrorBodyMessageOneItemPathItemOne": ".bad_request_error_body_message_one_item_path_item_one",
    "BadRequestErrorBodyMessageOneItemPathItemOneOne": ".bad_request_error_body_message_one_item_path_item_one_one",
    "BattleAcceptedResponseDtoOutput": ".battle_accepted_response_dto_output",
    "BattleAcceptedResponseDtoOutputStatus": ".battle_accepted_response_dto_output_status",
    "BattleAnalyticsResponseDtoOutput": ".battle_analytics_response_dto_output",
    "BattleCharactersResponseDtoOutput": ".battle_characters_response_dto_output",
    "BattleCharactersResponseDtoOutputCharactersItem": ".battle_characters_response_dto_output_characters_item",
    "BattleCreatedResponseDtoOutput": ".battle_created_response_dto_output",
    "BattleDeletedResponseDtoOutput": ".battle_deleted_response_dto_output",
    "BattleDurationStatsResponseDtoOutput": ".battle_duration_stats_response_dto_output",
    "BattleDurationStatsResponseDtoOutputFastest": ".battle_duration_stats_response_dto_output_fastest",
    "BattleDurationStatsResponseDtoOutputLongest": ".battle_duration_stats_response_dto_output_longest",
    "BattleRawResponseDtoOutput": ".battle_raw_response_dto_output",
    "BattleRawResponseDtoOutputRawData": ".battle_raw_response_dto_output_raw_data",
    "BattleRawResponseDtoOutputRawDataEventsItem": ".battle_raw_response_dto_output_raw_data_events_item",
    "BattleRawResponseDtoOutputRawDataEventsItemActionsItem": ".battle_raw_response_dto_output_raw_data_events_item_actions_item",
    "BattleResponseDtoOutput": ".battle_response_dto_output",
    "BattleResponseDtoOutputStatistics": ".battle_response_dto_output_statistics",
    "BattleResponseDtoOutputStatisticsBestEfficiency": ".battle_response_dto_output_statistics_best_efficiency",
    "BattleResponseDtoOutputStatisticsCriticalMaster": ".battle_response_dto_output_statistics_critical_master",
    "BattleResponseDtoOutputStatisticsDamagePerTurn": ".battle_response_dto_output_statistics_damage_per_turn",
    "BattleResponseDtoOutputStatisticsEvasionExpert": ".battle_response_dto_output_statistics_evasion_expert",
    "BattleResponseDtoOutputStatisticsLegendaryWarrior": ".battle_response_dto_output_statistics_legendary_warrior",
    "BattleResponseDtoOutputStatisticsMostActive": ".battle_response_dto_output_statistics_most_active",
    "BattleResponseDtoOutputStatisticsShieldWall": ".battle_response_dto_output_statistics_shield_wall",
    "BattleResponseDtoOutputStatisticsTopDamageDealer": ".battle_response_dto_output_statistics_top_damage_dealer",
    "BattleResponseDtoOutputStatisticsTopTank": ".battle_response_dto_output_statistics_top_tank",
    "BattleResponseDtoOutputStatisticsUntouchable": ".battle_response_dto_output_statistics_untouchable",
    "BattleResponseDtoOutputWarriorsItem": ".battle_response_dto_output_warriors_item",
    "BattleTimelineResponseDtoOutput": ".battle_timeline_response_dto_output",
    "BattleTimelineResponseDtoOutputTimelineItem": ".battle_timeline_response_dto_output_timeline_item",
    "BattleTimelineResponseDtoOutputTimelineItemActionsItem": ".battle_timeline_response_dto_output_timeline_item_actions_item",
    "BattleTimelineResponseDtoOutputTimelineItemCumulativeValue": ".battle_timeline_response_dto_output_timeline_item_cumulative_value",
    "BattleTimelineResponseDtoOutputTimelineItemDeltas": ".battle_timeline_response_dto_output_timeline_item_deltas",
    "BattleTimelineResponseDtoOutputTimelineItemDeltasByWarriorValue": ".battle_timeline_response_dto_output_timeline_item_deltas_by_warrior_value",
    "BattleTimelineResponseDtoOutputWarriorsItem": ".battle_timeline_response_dto_output_warriors_item",
    "BattleUserWorldsResponseDtoOutput": ".battle_user_worlds_response_dto_output",
    "BattleWarriorsSearchResponseDtoOutput": ".battle_warriors_search_response_dto_output",
    "BattleWarriorsSearchResponseDtoOutputWarriorsItem": ".battle_warriors_search_response_dto_output_warriors_item",
    "BattlesListResponseDtoOutput": ".battles_list_response_dto_output",
    "BattlesListResponseDtoOutputBattlesItem": ".battles_list_response_dto_output_battles_item",
    "BattlesListResponseDtoOutputBattlesItemStatistics": ".battles_list_response_dto_output_battles_item_statistics",
    "BattlesListResponseDtoOutputBattlesItemStatisticsBestEfficiency": ".battles_list_response_dto_output_battles_item_statistics_best_efficiency",
    "BattlesListResponseDtoOutputBattlesItemStatisticsCriticalMaster": ".battles_list_response_dto_output_battles_item_statistics_critical_master",
    "BattlesListResponseDtoOutputBattlesItemStatisticsDamagePerTurn": ".battles_list_response_dto_output_battles_item_statistics_damage_per_turn",
    "BattlesListResponseDtoOutputBattlesItemStatisticsEvasionExpert": ".battles_list_response_dto_output_battles_item_statistics_evasion_expert",
    "BattlesListResponseDtoOutputBattlesItemStatisticsLegendaryWarrior": ".battles_list_response_dto_output_battles_item_statistics_legendary_warrior",
    "BattlesListResponseDtoOutputBattlesItemStatisticsMostActive": ".battles_list_response_dto_output_battles_item_statistics_most_active",
    "BattlesListResponseDtoOutputBattlesItemStatisticsShieldWall": ".battles_list_response_dto_output_battles_item_statistics_shield_wall",
    "BattlesListResponseDtoOutputBattlesItemStatisticsTopDamageDealer": ".battles_list_response_dto_output_battles_item_statistics_top_damage_dealer",
    "BattlesListResponseDtoOutputBattlesItemStatisticsTopTank": ".battles_list_response_dto_output_battles_item_statistics_top_tank",
    "BattlesListResponseDtoOutputBattlesItemStatisticsUntouchable": ".battles_list_response_dto_output_battles_item_statistics_untouchable",
    "BattlesListResponseDtoOutputBattlesItemWarriorsItem": ".battles_list_response_dto_output_battles_item_warriors_item",
    "BattlesListResponseDtoOutputMeta": ".battles_list_response_dto_output_meta",
    "BattlesListResponseDtoOutputMetaPerformance": ".battles_list_response_dto_output_meta_performance",
    "BattlesListResponseDtoOutputPagination": ".battles_list_response_dto_output_pagination",
    "CombatProfileResponseDtoOutput": ".combat_profile_response_dto_output",
    "CombatProfileResponseDtoOutputDamageMixItem": ".combat_profile_response_dto_output_damage_mix_item",
    "CombatProfileResponseDtoOutputHighlightsItem": ".combat_profile_response_dto_output_highlights_item",
    "CombatProfileResponseDtoOutputMatchupByProfessionItem": ".combat_profile_response_dto_output_matchup_by_profession_item",
    "CombatProfileResponseDtoOutputMitigationMixItem": ".combat_profile_response_dto_output_mitigation_mix_item",
    "CombatProfileResponseDtoOutputPhTrendItem": ".combat_profile_response_dto_output_ph_trend_item",
    "CombatProfileResponseDtoOutputRatingTrendItem": ".combat_profile_response_dto_output_rating_trend_item",
    "CombatProfileResponseDtoOutputSpellUsageItem": ".combat_profile_response_dto_output_spell_usage_item",
    "CombatProfileResponseDtoOutputSummary": ".combat_profile_response_dto_output_summary",
    "ForbiddenErrorBody": ".forbidden_error_body",
    "HeadToHeadPaginatedResponseDtoOutput": ".head_to_head_paginated_response_dto_output",
    "HeadToHeadPaginatedResponseDtoOutputMeta": ".head_to_head_paginated_response_dto_output_meta",
    "HeadToHeadPaginatedResponseDtoOutputMetaPerformance": ".head_to_head_paginated_response_dto_output_meta_performance",
    "HeadToHeadPaginatedResponseDtoOutputPagination": ".head_to_head_paginated_response_dto_output_pagination",
    "HeadToHeadPaginatedResponseDtoOutputRecordsItem": ".head_to_head_paginated_response_dto_output_records_item",
    "HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleOpponentWarrior": ".head_to_head_paginated_response_dto_output_records_item_last_battle_opponent_warrior",
    "HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleResult": ".head_to_head_paginated_response_dto_output_records_item_last_battle_result",
    "HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleUserWarrior": ".head_to_head_paginated_response_dto_output_records_item_last_battle_user_warrior",
    "PhGrowthDataPointResponseDtoOutput": ".ph_growth_data_point_response_dto_output",
    "PlayerVsPlayerPaginatedResponseDtoOutput": ".player_vs_player_paginated_response_dto_output",
    "PlayerVsPlayerPaginatedResponseDtoOutputBattlesItem": ".player_vs_player_paginated_response_dto_output_battles_item",
    "PlayerVsPlayerPaginatedResponseDtoOutputBattlesItemOpponentWarrior": ".player_vs_player_paginated_response_dto_output_battles_item_opponent_warrior",
    "PlayerVsPlayerPaginatedResponseDtoOutputBattlesItemUserWarrior": ".player_vs_player_paginated_response_dto_output_battles_item_user_warrior",
    "PlayerVsPlayerPaginatedResponseDtoOutputMeta": ".player_vs_player_paginated_response_dto_output_meta",
    "PlayerVsPlayerPaginatedResponseDtoOutputMetaPerformance": ".player_vs_player_paginated_response_dto_output_meta_performance",
    "PlayerVsPlayerPaginatedResponseDtoOutputPagination": ".player_vs_player_paginated_response_dto_output_pagination",
    "ProfessionWinRateResponseDtoOutput": ".profession_win_rate_response_dto_output",
    "RatingDeltaByOpponentResponseDtoOutput": ".rating_delta_by_opponent_response_dto_output",
    "RatingGrowthDataPointResponseDtoOutput": ".rating_growth_data_point_response_dto_output",
    "StreakResponseDtoOutput": ".streak_response_dto_output",
    "StreakResponseDtoOutputCurrent": ".streak_response_dto_output_current",
    "StreakResponseDtoOutputCurrentType": ".streak_response_dto_output_current_type",
    "StreakResponseDtoOutputLongest": ".streak_response_dto_output_longest",
    "TooManyRequestsErrorBody": ".too_many_requests_error_body",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "UnauthorizedErrorBodyError": ".unauthorized_error_body_error",
    "UnauthorizedErrorBodyOne": ".unauthorized_error_body_one",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AbyssSeasonResponseDtoOutput",
    "BadRequestErrorBody",
    "BadRequestErrorBodyMessage",
    "BadRequestErrorBodyMessageOneItem",
    "BadRequestErrorBodyMessageOneItemPathItem",
    "BadRequestErrorBodyMessageOneItemPathItemOne",
    "BadRequestErrorBodyMessageOneItemPathItemOneOne",
    "BattleAcceptedResponseDtoOutput",
    "BattleAcceptedResponseDtoOutputStatus",
    "BattleAnalyticsResponseDtoOutput",
    "BattleCharactersResponseDtoOutput",
    "BattleCharactersResponseDtoOutputCharactersItem",
    "BattleCreatedResponseDtoOutput",
    "BattleDeletedResponseDtoOutput",
    "BattleDurationStatsResponseDtoOutput",
    "BattleDurationStatsResponseDtoOutputFastest",
    "BattleDurationStatsResponseDtoOutputLongest",
    "BattleRawResponseDtoOutput",
    "BattleRawResponseDtoOutputRawData",
    "BattleRawResponseDtoOutputRawDataEventsItem",
    "BattleRawResponseDtoOutputRawDataEventsItemActionsItem",
    "BattleResponseDtoOutput",
    "BattleResponseDtoOutputStatistics",
    "BattleResponseDtoOutputStatisticsBestEfficiency",
    "BattleResponseDtoOutputStatisticsCriticalMaster",
    "BattleResponseDtoOutputStatisticsDamagePerTurn",
    "BattleResponseDtoOutputStatisticsEvasionExpert",
    "BattleResponseDtoOutputStatisticsLegendaryWarrior",
    "BattleResponseDtoOutputStatisticsMostActive",
    "BattleResponseDtoOutputStatisticsShieldWall",
    "BattleResponseDtoOutputStatisticsTopDamageDealer",
    "BattleResponseDtoOutputStatisticsTopTank",
    "BattleResponseDtoOutputStatisticsUntouchable",
    "BattleResponseDtoOutputWarriorsItem",
    "BattleTimelineResponseDtoOutput",
    "BattleTimelineResponseDtoOutputTimelineItem",
    "BattleTimelineResponseDtoOutputTimelineItemActionsItem",
    "BattleTimelineResponseDtoOutputTimelineItemCumulativeValue",
    "BattleTimelineResponseDtoOutputTimelineItemDeltas",
    "BattleTimelineResponseDtoOutputTimelineItemDeltasByWarriorValue",
    "BattleTimelineResponseDtoOutputWarriorsItem",
    "BattleUserWorldsResponseDtoOutput",
    "BattleWarriorsSearchResponseDtoOutput",
    "BattleWarriorsSearchResponseDtoOutputWarriorsItem",
    "BattlesListResponseDtoOutput",
    "BattlesListResponseDtoOutputBattlesItem",
    "BattlesListResponseDtoOutputBattlesItemStatistics",
    "BattlesListResponseDtoOutputBattlesItemStatisticsBestEfficiency",
    "BattlesListResponseDtoOutputBattlesItemStatisticsCriticalMaster",
    "BattlesListResponseDtoOutputBattlesItemStatisticsDamagePerTurn",
    "BattlesListResponseDtoOutputBattlesItemStatisticsEvasionExpert",
    "BattlesListResponseDtoOutputBattlesItemStatisticsLegendaryWarrior",
    "BattlesListResponseDtoOutputBattlesItemStatisticsMostActive",
    "BattlesListResponseDtoOutputBattlesItemStatisticsShieldWall",
    "BattlesListResponseDtoOutputBattlesItemStatisticsTopDamageDealer",
    "BattlesListResponseDtoOutputBattlesItemStatisticsTopTank",
    "BattlesListResponseDtoOutputBattlesItemStatisticsUntouchable",
    "BattlesListResponseDtoOutputBattlesItemWarriorsItem",
    "BattlesListResponseDtoOutputMeta",
    "BattlesListResponseDtoOutputMetaPerformance",
    "BattlesListResponseDtoOutputPagination",
    "CombatProfileResponseDtoOutput",
    "CombatProfileResponseDtoOutputDamageMixItem",
    "CombatProfileResponseDtoOutputHighlightsItem",
    "CombatProfileResponseDtoOutputMatchupByProfessionItem",
    "CombatProfileResponseDtoOutputMitigationMixItem",
    "CombatProfileResponseDtoOutputPhTrendItem",
    "CombatProfileResponseDtoOutputRatingTrendItem",
    "CombatProfileResponseDtoOutputSpellUsageItem",
    "CombatProfileResponseDtoOutputSummary",
    "ForbiddenErrorBody",
    "HeadToHeadPaginatedResponseDtoOutput",
    "HeadToHeadPaginatedResponseDtoOutputMeta",
    "HeadToHeadPaginatedResponseDtoOutputMetaPerformance",
    "HeadToHeadPaginatedResponseDtoOutputPagination",
    "HeadToHeadPaginatedResponseDtoOutputRecordsItem",
    "HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleOpponentWarrior",
    "HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleResult",
    "HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleUserWarrior",
    "PhGrowthDataPointResponseDtoOutput",
    "PlayerVsPlayerPaginatedResponseDtoOutput",
    "PlayerVsPlayerPaginatedResponseDtoOutputBattlesItem",
    "PlayerVsPlayerPaginatedResponseDtoOutputBattlesItemOpponentWarrior",
    "PlayerVsPlayerPaginatedResponseDtoOutputBattlesItemUserWarrior",
    "PlayerVsPlayerPaginatedResponseDtoOutputMeta",
    "PlayerVsPlayerPaginatedResponseDtoOutputMetaPerformance",
    "PlayerVsPlayerPaginatedResponseDtoOutputPagination",
    "ProfessionWinRateResponseDtoOutput",
    "RatingDeltaByOpponentResponseDtoOutput",
    "RatingGrowthDataPointResponseDtoOutput",
    "StreakResponseDtoOutput",
    "StreakResponseDtoOutputCurrent",
    "StreakResponseDtoOutputCurrentType",
    "StreakResponseDtoOutputLongest",
    "TooManyRequestsErrorBody",
    "UnauthorizedErrorBody",
    "UnauthorizedErrorBodyError",
    "UnauthorizedErrorBodyOne",
]
