



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Destiny2AwaGetActionTokenResponse,
        Destiny2AwaInitializeRequestResponse,
        Destiny2AwaProvideAuthorizationResultResponse,
        Destiny2ClearLoadoutResponse,
        Destiny2EquipItemResponse,
        Destiny2EquipItemsResponse,
        Destiny2EquipLoadoutResponse,
        Destiny2GetActivityHistoryResponse,
        Destiny2GetCharacterResponse,
        Destiny2GetClanAggregateStatsResponse,
        Destiny2GetClanBannerSourceResponse,
        Destiny2GetClanLeaderboardsResponse,
        Destiny2GetClanWeeklyRewardStateResponse,
        Destiny2GetCollectibleNodeDetailsResponse,
        Destiny2GetDestinyAggregateActivityStatsResponse,
        Destiny2GetDestinyEntityDefinitionResponse,
        Destiny2GetDestinyManifestResponse,
        Destiny2GetHistoricalStatsDefinitionResponse,
        Destiny2GetHistoricalStatsForAccountResponse,
        Destiny2GetHistoricalStatsResponse,
        Destiny2GetItemResponse,
        Destiny2GetLeaderboardsForCharacterResponse,
        Destiny2GetLeaderboardsResponse,
        Destiny2GetLinkedProfilesResponse,
        Destiny2GetPostGameCarnageReportResponse,
        Destiny2GetProfileResponse,
        Destiny2GetPublicMilestoneContentResponse,
        Destiny2GetPublicMilestonesResponse,
        Destiny2GetPublicVendorsResponse,
        Destiny2GetUniqueWeaponHistoryResponse,
        Destiny2GetVendorResponse,
        Destiny2GetVendorsResponse,
        Destiny2InsertSocketPlugFreeResponse,
        Destiny2InsertSocketPlugResponse,
        Destiny2PullFromPostmasterResponse,
        Destiny2ReportOffensivePostGameCarnageReportPlayerResponse,
        Destiny2SearchDestinyEntitiesResponse,
        Destiny2SearchDestinyPlayerByBungieNameResponse,
        Destiny2SetItemLockStateResponse,
        Destiny2SetQuestTrackedStateResponse,
        Destiny2SnapshotLoadoutResponse,
        Destiny2TransferItemResponse,
        Destiny2UpdateLoadoutIdentifiersResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "Destiny2AwaGetActionTokenResponse": ".types",
    "Destiny2AwaInitializeRequestResponse": ".types",
    "Destiny2AwaProvideAuthorizationResultResponse": ".types",
    "Destiny2ClearLoadoutResponse": ".types",
    "Destiny2EquipItemResponse": ".types",
    "Destiny2EquipItemsResponse": ".types",
    "Destiny2EquipLoadoutResponse": ".types",
    "Destiny2GetActivityHistoryResponse": ".types",
    "Destiny2GetCharacterResponse": ".types",
    "Destiny2GetClanAggregateStatsResponse": ".types",
    "Destiny2GetClanBannerSourceResponse": ".types",
    "Destiny2GetClanLeaderboardsResponse": ".types",
    "Destiny2GetClanWeeklyRewardStateResponse": ".types",
    "Destiny2GetCollectibleNodeDetailsResponse": ".types",
    "Destiny2GetDestinyAggregateActivityStatsResponse": ".types",
    "Destiny2GetDestinyEntityDefinitionResponse": ".types",
    "Destiny2GetDestinyManifestResponse": ".types",
    "Destiny2GetHistoricalStatsDefinitionResponse": ".types",
    "Destiny2GetHistoricalStatsForAccountResponse": ".types",
    "Destiny2GetHistoricalStatsResponse": ".types",
    "Destiny2GetItemResponse": ".types",
    "Destiny2GetLeaderboardsForCharacterResponse": ".types",
    "Destiny2GetLeaderboardsResponse": ".types",
    "Destiny2GetLinkedProfilesResponse": ".types",
    "Destiny2GetPostGameCarnageReportResponse": ".types",
    "Destiny2GetProfileResponse": ".types",
    "Destiny2GetPublicMilestoneContentResponse": ".types",
    "Destiny2GetPublicMilestonesResponse": ".types",
    "Destiny2GetPublicVendorsResponse": ".types",
    "Destiny2GetUniqueWeaponHistoryResponse": ".types",
    "Destiny2GetVendorResponse": ".types",
    "Destiny2GetVendorsResponse": ".types",
    "Destiny2InsertSocketPlugFreeResponse": ".types",
    "Destiny2InsertSocketPlugResponse": ".types",
    "Destiny2PullFromPostmasterResponse": ".types",
    "Destiny2ReportOffensivePostGameCarnageReportPlayerResponse": ".types",
    "Destiny2SearchDestinyEntitiesResponse": ".types",
    "Destiny2SearchDestinyPlayerByBungieNameResponse": ".types",
    "Destiny2SetItemLockStateResponse": ".types",
    "Destiny2SetQuestTrackedStateResponse": ".types",
    "Destiny2SnapshotLoadoutResponse": ".types",
    "Destiny2TransferItemResponse": ".types",
    "Destiny2UpdateLoadoutIdentifiersResponse": ".types",
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
