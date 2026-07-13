

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.tokens_apply_missing_partner_offers_without_claim_response import (
    TokensApplyMissingPartnerOffersWithoutClaimResponse,
)
from .types.tokens_claim_partner_offer_response import TokensClaimPartnerOfferResponse
from .types.tokens_force_drops_repair_response import TokensForceDropsRepairResponse
from .types.tokens_get_bungie_rewards_for_platform_user_response import TokensGetBungieRewardsForPlatformUserResponse
from .types.tokens_get_bungie_rewards_for_user_response import TokensGetBungieRewardsForUserResponse
from .types.tokens_get_bungie_rewards_list_response import TokensGetBungieRewardsListResponse
from .types.tokens_get_partner_offer_sku_history_response import TokensGetPartnerOfferSkuHistoryResponse
from .types.tokens_get_partner_reward_history_response import TokensGetPartnerRewardHistoryResponse


class RawTokensClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def applymissingpartnerofferswithoutclaim(
        self,
        partner_application_id: int,
        target_bnet_membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TokensApplyMissingPartnerOffersWithoutClaimResponse]:
        """
        Apply a partner offer to the targeted user. This endpoint does not claim a new offer, but any already claimed offers will be applied to the game if not already.

        Parameters
        ----------
        partner_application_id : int
            The partner application identifier.

        target_bnet_membership_id : int
            The bungie.net user to apply missing offers to. If not self, elevated permissions are required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokensApplyMissingPartnerOffersWithoutClaimResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Tokens/Partner/ApplyMissingOffers/{jsonable_encoder(partner_application_id)}/{jsonable_encoder(target_bnet_membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokensApplyMissingPartnerOffersWithoutClaimResponse,
                    parse_obj_as(
                        type_=TokensApplyMissingPartnerOffersWithoutClaimResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def claimpartneroffer(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TokensClaimPartnerOfferResponse]:
        """
        Claim a partner offer as the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokensClaimPartnerOfferResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Tokens/Partner/ClaimOffer/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokensClaimPartnerOfferResponse,
                    parse_obj_as(
                        type_=TokensClaimPartnerOfferResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def forcedropsrepair(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TokensForceDropsRepairResponse]:
        """
        Twitch Drops self-repair function - scans twitch for drops not marked as fulfilled and resyncs them.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokensForceDropsRepairResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Tokens/Partner/ForceDropsRepair/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokensForceDropsRepairResponse,
                    parse_obj_as(
                        type_=TokensForceDropsRepairResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getpartnerofferskuhistory(
        self,
        partner_application_id: int,
        target_bnet_membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TokensGetPartnerOfferSkuHistoryResponse]:
        """
        Returns the partner sku and offer history of the targeted user. Elevated permissions are required to see users that are not yourself.

        Parameters
        ----------
        partner_application_id : int
            The partner application identifier.

        target_bnet_membership_id : int
            The bungie.net user to apply missing offers to. If not self, elevated permissions are required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokensGetPartnerOfferSkuHistoryResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Tokens/Partner/History/{jsonable_encoder(partner_application_id)}/{jsonable_encoder(target_bnet_membership_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokensGetPartnerOfferSkuHistoryResponse,
                    parse_obj_as(
                        type_=TokensGetPartnerOfferSkuHistoryResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getpartnerrewardhistory(
        self,
        target_bnet_membership_id: int,
        partner_application_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TokensGetPartnerRewardHistoryResponse]:
        """
        Returns the partner rewards history of the targeted user, both partner offers and Twitch drops.

        Parameters
        ----------
        target_bnet_membership_id : int
            The bungie.net user to return reward history for.

        partner_application_id : int
            The partner application identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokensGetPartnerRewardHistoryResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Tokens/Partner/History/{jsonable_encoder(target_bnet_membership_id)}/Application/{jsonable_encoder(partner_application_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokensGetPartnerRewardHistoryResponse,
                    parse_obj_as(
                        type_=TokensGetPartnerRewardHistoryResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getbungierewardslist(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TokensGetBungieRewardsListResponse]:
        """
        Returns a list of the current bungie rewards

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokensGetBungieRewardsListResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Tokens/Rewards/BungieRewards/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokensGetBungieRewardsListResponse,
                    parse_obj_as(
                        type_=TokensGetBungieRewardsListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getbungierewardsforplatformuser(
        self, membership_id: int, membership_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TokensGetBungieRewardsForPlatformUserResponse]:
        """
        Returns the bungie rewards for the targeted user when a platform membership Id and Type are used.

        Parameters
        ----------
        membership_id : int
            users platform membershipId for requested user rewards. If not self, elevated permissions are required.

        membership_type : int
            The target Destiny 2 membership type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokensGetBungieRewardsForPlatformUserResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Tokens/Rewards/GetRewardsForPlatformUser/{jsonable_encoder(membership_id)}/{jsonable_encoder(membership_type)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokensGetBungieRewardsForPlatformUserResponse,
                    parse_obj_as(
                        type_=TokensGetBungieRewardsForPlatformUserResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getbungierewardsforuser(
        self, membership_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TokensGetBungieRewardsForUserResponse]:
        """
        Returns the bungie rewards for the targeted user.

        Parameters
        ----------
        membership_id : int
            bungie.net user membershipId for requested user rewards. If not self, elevated permissions are required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokensGetBungieRewardsForUserResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Tokens/Rewards/GetRewardsForUser/{jsonable_encoder(membership_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokensGetBungieRewardsForUserResponse,
                    parse_obj_as(
                        type_=TokensGetBungieRewardsForUserResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTokensClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def applymissingpartnerofferswithoutclaim(
        self,
        partner_application_id: int,
        target_bnet_membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TokensApplyMissingPartnerOffersWithoutClaimResponse]:
        """
        Apply a partner offer to the targeted user. This endpoint does not claim a new offer, but any already claimed offers will be applied to the game if not already.

        Parameters
        ----------
        partner_application_id : int
            The partner application identifier.

        target_bnet_membership_id : int
            The bungie.net user to apply missing offers to. If not self, elevated permissions are required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokensApplyMissingPartnerOffersWithoutClaimResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Tokens/Partner/ApplyMissingOffers/{jsonable_encoder(partner_application_id)}/{jsonable_encoder(target_bnet_membership_id)}/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokensApplyMissingPartnerOffersWithoutClaimResponse,
                    parse_obj_as(
                        type_=TokensApplyMissingPartnerOffersWithoutClaimResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def claimpartneroffer(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TokensClaimPartnerOfferResponse]:
        """
        Claim a partner offer as the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokensClaimPartnerOfferResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Tokens/Partner/ClaimOffer/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokensClaimPartnerOfferResponse,
                    parse_obj_as(
                        type_=TokensClaimPartnerOfferResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def forcedropsrepair(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TokensForceDropsRepairResponse]:
        """
        Twitch Drops self-repair function - scans twitch for drops not marked as fulfilled and resyncs them.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokensForceDropsRepairResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Tokens/Partner/ForceDropsRepair/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokensForceDropsRepairResponse,
                    parse_obj_as(
                        type_=TokensForceDropsRepairResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getpartnerofferskuhistory(
        self,
        partner_application_id: int,
        target_bnet_membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TokensGetPartnerOfferSkuHistoryResponse]:
        """
        Returns the partner sku and offer history of the targeted user. Elevated permissions are required to see users that are not yourself.

        Parameters
        ----------
        partner_application_id : int
            The partner application identifier.

        target_bnet_membership_id : int
            The bungie.net user to apply missing offers to. If not self, elevated permissions are required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokensGetPartnerOfferSkuHistoryResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Tokens/Partner/History/{jsonable_encoder(partner_application_id)}/{jsonable_encoder(target_bnet_membership_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokensGetPartnerOfferSkuHistoryResponse,
                    parse_obj_as(
                        type_=TokensGetPartnerOfferSkuHistoryResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getpartnerrewardhistory(
        self,
        target_bnet_membership_id: int,
        partner_application_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TokensGetPartnerRewardHistoryResponse]:
        """
        Returns the partner rewards history of the targeted user, both partner offers and Twitch drops.

        Parameters
        ----------
        target_bnet_membership_id : int
            The bungie.net user to return reward history for.

        partner_application_id : int
            The partner application identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokensGetPartnerRewardHistoryResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Tokens/Partner/History/{jsonable_encoder(target_bnet_membership_id)}/Application/{jsonable_encoder(partner_application_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokensGetPartnerRewardHistoryResponse,
                    parse_obj_as(
                        type_=TokensGetPartnerRewardHistoryResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getbungierewardslist(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TokensGetBungieRewardsListResponse]:
        """
        Returns a list of the current bungie rewards

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokensGetBungieRewardsListResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Tokens/Rewards/BungieRewards/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokensGetBungieRewardsListResponse,
                    parse_obj_as(
                        type_=TokensGetBungieRewardsListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getbungierewardsforplatformuser(
        self, membership_id: int, membership_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TokensGetBungieRewardsForPlatformUserResponse]:
        """
        Returns the bungie rewards for the targeted user when a platform membership Id and Type are used.

        Parameters
        ----------
        membership_id : int
            users platform membershipId for requested user rewards. If not self, elevated permissions are required.

        membership_type : int
            The target Destiny 2 membership type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokensGetBungieRewardsForPlatformUserResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Tokens/Rewards/GetRewardsForPlatformUser/{jsonable_encoder(membership_id)}/{jsonable_encoder(membership_type)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokensGetBungieRewardsForPlatformUserResponse,
                    parse_obj_as(
                        type_=TokensGetBungieRewardsForPlatformUserResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getbungierewardsforuser(
        self, membership_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TokensGetBungieRewardsForUserResponse]:
        """
        Returns the bungie rewards for the targeted user.

        Parameters
        ----------
        membership_id : int
            bungie.net user membershipId for requested user rewards. If not self, elevated permissions are required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokensGetBungieRewardsForUserResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Tokens/Rewards/GetRewardsForUser/{jsonable_encoder(membership_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokensGetBungieRewardsForUserResponse,
                    parse_obj_as(
                        type_=TokensGetBungieRewardsForUserResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
