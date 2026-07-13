



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .tokens_apply_missing_partner_offers_without_claim_response import (
        TokensApplyMissingPartnerOffersWithoutClaimResponse,
    )
    from .tokens_claim_partner_offer_response import TokensClaimPartnerOfferResponse
    from .tokens_force_drops_repair_response import TokensForceDropsRepairResponse
    from .tokens_get_bungie_rewards_for_platform_user_response import TokensGetBungieRewardsForPlatformUserResponse
    from .tokens_get_bungie_rewards_for_user_response import TokensGetBungieRewardsForUserResponse
    from .tokens_get_bungie_rewards_list_response import TokensGetBungieRewardsListResponse
    from .tokens_get_partner_offer_sku_history_response import TokensGetPartnerOfferSkuHistoryResponse
    from .tokens_get_partner_reward_history_response import TokensGetPartnerRewardHistoryResponse
_dynamic_imports: typing.Dict[str, str] = {
    "TokensApplyMissingPartnerOffersWithoutClaimResponse": ".tokens_apply_missing_partner_offers_without_claim_response",
    "TokensClaimPartnerOfferResponse": ".tokens_claim_partner_offer_response",
    "TokensForceDropsRepairResponse": ".tokens_force_drops_repair_response",
    "TokensGetBungieRewardsForPlatformUserResponse": ".tokens_get_bungie_rewards_for_platform_user_response",
    "TokensGetBungieRewardsForUserResponse": ".tokens_get_bungie_rewards_for_user_response",
    "TokensGetBungieRewardsListResponse": ".tokens_get_bungie_rewards_list_response",
    "TokensGetPartnerOfferSkuHistoryResponse": ".tokens_get_partner_offer_sku_history_response",
    "TokensGetPartnerRewardHistoryResponse": ".tokens_get_partner_reward_history_response",
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
    "TokensApplyMissingPartnerOffersWithoutClaimResponse",
    "TokensClaimPartnerOfferResponse",
    "TokensForceDropsRepairResponse",
    "TokensGetBungieRewardsForPlatformUserResponse",
    "TokensGetBungieRewardsForUserResponse",
    "TokensGetBungieRewardsListResponse",
    "TokensGetPartnerOfferSkuHistoryResponse",
    "TokensGetPartnerRewardHistoryResponse",
]
