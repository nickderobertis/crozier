



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BattlesControllerGetBattleAnalyticsRequestPeriod,
        BattlesControllerGetBattleDurationRequestPeriod,
        BattlesControllerGetBattleDurationRequestSortBy,
        BattlesControllerGetBattleDurationRequestSortOrder,
        BattlesControllerGetCombatProfileRequestPeriod,
        BattlesControllerGetCombatProfileRequestSortBy,
        BattlesControllerGetCombatProfileRequestSortOrder,
        BattlesControllerGetCurrentStreakRequestPeriod,
        BattlesControllerGetCurrentStreakRequestSortBy,
        BattlesControllerGetCurrentStreakRequestSortOrder,
        BattlesControllerGetDashboardBattlesRequestResultItem,
        BattlesControllerGetDashboardBattlesRequestSortOrder,
        BattlesControllerGetDashboardBattlesRequestTypeItem,
        BattlesControllerGetHeadToHeadRequestPeriod,
        BattlesControllerGetHeadToHeadRequestSortBy,
        BattlesControllerGetHeadToHeadRequestSortOrder,
        BattlesControllerGetPhGrowthRequestPeriod,
        BattlesControllerGetPhGrowthRequestSortBy,
        BattlesControllerGetPhGrowthRequestSortOrder,
        BattlesControllerGetPlayerVsPlayerBattlesRequestPeriod,
        BattlesControllerGetPlayerVsPlayerBattlesRequestSortBy,
        BattlesControllerGetPlayerVsPlayerBattlesRequestSortOrder,
        BattlesControllerGetProfessionWinRateRequestPeriod,
        BattlesControllerGetProfessionWinRateRequestSortBy,
        BattlesControllerGetProfessionWinRateRequestSortOrder,
        BattlesControllerGetRatingDeltaByOpponentRequestPeriod,
        BattlesControllerGetRatingDeltaByOpponentRequestSortBy,
        BattlesControllerGetRatingDeltaByOpponentRequestSortOrder,
        BattlesControllerGetRatingGrowthRequestPeriod,
        BattlesControllerGetRatingGrowthRequestSortBy,
        BattlesControllerGetRatingGrowthRequestSortOrder,
        CreateBattleDtoEventsItem,
        CreateBattleDtoEventsItemF,
        CreateBattleDtoEventsItemFwValue,
        CreateBattleDtoEventsItemMatchSummary,
        CreateBattleDtoEventsItemMatchSummaryDailyStage,
        CreateBattleDtoEventsItemParty,
        CreateBattleDtoEventsItemPartyMembersValue,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "BattlesControllerGetBattleAnalyticsRequestPeriod": ".types",
    "BattlesControllerGetBattleDurationRequestPeriod": ".types",
    "BattlesControllerGetBattleDurationRequestSortBy": ".types",
    "BattlesControllerGetBattleDurationRequestSortOrder": ".types",
    "BattlesControllerGetCombatProfileRequestPeriod": ".types",
    "BattlesControllerGetCombatProfileRequestSortBy": ".types",
    "BattlesControllerGetCombatProfileRequestSortOrder": ".types",
    "BattlesControllerGetCurrentStreakRequestPeriod": ".types",
    "BattlesControllerGetCurrentStreakRequestSortBy": ".types",
    "BattlesControllerGetCurrentStreakRequestSortOrder": ".types",
    "BattlesControllerGetDashboardBattlesRequestResultItem": ".types",
    "BattlesControllerGetDashboardBattlesRequestSortOrder": ".types",
    "BattlesControllerGetDashboardBattlesRequestTypeItem": ".types",
    "BattlesControllerGetHeadToHeadRequestPeriod": ".types",
    "BattlesControllerGetHeadToHeadRequestSortBy": ".types",
    "BattlesControllerGetHeadToHeadRequestSortOrder": ".types",
    "BattlesControllerGetPhGrowthRequestPeriod": ".types",
    "BattlesControllerGetPhGrowthRequestSortBy": ".types",
    "BattlesControllerGetPhGrowthRequestSortOrder": ".types",
    "BattlesControllerGetPlayerVsPlayerBattlesRequestPeriod": ".types",
    "BattlesControllerGetPlayerVsPlayerBattlesRequestSortBy": ".types",
    "BattlesControllerGetPlayerVsPlayerBattlesRequestSortOrder": ".types",
    "BattlesControllerGetProfessionWinRateRequestPeriod": ".types",
    "BattlesControllerGetProfessionWinRateRequestSortBy": ".types",
    "BattlesControllerGetProfessionWinRateRequestSortOrder": ".types",
    "BattlesControllerGetRatingDeltaByOpponentRequestPeriod": ".types",
    "BattlesControllerGetRatingDeltaByOpponentRequestSortBy": ".types",
    "BattlesControllerGetRatingDeltaByOpponentRequestSortOrder": ".types",
    "BattlesControllerGetRatingGrowthRequestPeriod": ".types",
    "BattlesControllerGetRatingGrowthRequestSortBy": ".types",
    "BattlesControllerGetRatingGrowthRequestSortOrder": ".types",
    "CreateBattleDtoEventsItem": ".types",
    "CreateBattleDtoEventsItemF": ".types",
    "CreateBattleDtoEventsItemFwValue": ".types",
    "CreateBattleDtoEventsItemMatchSummary": ".types",
    "CreateBattleDtoEventsItemMatchSummaryDailyStage": ".types",
    "CreateBattleDtoEventsItemParty": ".types",
    "CreateBattleDtoEventsItemPartyMembersValue": ".types",
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
