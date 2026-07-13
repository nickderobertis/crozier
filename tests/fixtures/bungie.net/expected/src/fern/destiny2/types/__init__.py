



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .destiny2awa_get_action_token_response import Destiny2AwaGetActionTokenResponse
    from .destiny2awa_initialize_request_response import Destiny2AwaInitializeRequestResponse
    from .destiny2awa_provide_authorization_result_response import Destiny2AwaProvideAuthorizationResultResponse
    from .destiny2clear_loadout_response import Destiny2ClearLoadoutResponse
    from .destiny2equip_item_response import Destiny2EquipItemResponse
    from .destiny2equip_items_response import Destiny2EquipItemsResponse
    from .destiny2equip_loadout_response import Destiny2EquipLoadoutResponse
    from .destiny2get_activity_history_response import Destiny2GetActivityHistoryResponse
    from .destiny2get_character_response import Destiny2GetCharacterResponse
    from .destiny2get_clan_aggregate_stats_response import Destiny2GetClanAggregateStatsResponse
    from .destiny2get_clan_banner_source_response import Destiny2GetClanBannerSourceResponse
    from .destiny2get_clan_leaderboards_response import Destiny2GetClanLeaderboardsResponse
    from .destiny2get_clan_weekly_reward_state_response import Destiny2GetClanWeeklyRewardStateResponse
    from .destiny2get_collectible_node_details_response import Destiny2GetCollectibleNodeDetailsResponse
    from .destiny2get_destiny_aggregate_activity_stats_response import Destiny2GetDestinyAggregateActivityStatsResponse
    from .destiny2get_destiny_entity_definition_response import Destiny2GetDestinyEntityDefinitionResponse
    from .destiny2get_destiny_manifest_response import Destiny2GetDestinyManifestResponse
    from .destiny2get_historical_stats_definition_response import Destiny2GetHistoricalStatsDefinitionResponse
    from .destiny2get_historical_stats_for_account_response import Destiny2GetHistoricalStatsForAccountResponse
    from .destiny2get_historical_stats_response import Destiny2GetHistoricalStatsResponse
    from .destiny2get_item_response import Destiny2GetItemResponse
    from .destiny2get_leaderboards_for_character_response import Destiny2GetLeaderboardsForCharacterResponse
    from .destiny2get_leaderboards_response import Destiny2GetLeaderboardsResponse
    from .destiny2get_linked_profiles_response import Destiny2GetLinkedProfilesResponse
    from .destiny2get_post_game_carnage_report_response import Destiny2GetPostGameCarnageReportResponse
    from .destiny2get_profile_response import Destiny2GetProfileResponse
    from .destiny2get_public_milestone_content_response import Destiny2GetPublicMilestoneContentResponse
    from .destiny2get_public_milestones_response import Destiny2GetPublicMilestonesResponse
    from .destiny2get_public_vendors_response import Destiny2GetPublicVendorsResponse
    from .destiny2get_unique_weapon_history_response import Destiny2GetUniqueWeaponHistoryResponse
    from .destiny2get_vendor_response import Destiny2GetVendorResponse
    from .destiny2get_vendors_response import Destiny2GetVendorsResponse
    from .destiny2insert_socket_plug_free_response import Destiny2InsertSocketPlugFreeResponse
    from .destiny2insert_socket_plug_response import Destiny2InsertSocketPlugResponse
    from .destiny2pull_from_postmaster_response import Destiny2PullFromPostmasterResponse
    from .destiny2report_offensive_post_game_carnage_report_player_response import (
        Destiny2ReportOffensivePostGameCarnageReportPlayerResponse,
    )
    from .destiny2search_destiny_entities_response import Destiny2SearchDestinyEntitiesResponse
    from .destiny2search_destiny_player_by_bungie_name_response import Destiny2SearchDestinyPlayerByBungieNameResponse
    from .destiny2set_item_lock_state_response import Destiny2SetItemLockStateResponse
    from .destiny2set_quest_tracked_state_response import Destiny2SetQuestTrackedStateResponse
    from .destiny2snapshot_loadout_response import Destiny2SnapshotLoadoutResponse
    from .destiny2transfer_item_response import Destiny2TransferItemResponse
    from .destiny2update_loadout_identifiers_response import Destiny2UpdateLoadoutIdentifiersResponse
