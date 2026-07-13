

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTokensClient, RawTokensClient
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


class TokensClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTokensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTokensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTokensClient
        """
        return self._raw_client

    def applymissingpartnerofferswithoutclaim(
        self,
        partner_application_id: int,
        target_bnet_membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokensApplyMissingPartnerOffersWithoutClaimResponse:
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
        TokensApplyMissingPartnerOffersWithoutClaimResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tokens.applymissingpartnerofferswithoutclaim(
            partner_application_id=1,
            target_bnet_membership_id=1000000,
        )
        """
        _response = self._raw_client.applymissingpartnerofferswithoutclaim(
            partner_application_id, target_bnet_membership_id, request_options=request_options
        )
        return _response.data

    def claimpartneroffer(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TokensClaimPartnerOfferResponse:
        """
        Claim a partner offer as the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokensClaimPartnerOfferResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tokens.claimpartneroffer()
        """
        _response = self._raw_client.claimpartneroffer(request_options=request_options)
        return _response.data

    def forcedropsrepair(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TokensForceDropsRepairResponse:
        """
        Twitch Drops self-repair function - scans twitch for drops not marked as fulfilled and resyncs them.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokensForceDropsRepairResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tokens.forcedropsrepair()
        """
        _response = self._raw_client.forcedropsrepair(request_options=request_options)
        return _response.data

    def getpartnerofferskuhistory(
        self,
        partner_application_id: int,
        target_bnet_membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokensGetPartnerOfferSkuHistoryResponse:
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
        TokensGetPartnerOfferSkuHistoryResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tokens.getpartnerofferskuhistory(
            partner_application_id=1,
            target_bnet_membership_id=1000000,
        )
        """
        _response = self._raw_client.getpartnerofferskuhistory(
            partner_application_id, target_bnet_membership_id, request_options=request_options
        )
        return _response.data

    def getpartnerrewardhistory(
        self,
        target_bnet_membership_id: int,
        partner_application_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokensGetPartnerRewardHistoryResponse:
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
        TokensGetPartnerRewardHistoryResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tokens.getpartnerrewardhistory(
            target_bnet_membership_id=1000000,
            partner_application_id=1,
        )
        """
        _response = self._raw_client.getpartnerrewardhistory(
            target_bnet_membership_id, partner_application_id, request_options=request_options
        )
        return _response.data

    def getbungierewardslist(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TokensGetBungieRewardsListResponse:
        """
        Returns a list of the current bungie rewards

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokensGetBungieRewardsListResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tokens.getbungierewardslist()
        """
        _response = self._raw_client.getbungierewardslist(request_options=request_options)
        return _response.data

    def getbungierewardsforplatformuser(
        self, membership_id: int, membership_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TokensGetBungieRewardsForPlatformUserResponse:
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
        TokensGetBungieRewardsForPlatformUserResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tokens.getbungierewardsforplatformuser(
            membership_id=1000000,
            membership_type=1,
        )
        """
        _response = self._raw_client.getbungierewardsforplatformuser(
            membership_id, membership_type, request_options=request_options
        )
        return _response.data

    def getbungierewardsforuser(
        self, membership_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TokensGetBungieRewardsForUserResponse:
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
        TokensGetBungieRewardsForUserResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tokens.getbungierewardsforuser(
            membership_id=1000000,
        )
        """
        _response = self._raw_client.getbungierewardsforuser(membership_id, request_options=request_options)
        return _response.data


class AsyncTokensClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTokensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTokensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTokensClient
        """
        return self._raw_client

    async def applymissingpartnerofferswithoutclaim(
        self,
        partner_application_id: int,
        target_bnet_membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokensApplyMissingPartnerOffersWithoutClaimResponse:
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
        TokensApplyMissingPartnerOffersWithoutClaimResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tokens.applymissingpartnerofferswithoutclaim(
                partner_application_id=1,
                target_bnet_membership_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.applymissingpartnerofferswithoutclaim(
            partner_application_id, target_bnet_membership_id, request_options=request_options
        )
        return _response.data

    async def claimpartneroffer(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TokensClaimPartnerOfferResponse:
        """
        Claim a partner offer as the authenticated user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokensClaimPartnerOfferResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tokens.claimpartneroffer()


        asyncio.run(main())
        """
        _response = await self._raw_client.claimpartneroffer(request_options=request_options)
        return _response.data

    async def forcedropsrepair(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TokensForceDropsRepairResponse:
        """
        Twitch Drops self-repair function - scans twitch for drops not marked as fulfilled and resyncs them.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokensForceDropsRepairResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tokens.forcedropsrepair()


        asyncio.run(main())
        """
        _response = await self._raw_client.forcedropsrepair(request_options=request_options)
        return _response.data

    async def getpartnerofferskuhistory(
        self,
        partner_application_id: int,
        target_bnet_membership_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokensGetPartnerOfferSkuHistoryResponse:
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
        TokensGetPartnerOfferSkuHistoryResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tokens.getpartnerofferskuhistory(
                partner_application_id=1,
                target_bnet_membership_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpartnerofferskuhistory(
            partner_application_id, target_bnet_membership_id, request_options=request_options
        )
        return _response.data

    async def getpartnerrewardhistory(
        self,
        target_bnet_membership_id: int,
        partner_application_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TokensGetPartnerRewardHistoryResponse:
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
        TokensGetPartnerRewardHistoryResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tokens.getpartnerrewardhistory(
                target_bnet_membership_id=1000000,
                partner_application_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpartnerrewardhistory(
            target_bnet_membership_id, partner_application_id, request_options=request_options
        )
        return _response.data

    async def getbungierewardslist(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TokensGetBungieRewardsListResponse:
        """
        Returns a list of the current bungie rewards

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokensGetBungieRewardsListResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tokens.getbungierewardslist()


        asyncio.run(main())
        """
        _response = await self._raw_client.getbungierewardslist(request_options=request_options)
        return _response.data

    async def getbungierewardsforplatformuser(
        self, membership_id: int, membership_type: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TokensGetBungieRewardsForPlatformUserResponse:
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
        TokensGetBungieRewardsForPlatformUserResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tokens.getbungierewardsforplatformuser(
                membership_id=1000000,
                membership_type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getbungierewardsforplatformuser(
            membership_id, membership_type, request_options=request_options
        )
        return _response.data

    async def getbungierewardsforuser(
        self, membership_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TokensGetBungieRewardsForUserResponse:
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
        TokensGetBungieRewardsForUserResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tokens.getbungierewardsforuser(
                membership_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getbungierewardsforuser(membership_id, request_options=request_options)
        return _response.data
