



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .battles_controller_get_battle_analytics_request_period import BattlesControllerGetBattleAnalyticsRequestPeriod
    from .battles_controller_get_battle_duration_request_period import BattlesControllerGetBattleDurationRequestPeriod
    from .battles_controller_get_battle_duration_request_sort_by import BattlesControllerGetBattleDurationRequestSortBy
    from .battles_controller_get_battle_duration_request_sort_order import (
        BattlesControllerGetBattleDurationRequestSortOrder,
    )
    from .battles_controller_get_combat_profile_request_period import BattlesControllerGetCombatProfileRequestPeriod
    from .battles_controller_get_combat_profile_request_sort_by import BattlesControllerGetCombatProfileRequestSortBy
    from .battles_controller_get_combat_profile_request_sort_order import (
        BattlesControllerGetCombatProfileRequestSortOrder,
    )
    from .battles_controller_get_current_streak_request_period import BattlesControllerGetCurrentStreakRequestPeriod
    from .battles_controller_get_current_streak_request_sort_by import BattlesControllerGetCurrentStreakRequestSortBy
    from .battles_controller_get_current_streak_request_sort_order import (
        BattlesControllerGetCurrentStreakRequestSortOrder,
    )
    from .battles_controller_get_dashboard_battles_request_result_item import (
        BattlesControllerGetDashboardBattlesRequestResultItem,
    )
    from .battles_controller_get_dashboard_battles_request_sort_order import (
        BattlesControllerGetDashboardBattlesRequestSortOrder,
    )
    from .battles_controller_get_dashboard_battles_request_type_item import (
        BattlesControllerGetDashboardBattlesRequestTypeItem,
    )
    from .battles_controller_get_head_to_head_request_period import BattlesControllerGetHeadToHeadRequestPeriod
    from .battles_controller_get_head_to_head_request_sort_by import BattlesControllerGetHeadToHeadRequestSortBy
    from .battles_controller_get_head_to_head_request_sort_order import BattlesControllerGetHeadToHeadRequestSortOrder
    from .battles_controller_get_ph_growth_request_period import BattlesControllerGetPhGrowthRequestPeriod
    from .battles_controller_get_ph_growth_request_sort_by import BattlesControllerGetPhGrowthRequestSortBy
    from .battles_controller_get_ph_growth_request_sort_order import BattlesControllerGetPhGrowthRequestSortOrder
    from .battles_controller_get_player_vs_player_battles_request_period import (
        BattlesControllerGetPlayerVsPlayerBattlesRequestPeriod,
    )
    from .battles_controller_get_player_vs_player_battles_request_sort_by import (
        BattlesControllerGetPlayerVsPlayerBattlesRequestSortBy,
    )
    from .battles_controller_get_player_vs_player_battles_request_sort_order import (
        BattlesControllerGetPlayerVsPlayerBattlesRequestSortOrder,
    )
    from .battles_controller_get_profession_win_rate_request_period import (
        BattlesControllerGetProfessionWinRateRequestPeriod,
    )
    from .battles_controller_get_profession_win_rate_request_sort_by import (
        BattlesControllerGetProfessionWinRateRequestSortBy,
    )
    from .battles_controller_get_profession_win_rate_request_sort_order import (
        BattlesControllerGetProfessionWinRateRequestSortOrder,
    )
    from .battles_controller_get_rating_delta_by_opponent_request_period import (
        BattlesControllerGetRatingDeltaByOpponentRequestPeriod,
    )
    from .battles_controller_get_rating_delta_by_opponent_request_sort_by import (
        BattlesControllerGetRatingDeltaByOpponentRequestSortBy,
    )
    from .battles_controller_get_rating_delta_by_opponent_request_sort_order import (
        BattlesControllerGetRatingDeltaByOpponentRequestSortOrder,
    )
    from .battles_controller_get_rating_growth_request_period import BattlesControllerGetRatingGrowthRequestPeriod
    from .battles_controller_get_rating_growth_request_sort_by import BattlesControllerGetRatingGrowthRequestSortBy
    from .battles_controller_get_rating_growth_request_sort_order import (
        BattlesControllerGetRatingGrowthRequestSortOrder,
    )
    from .create_battle_dto_events_item import CreateBattleDtoEventsItem
    from .create_battle_dto_events_item_f import CreateBattleDtoEventsItemF
    from .create_battle_dto_events_item_fw_value import CreateBattleDtoEventsItemFwValue
    from .create_battle_dto_events_item_match_summary import CreateBattleDtoEventsItemMatchSummary
    from .create_battle_dto_events_item_match_summary_daily_stage import CreateBattleDtoEventsItemMatchSummaryDailyStage
    from .create_battle_dto_events_item_party import CreateBattleDtoEventsItemParty
    from .create_battle_dto_events_item_party_members_value import CreateBattleDtoEventsItemPartyMembersValue