_dynamic_imports: typing.Dict[str, str] = {
    "Destiny2AwaGetActionTokenResponse": ".destiny2awa_get_action_token_response",
    "Destiny2AwaInitializeRequestResponse": ".destiny2awa_initialize_request_response",
    "Destiny2AwaProvideAuthorizationResultResponse": ".destiny2awa_provide_authorization_result_response",
    "Destiny2ClearLoadoutResponse": ".destiny2clear_loadout_response",
    "Destiny2EquipItemResponse": ".destiny2equip_item_response",
    "Destiny2EquipItemsResponse": ".destiny2equip_items_response",
    "Destiny2EquipLoadoutResponse": ".destiny2equip_loadout_response",
    "Destiny2GetActivityHistoryResponse": ".destiny2get_activity_history_response",
    "Destiny2GetCharacterResponse": ".destiny2get_character_response",
    "Destiny2GetClanAggregateStatsResponse": ".destiny2get_clan_aggregate_stats_response",
    "Destiny2GetClanBannerSourceResponse": ".destiny2get_clan_banner_source_response",
    "Destiny2GetClanLeaderboardsResponse": ".destiny2get_clan_leaderboards_response",
    "Destiny2GetClanWeeklyRewardStateResponse": ".destiny2get_clan_weekly_reward_state_response",
    "Destiny2GetCollectibleNodeDetailsResponse": ".destiny2get_collectible_node_details_response",
    "Destiny2GetDestinyAggregateActivityStatsResponse": ".destiny2get_destiny_aggregate_activity_stats_response",
    "Destiny2GetDestinyEntityDefinitionResponse": ".destiny2get_destiny_entity_definition_response",
    "Destiny2GetDestinyManifestResponse": ".destiny2get_destiny_manifest_response",
    "Destiny2GetHistoricalStatsDefinitionResponse": ".destiny2get_historical_stats_definition_response",
    "Destiny2GetHistoricalStatsForAccountResponse": ".destiny2get_historical_stats_for_account_response",
    "Destiny2GetHistoricalStatsResponse": ".destiny2get_historical_stats_response",
    "Destiny2GetItemResponse": ".destiny2get_item_response",
    "Destiny2GetLeaderboardsForCharacterResponse": ".destiny2get_leaderboards_for_character_response",
    "Destiny2GetLeaderboardsResponse": ".destiny2get_leaderboards_response",
    "Destiny2GetLinkedProfilesResponse": ".destiny2get_linked_profiles_response",
    "Destiny2GetPostGameCarnageReportResponse": ".destiny2get_post_game_carnage_report_response",
    "Destiny2GetProfileResponse": ".destiny2get_profile_response",
    "Destiny2GetPublicMilestoneContentResponse": ".destiny2get_public_milestone_content_response",
    "Destiny2GetPublicMilestonesResponse": ".destiny2get_public_milestones_response",
    "Destiny2GetPublicVendorsResponse": ".destiny2get_public_vendors_response",
    "Destiny2GetUniqueWeaponHistoryResponse": ".destiny2get_unique_weapon_history_response",
    "Destiny2GetVendorResponse": ".destiny2get_vendor_response",
    "Destiny2GetVendorsResponse": ".destiny2get_vendors_response",
    "Destiny2InsertSocketPlugFreeResponse": ".destiny2insert_socket_plug_free_response",
    "Destiny2InsertSocketPlugResponse": ".destiny2insert_socket_plug_response",
    "Destiny2PullFromPostmasterResponse": ".destiny2pull_from_postmaster_response",
    "Destiny2ReportOffensivePostGameCarnageReportPlayerResponse": ".destiny2report_offensive_post_game_carnage_report_player_response",
    "Destiny2SearchDestinyEntitiesResponse": ".destiny2search_destiny_entities_response",
    "Destiny2SearchDestinyPlayerByBungieNameResponse": ".destiny2search_destiny_player_by_bungie_name_response",
    "Destiny2SetItemLockStateResponse": ".destiny2set_item_lock_state_response",
    "Destiny2SetQuestTrackedStateResponse": ".destiny2set_quest_tracked_state_response",
    "Destiny2SnapshotLoadoutResponse": ".destiny2snapshot_loadout_response",
    "Destiny2TransferItemResponse": ".destiny2transfer_item_response",
    "Destiny2UpdateLoadoutIdentifiersResponse": ".destiny2update_loadout_identifiers_response",
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
    "Destiny2AwaGetActionTokenResponse",
    "Destiny2AwaInitializeRequestResponse",
    "Destiny2AwaProvideAuthorizationResultResponse",
    "Destiny2ClearLoadoutResponse",
    "Destiny2EquipItemResponse",
    "Destiny2EquipItemsResponse",
    "Destiny2EquipLoadoutResponse",
    "Destiny2GetActivityHistoryResponse",
    "Destiny2GetCharacterResponse",
    "Destiny2GetClanAggregateStatsResponse",
    "Destiny2GetClanBannerSourceResponse",
    "Destiny2GetClanLeaderboardsResponse",
    "Destiny2GetClanWeeklyRewardStateResponse",
    "Destiny2GetCollectibleNodeDetailsResponse",
    "Destiny2GetDestinyAggregateActivityStatsResponse",
    "Destiny2GetDestinyEntityDefinitionResponse",
    "Destiny2GetDestinyManifestResponse",
    "Destiny2GetHistoricalStatsDefinitionResponse",
    "Destiny2GetHistoricalStatsForAccountResponse",
    "Destiny2GetHistoricalStatsResponse",
    "Destiny2GetItemResponse",
    "Destiny2GetLeaderboardsForCharacterResponse",
    "Destiny2GetLeaderboardsResponse",
    "Destiny2GetLinkedProfilesResponse",
    "Destiny2GetPostGameCarnageReportResponse",
    "Destiny2GetProfileResponse",
    "Destiny2GetPublicMilestoneContentResponse",
    "Destiny2GetPublicMilestonesResponse",
    "Destiny2GetPublicVendorsResponse",
    "Destiny2GetUniqueWeaponHistoryResponse",
    "Destiny2GetVendorResponse",
    "Destiny2GetVendorsResponse",
    "Destiny2InsertSocketPlugFreeResponse",
    "Destiny2InsertSocketPlugResponse",
    "Destiny2PullFromPostmasterResponse",
    "Destiny2ReportOffensivePostGameCarnageReportPlayerResponse",
    "Destiny2SearchDestinyEntitiesResponse",
    "Destiny2SearchDestinyPlayerByBungieNameResponse",
    "Destiny2SetItemLockStateResponse",
    "Destiny2SetQuestTrackedStateResponse",
    "Destiny2SnapshotLoadoutResponse",
    "Destiny2TransferItemResponse",
    "Destiny2UpdateLoadoutIdentifiersResponse",
]