_dynamic_imports: typing.Dict[str, str] = {
    "BattlesControllerGetBattleAnalyticsRequestPeriod": ".battles_controller_get_battle_analytics_request_period",
    "BattlesControllerGetBattleDurationRequestPeriod": ".battles_controller_get_battle_duration_request_period",
    "BattlesControllerGetBattleDurationRequestSortBy": ".battles_controller_get_battle_duration_request_sort_by",
    "BattlesControllerGetBattleDurationRequestSortOrder": ".battles_controller_get_battle_duration_request_sort_order",
    "BattlesControllerGetCombatProfileRequestPeriod": ".battles_controller_get_combat_profile_request_period",
    "BattlesControllerGetCombatProfileRequestSortBy": ".battles_controller_get_combat_profile_request_sort_by",
    "BattlesControllerGetCombatProfileRequestSortOrder": ".battles_controller_get_combat_profile_request_sort_order",
    "BattlesControllerGetCurrentStreakRequestPeriod": ".battles_controller_get_current_streak_request_period",
    "BattlesControllerGetCurrentStreakRequestSortBy": ".battles_controller_get_current_streak_request_sort_by",
    "BattlesControllerGetCurrentStreakRequestSortOrder": ".battles_controller_get_current_streak_request_sort_order",
    "BattlesControllerGetDashboardBattlesRequestResultItem": ".battles_controller_get_dashboard_battles_request_result_item",
    "BattlesControllerGetDashboardBattlesRequestSortOrder": ".battles_controller_get_dashboard_battles_request_sort_order",
    "BattlesControllerGetDashboardBattlesRequestTypeItem": ".battles_controller_get_dashboard_battles_request_type_item",
    "BattlesControllerGetHeadToHeadRequestPeriod": ".battles_controller_get_head_to_head_request_period",
    "BattlesControllerGetHeadToHeadRequestSortBy": ".battles_controller_get_head_to_head_request_sort_by",
    "BattlesControllerGetHeadToHeadRequestSortOrder": ".battles_controller_get_head_to_head_request_sort_order",
    "BattlesControllerGetPhGrowthRequestPeriod": ".battles_controller_get_ph_growth_request_period",
    "BattlesControllerGetPhGrowthRequestSortBy": ".battles_controller_get_ph_growth_request_sort_by",
    "BattlesControllerGetPhGrowthRequestSortOrder": ".battles_controller_get_ph_growth_request_sort_order",
    "BattlesControllerGetPlayerVsPlayerBattlesRequestPeriod": ".battles_controller_get_player_vs_player_battles_request_period",
    "BattlesControllerGetPlayerVsPlayerBattlesRequestSortBy": ".battles_controller_get_player_vs_player_battles_request_sort_by",
    "BattlesControllerGetPlayerVsPlayerBattlesRequestSortOrder": ".battles_controller_get_player_vs_player_battles_request_sort_order",
    "BattlesControllerGetProfessionWinRateRequestPeriod": ".battles_controller_get_profession_win_rate_request_period",
    "BattlesControllerGetProfessionWinRateRequestSortBy": ".battles_controller_get_profession_win_rate_request_sort_by",
    "BattlesControllerGetProfessionWinRateRequestSortOrder": ".battles_controller_get_profession_win_rate_request_sort_order",
    "BattlesControllerGetRatingDeltaByOpponentRequestPeriod": ".battles_controller_get_rating_delta_by_opponent_request_period",
    "BattlesControllerGetRatingDeltaByOpponentRequestSortBy": ".battles_controller_get_rating_delta_by_opponent_request_sort_by",
    "BattlesControllerGetRatingDeltaByOpponentRequestSortOrder": ".battles_controller_get_rating_delta_by_opponent_request_sort_order",
    "BattlesControllerGetRatingGrowthRequestPeriod": ".battles_controller_get_rating_growth_request_period",
    "BattlesControllerGetRatingGrowthRequestSortBy": ".battles_controller_get_rating_growth_request_sort_by",
    "BattlesControllerGetRatingGrowthRequestSortOrder": ".battles_controller_get_rating_growth_request_sort_order",
    "CreateBattleDtoEventsItem": ".create_battle_dto_events_item",
    "CreateBattleDtoEventsItemF": ".create_battle_dto_events_item_f",
    "CreateBattleDtoEventsItemFwValue": ".create_battle_dto_events_item_fw_value",
    "CreateBattleDtoEventsItemMatchSummary": ".create_battle_dto_events_item_match_summary",
    "CreateBattleDtoEventsItemMatchSummaryDailyStage": ".create_battle_dto_events_item_match_summary_daily_stage",
    "CreateBattleDtoEventsItemParty": ".create_battle_dto_events_item_party",
    "CreateBattleDtoEventsItemPartyMembersValue": ".create_battle_dto_events_item_party_members_value",
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
    "BattlesControllerGetBattleAnalyticsRequestPeriod",
    "BattlesControllerGetBattleDurationRequestPeriod",
    "BattlesControllerGetBattleDurationRequestSortBy",
    "BattlesControllerGetBattleDurationRequestSortOrder",
    "BattlesControllerGetCombatProfileRequestPeriod",
    "BattlesControllerGetCombatProfileRequestSortBy",
    "BattlesControllerGetCombatProfileRequestSortOrder",
    "BattlesControllerGetCurrentStreakRequestPeriod",
    "BattlesControllerGetCurrentStreakRequestSortBy",
    "BattlesControllerGetCurrentStreakRequestSortOrder",
    "BattlesControllerGetDashboardBattlesRequestResultItem",
    "BattlesControllerGetDashboardBattlesRequestSortOrder",
    "BattlesControllerGetDashboardBattlesRequestTypeItem",
    "BattlesControllerGetHeadToHeadRequestPeriod",
    "BattlesControllerGetHeadToHeadRequestSortBy",
    "BattlesControllerGetHeadToHeadRequestSortOrder",
    "BattlesControllerGetPhGrowthRequestPeriod",
    "BattlesControllerGetPhGrowthRequestSortBy",
    "BattlesControllerGetPhGrowthRequestSortOrder",
    "BattlesControllerGetPlayerVsPlayerBattlesRequestPeriod",
    "BattlesControllerGetPlayerVsPlayerBattlesRequestSortBy",
    "BattlesControllerGetPlayerVsPlayerBattlesRequestSortOrder",
    "BattlesControllerGetProfessionWinRateRequestPeriod",
    "BattlesControllerGetProfessionWinRateRequestSortBy",
    "BattlesControllerGetProfessionWinRateRequestSortOrder",
    "BattlesControllerGetRatingDeltaByOpponentRequestPeriod",
    "BattlesControllerGetRatingDeltaByOpponentRequestSortBy",
    "BattlesControllerGetRatingDeltaByOpponentRequestSortOrder",
    "BattlesControllerGetRatingGrowthRequestPeriod",
    "BattlesControllerGetRatingGrowthRequestSortBy",
    "BattlesControllerGetRatingGrowthRequestSortOrder",
    "CreateBattleDtoEventsItem",
    "CreateBattleDtoEventsItemF",
    "CreateBattleDtoEventsItemFwValue",
    "CreateBattleDtoEventsItemMatchSummary",
    "CreateBattleDtoEventsItemMatchSummaryDailyStage",
    "CreateBattleDtoEventsItemParty",
    "CreateBattleDtoEventsItemPartyMembersValue",
]
