

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.accumulate_loyalty_points_response import AccumulateLoyaltyPointsResponse
from ..types.adjust_loyalty_points_response import AdjustLoyaltyPointsResponse
from ..types.calculate_loyalty_points_response import CalculateLoyaltyPointsResponse
from ..types.create_loyalty_account_response import CreateLoyaltyAccountResponse
from ..types.create_loyalty_reward_response import CreateLoyaltyRewardResponse
from ..types.delete_loyalty_reward_response import DeleteLoyaltyRewardResponse
from ..types.list_loyalty_programs_response import ListLoyaltyProgramsResponse
from ..types.loyalty_account import LoyaltyAccount
from ..types.loyalty_event_accumulate_points import LoyaltyEventAccumulatePoints
from ..types.loyalty_event_adjust_points import LoyaltyEventAdjustPoints
from ..types.loyalty_event_query import LoyaltyEventQuery
from ..types.loyalty_reward import LoyaltyReward
from ..types.money import Money
from ..types.redeem_loyalty_reward_response import RedeemLoyaltyRewardResponse
from ..types.retrieve_loyalty_account_response import RetrieveLoyaltyAccountResponse
from ..types.retrieve_loyalty_program_response import RetrieveLoyaltyProgramResponse
from ..types.retrieve_loyalty_reward_response import RetrieveLoyaltyRewardResponse
from ..types.search_loyalty_accounts_request_loyalty_account_query import (
    SearchLoyaltyAccountsRequestLoyaltyAccountQuery,
)
from ..types.search_loyalty_accounts_response import SearchLoyaltyAccountsResponse
from ..types.search_loyalty_events_response import SearchLoyaltyEventsResponse
from ..types.search_loyalty_rewards_request_loyalty_reward_query import SearchLoyaltyRewardsRequestLoyaltyRewardQuery
from ..types.search_loyalty_rewards_response import SearchLoyaltyRewardsResponse
from .raw_client import AsyncRawLoyaltyClient, RawLoyaltyClient


OMIT = typing.cast(typing.Any, ...)


class LoyaltyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLoyaltyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLoyaltyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLoyaltyClient
        """
        return self._raw_client

    def create_loyalty_account(
        self,
        *,
        idempotency_key: str,
        loyalty_account: LoyaltyAccount,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateLoyaltyAccountResponse:
        """
        Creates a loyalty account. To create a loyalty account, you must provide the `program_id` and a `mapping` with the `phone_number` of the buyer.

        Parameters
        ----------
        idempotency_key : str
            A unique string that identifies this `CreateLoyaltyAccount` request.
            Keys can be any valid string, but must be unique for every request.

        loyalty_account : LoyaltyAccount

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateLoyaltyAccountResponse
            Success

        Examples
        --------
        from fern import FernApi, LoyaltyAccount

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.loyalty.create_loyalty_account(
            idempotency_key="idempotency_key",
            loyalty_account=LoyaltyAccount(
                program_id="program_id",
            ),
        )
        """
        _response = self._raw_client.create_loyalty_account(
            idempotency_key=idempotency_key, loyalty_account=loyalty_account, request_options=request_options
        )
        return _response.data

    def search_loyalty_accounts(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchLoyaltyAccountsRequestLoyaltyAccountQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchLoyaltyAccountsResponse:
        """
        Searches for loyalty accounts in a loyalty program.

        You can search for a loyalty account using the phone number or customer ID associated with the account. To return all loyalty accounts, specify an empty `query` object or omit it entirely.

        Search results are sorted by `created_at` in ascending order.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to
            this endpoint. Provide this to retrieve the next set of
            results for the original query.

            For more information,
            see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        limit : typing.Optional[int]
            The maximum number of results to include in the response.

        query : typing.Optional[SearchLoyaltyAccountsRequestLoyaltyAccountQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchLoyaltyAccountsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.loyalty.search_loyalty_accounts()
        """
        _response = self._raw_client.search_loyalty_accounts(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    def retrieve_loyalty_account(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveLoyaltyAccountResponse:
        """
        Retrieves a loyalty account.

        Parameters
        ----------
        account_id : str
            The ID of the [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveLoyaltyAccountResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.loyalty.retrieve_loyalty_account(
            account_id="account_id",
        )
        """
        _response = self._raw_client.retrieve_loyalty_account(account_id, request_options=request_options)
        return _response.data

    def accumulate_loyalty_points(
        self,
        account_id: str,
        *,
        accumulate_points: LoyaltyEventAccumulatePoints,
        idempotency_key: str,
        location_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccumulateLoyaltyPointsResponse:
        """
        Adds points to a loyalty account.

        - If you are using the Orders API to manage orders, you only provide the `order_id`.
        The endpoint reads the order to compute points to add to the buyer's account.
        - If you are not using the Orders API to manage orders,
        you first perform a client-side computation to compute the points.
        For spend-based and visit-based programs, you can first call
        [CalculateLoyaltyPoints](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/calculate-loyalty-points) to compute the points
        that you provide to this endpoint.

        __Note:__ The country of the seller's Square account determines whether tax is included in the purchase amount when accruing points for spend-based and visit-based programs.
        For more information, see [Availability of Square Loyalty](https://developer.squareup.com/docs/loyalty-api/overview#loyalty-market-availability).

        Parameters
        ----------
        account_id : str
            The [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) ID to which to add the points.

        accumulate_points : LoyaltyEventAccumulatePoints

        idempotency_key : str
            A unique string that identifies the `AccumulateLoyaltyPoints` request.
            Keys can be any valid string but must be unique for every request.

        location_id : str
            The [location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) where the purchase was made.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccumulateLoyaltyPointsResponse
            Success

        Examples
        --------
        from fern import FernApi, LoyaltyEventAccumulatePoints

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.loyalty.accumulate_loyalty_points(
            account_id="account_id",
            accumulate_points=LoyaltyEventAccumulatePoints(),
            idempotency_key="idempotency_key",
            location_id="location_id",
        )
        """
        _response = self._raw_client.accumulate_loyalty_points(
            account_id,
            accumulate_points=accumulate_points,
            idempotency_key=idempotency_key,
            location_id=location_id,
            request_options=request_options,
        )
        return _response.data

    def adjust_loyalty_points(
        self,
        account_id: str,
        *,
        adjust_points: LoyaltyEventAdjustPoints,
        idempotency_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AdjustLoyaltyPointsResponse:
        """
        Adds points to or subtracts points from a buyer's account.

        Use this endpoint only when you need to manually adjust points. Otherwise, in your application flow, you call
        [AccumulateLoyaltyPoints](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/accumulate-loyalty-points)
        to add points when a buyer pays for the purchase.

        Parameters
        ----------
        account_id : str
            The ID of the [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) in which to adjust the points.

        adjust_points : LoyaltyEventAdjustPoints

        idempotency_key : str
            A unique string that identifies this `AdjustLoyaltyPoints` request.
            Keys can be any valid string, but must be unique for every request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdjustLoyaltyPointsResponse
            Success

        Examples
        --------
        from fern import FernApi, LoyaltyEventAdjustPoints

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.loyalty.adjust_loyalty_points(
            account_id="account_id",
            adjust_points=LoyaltyEventAdjustPoints(
                points=1,
            ),
            idempotency_key="idempotency_key",
        )
        """
        _response = self._raw_client.adjust_loyalty_points(
            account_id, adjust_points=adjust_points, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    def search_loyalty_events(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[LoyaltyEventQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchLoyaltyEventsResponse:
        """
        Searches for loyalty events.

        A Square loyalty program maintains a ledger of events that occur during the lifetime of a
        buyer's loyalty account. Each change in the point balance
        (for example, points earned, points redeemed, and points expired) is
        recorded in the ledger. Using this endpoint, you can search the ledger for events.

        Search results are sorted by `created_at` in descending order.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for your original query.
            For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        limit : typing.Optional[int]
            The maximum number of results to include in the response.
            The last page might contain fewer events.
            The default is 30 events.

        query : typing.Optional[LoyaltyEventQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchLoyaltyEventsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.loyalty.search_loyalty_events()
        """
        _response = self._raw_client.search_loyalty_events(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    def list_loyalty_programs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListLoyaltyProgramsResponse:
        """
        Returns a list of loyalty programs in the seller's account.
        Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).


        Replaced with [RetrieveLoyaltyProgram](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/retrieve-loyalty-program) when used with the keyword `main`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListLoyaltyProgramsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.loyalty.list_loyalty_programs()
        """
        _response = self._raw_client.list_loyalty_programs(request_options=request_options)
        return _response.data

    def retrieve_loyalty_program(
        self, program_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveLoyaltyProgramResponse:
        """
        Retrieves the loyalty program in a seller's account, specified by the program ID or the keyword `main`.

        Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).

        Parameters
        ----------
        program_id : str
            The ID of the loyalty program or the keyword `main`. Either value can be used to retrieve the single loyalty program that belongs to the seller.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveLoyaltyProgramResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.loyalty.retrieve_loyalty_program(
            program_id="program_id",
        )
        """
        _response = self._raw_client.retrieve_loyalty_program(program_id, request_options=request_options)
        return _response.data

    def calculate_loyalty_points(
        self,
        program_id: str,
        *,
        order_id: typing.Optional[str] = OMIT,
        transaction_amount_money: typing.Optional[Money] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CalculateLoyaltyPointsResponse:
        """
        Calculates the points a purchase earns.

        - If you are using the Orders API to manage orders, you provide `order_id` in the request. The
        endpoint calculates the points by reading the order.
        - If you are not using the Orders API to manage orders, you provide the purchase amount in
        the request for the endpoint to calculate the points.

        An application might call this endpoint to show the points that a buyer can earn with the
        specific purchase.

        __Note:__ The country of the seller's Square account determines whether tax is included in the purchase amount when accruing points for spend-based and visit-based programs.
        For more information, see [Availability of Square Loyalty](https://developer.squareup.com/docs/loyalty-api/overview#loyalty-market-availability).

        Parameters
        ----------
        program_id : str
            The [loyalty program](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgram) ID, which defines the rules for accruing points.

        order_id : typing.Optional[str]
            The [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) ID for which to calculate the points.
            Specify this field if your application uses the Orders API to process orders.
            Otherwise, specify the `transaction_amount_money`.

        transaction_amount_money : typing.Optional[Money]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CalculateLoyaltyPointsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.loyalty.calculate_loyalty_points(
            program_id="program_id",
        )
        """
        _response = self._raw_client.calculate_loyalty_points(
            program_id,
            order_id=order_id,
            transaction_amount_money=transaction_amount_money,
            request_options=request_options,
        )
        return _response.data

    def create_loyalty_reward(
        self, *, idempotency_key: str, reward: LoyaltyReward, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateLoyaltyRewardResponse:
        """
        Creates a loyalty reward. In the process, the endpoint does following:

        - Uses the `reward_tier_id` in the request to determine the number of points
        to lock for this reward.
        - If the request includes `order_id`, it adds the reward and related discount to the order.

        After a reward is created, the points are locked and
        not available for the buyer to redeem another reward.

        Parameters
        ----------
        idempotency_key : str
            A unique string that identifies this `CreateLoyaltyReward` request.
            Keys can be any valid string, but must be unique for every request.

        reward : LoyaltyReward

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateLoyaltyRewardResponse
            Success

        Examples
        --------
        from fern import FernApi, LoyaltyReward

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.loyalty.create_loyalty_reward(
            idempotency_key="idempotency_key",
            reward=LoyaltyReward(
                loyalty_account_id="loyalty_account_id",
                reward_tier_id="reward_tier_id",
            ),
        )
        """
        _response = self._raw_client.create_loyalty_reward(
            idempotency_key=idempotency_key, reward=reward, request_options=request_options
        )
        return _response.data

    def search_loyalty_rewards(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchLoyaltyRewardsRequestLoyaltyRewardQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchLoyaltyRewardsResponse:
        """
        Searches for loyalty rewards in a loyalty account.

        In the current implementation, the endpoint supports search by the reward `status`.

        If you know a reward ID, use the
        [RetrieveLoyaltyReward](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/retrieve-loyalty-reward) endpoint.

        Search results are sorted by `updated_at` in descending order.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to
            this endpoint. Provide this to retrieve the next set of
            results for the original query.
            For more information,
            see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        limit : typing.Optional[int]
            The maximum number of results to return in the response.

        query : typing.Optional[SearchLoyaltyRewardsRequestLoyaltyRewardQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchLoyaltyRewardsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.loyalty.search_loyalty_rewards()
        """
        _response = self._raw_client.search_loyalty_rewards(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    def retrieve_loyalty_reward(
        self, reward_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveLoyaltyRewardResponse:
        """
        Retrieves a loyalty reward.

        Parameters
        ----------
        reward_id : str
            The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveLoyaltyRewardResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.loyalty.retrieve_loyalty_reward(
            reward_id="reward_id",
        )
        """
        _response = self._raw_client.retrieve_loyalty_reward(reward_id, request_options=request_options)
        return _response.data

    def delete_loyalty_reward(
        self, reward_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteLoyaltyRewardResponse:
        """
        Deletes a loyalty reward by doing the following:

        - Returns the loyalty points back to the loyalty account.
        - If an order ID was specified when the reward was created
        (see [CreateLoyaltyReward](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/create-loyalty-reward)),
        it updates the order by removing the reward and related
        discounts.

        You cannot delete a reward that has reached the terminal state (REDEEMED).

        Parameters
        ----------
        reward_id : str
            The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteLoyaltyRewardResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.loyalty.delete_loyalty_reward(
            reward_id="reward_id",
        )
        """
        _response = self._raw_client.delete_loyalty_reward(reward_id, request_options=request_options)
        return _response.data

    def redeem_loyalty_reward(
        self,
        reward_id: str,
        *,
        idempotency_key: str,
        location_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RedeemLoyaltyRewardResponse:
        """
        Redeems a loyalty reward.

        The endpoint sets the reward to the `REDEEMED` terminal state.

        If you are using your own order processing system (not using the
        Orders API), you call this endpoint after the buyer paid for the
        purchase.

        After the reward reaches the terminal state, it cannot be deleted.
        In other words, points used for the reward cannot be returned
        to the account.

        Parameters
        ----------
        reward_id : str
            The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to redeem.

        idempotency_key : str
            A unique string that identifies this `RedeemLoyaltyReward` request.
            Keys can be any valid string, but must be unique for every request.

        location_id : str
            The ID of the [location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) where the reward is redeemed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedeemLoyaltyRewardResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.loyalty.redeem_loyalty_reward(
            reward_id="reward_id",
            idempotency_key="idempotency_key",
            location_id="location_id",
        )
        """
        _response = self._raw_client.redeem_loyalty_reward(
            reward_id, idempotency_key=idempotency_key, location_id=location_id, request_options=request_options
        )
        return _response.data


class AsyncLoyaltyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLoyaltyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLoyaltyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLoyaltyClient
        """
        return self._raw_client

    async def create_loyalty_account(
        self,
        *,
        idempotency_key: str,
        loyalty_account: LoyaltyAccount,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateLoyaltyAccountResponse:
        """
        Creates a loyalty account. To create a loyalty account, you must provide the `program_id` and a `mapping` with the `phone_number` of the buyer.

        Parameters
        ----------
        idempotency_key : str
            A unique string that identifies this `CreateLoyaltyAccount` request.
            Keys can be any valid string, but must be unique for every request.

        loyalty_account : LoyaltyAccount

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateLoyaltyAccountResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LoyaltyAccount

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.loyalty.create_loyalty_account(
                idempotency_key="idempotency_key",
                loyalty_account=LoyaltyAccount(
                    program_id="program_id",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_loyalty_account(
            idempotency_key=idempotency_key, loyalty_account=loyalty_account, request_options=request_options
        )
        return _response.data

    async def search_loyalty_accounts(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchLoyaltyAccountsRequestLoyaltyAccountQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchLoyaltyAccountsResponse:
        """
        Searches for loyalty accounts in a loyalty program.

        You can search for a loyalty account using the phone number or customer ID associated with the account. To return all loyalty accounts, specify an empty `query` object or omit it entirely.

        Search results are sorted by `created_at` in ascending order.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to
            this endpoint. Provide this to retrieve the next set of
            results for the original query.

            For more information,
            see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        limit : typing.Optional[int]
            The maximum number of results to include in the response.

        query : typing.Optional[SearchLoyaltyAccountsRequestLoyaltyAccountQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchLoyaltyAccountsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.loyalty.search_loyalty_accounts()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_loyalty_accounts(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    async def retrieve_loyalty_account(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveLoyaltyAccountResponse:
        """
        Retrieves a loyalty account.

        Parameters
        ----------
        account_id : str
            The ID of the [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveLoyaltyAccountResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.loyalty.retrieve_loyalty_account(
                account_id="account_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_loyalty_account(account_id, request_options=request_options)
        return _response.data

    async def accumulate_loyalty_points(
        self,
        account_id: str,
        *,
        accumulate_points: LoyaltyEventAccumulatePoints,
        idempotency_key: str,
        location_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccumulateLoyaltyPointsResponse:
        """
        Adds points to a loyalty account.

        - If you are using the Orders API to manage orders, you only provide the `order_id`.
        The endpoint reads the order to compute points to add to the buyer's account.
        - If you are not using the Orders API to manage orders,
        you first perform a client-side computation to compute the points.
        For spend-based and visit-based programs, you can first call
        [CalculateLoyaltyPoints](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/calculate-loyalty-points) to compute the points
        that you provide to this endpoint.

        __Note:__ The country of the seller's Square account determines whether tax is included in the purchase amount when accruing points for spend-based and visit-based programs.
        For more information, see [Availability of Square Loyalty](https://developer.squareup.com/docs/loyalty-api/overview#loyalty-market-availability).

        Parameters
        ----------
        account_id : str
            The [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) ID to which to add the points.

        accumulate_points : LoyaltyEventAccumulatePoints

        idempotency_key : str
            A unique string that identifies the `AccumulateLoyaltyPoints` request.
            Keys can be any valid string but must be unique for every request.

        location_id : str
            The [location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) where the purchase was made.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccumulateLoyaltyPointsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LoyaltyEventAccumulatePoints

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.loyalty.accumulate_loyalty_points(
                account_id="account_id",
                accumulate_points=LoyaltyEventAccumulatePoints(),
                idempotency_key="idempotency_key",
                location_id="location_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accumulate_loyalty_points(
            account_id,
            accumulate_points=accumulate_points,
            idempotency_key=idempotency_key,
            location_id=location_id,
            request_options=request_options,
        )
        return _response.data

    async def adjust_loyalty_points(
        self,
        account_id: str,
        *,
        adjust_points: LoyaltyEventAdjustPoints,
        idempotency_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AdjustLoyaltyPointsResponse:
        """
        Adds points to or subtracts points from a buyer's account.

        Use this endpoint only when you need to manually adjust points. Otherwise, in your application flow, you call
        [AccumulateLoyaltyPoints](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/accumulate-loyalty-points)
        to add points when a buyer pays for the purchase.

        Parameters
        ----------
        account_id : str
            The ID of the [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) in which to adjust the points.

        adjust_points : LoyaltyEventAdjustPoints

        idempotency_key : str
            A unique string that identifies this `AdjustLoyaltyPoints` request.
            Keys can be any valid string, but must be unique for every request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AdjustLoyaltyPointsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LoyaltyEventAdjustPoints

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.loyalty.adjust_loyalty_points(
                account_id="account_id",
                adjust_points=LoyaltyEventAdjustPoints(
                    points=1,
                ),
                idempotency_key="idempotency_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.adjust_loyalty_points(
            account_id, adjust_points=adjust_points, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    async def search_loyalty_events(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[LoyaltyEventQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchLoyaltyEventsResponse:
        """
        Searches for loyalty events.

        A Square loyalty program maintains a ledger of events that occur during the lifetime of a
        buyer's loyalty account. Each change in the point balance
        (for example, points earned, points redeemed, and points expired) is
        recorded in the ledger. Using this endpoint, you can search the ledger for events.

        Search results are sorted by `created_at` in descending order.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for your original query.
            For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        limit : typing.Optional[int]
            The maximum number of results to include in the response.
            The last page might contain fewer events.
            The default is 30 events.

        query : typing.Optional[LoyaltyEventQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchLoyaltyEventsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.loyalty.search_loyalty_events()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_loyalty_events(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    async def list_loyalty_programs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListLoyaltyProgramsResponse:
        """
        Returns a list of loyalty programs in the seller's account.
        Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).


        Replaced with [RetrieveLoyaltyProgram](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/retrieve-loyalty-program) when used with the keyword `main`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListLoyaltyProgramsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.loyalty.list_loyalty_programs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_loyalty_programs(request_options=request_options)
        return _response.data

    async def retrieve_loyalty_program(
        self, program_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveLoyaltyProgramResponse:
        """
        Retrieves the loyalty program in a seller's account, specified by the program ID or the keyword `main`.

        Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).

        Parameters
        ----------
        program_id : str
            The ID of the loyalty program or the keyword `main`. Either value can be used to retrieve the single loyalty program that belongs to the seller.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveLoyaltyProgramResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.loyalty.retrieve_loyalty_program(
                program_id="program_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_loyalty_program(program_id, request_options=request_options)
        return _response.data

    async def calculate_loyalty_points(
        self,
        program_id: str,
        *,
        order_id: typing.Optional[str] = OMIT,
        transaction_amount_money: typing.Optional[Money] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CalculateLoyaltyPointsResponse:
        """
        Calculates the points a purchase earns.

        - If you are using the Orders API to manage orders, you provide `order_id` in the request. The
        endpoint calculates the points by reading the order.
        - If you are not using the Orders API to manage orders, you provide the purchase amount in
        the request for the endpoint to calculate the points.

        An application might call this endpoint to show the points that a buyer can earn with the
        specific purchase.

        __Note:__ The country of the seller's Square account determines whether tax is included in the purchase amount when accruing points for spend-based and visit-based programs.
        For more information, see [Availability of Square Loyalty](https://developer.squareup.com/docs/loyalty-api/overview#loyalty-market-availability).

        Parameters
        ----------
        program_id : str
            The [loyalty program](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgram) ID, which defines the rules for accruing points.

        order_id : typing.Optional[str]
            The [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) ID for which to calculate the points.
            Specify this field if your application uses the Orders API to process orders.
            Otherwise, specify the `transaction_amount_money`.

        transaction_amount_money : typing.Optional[Money]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CalculateLoyaltyPointsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.loyalty.calculate_loyalty_points(
                program_id="program_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.calculate_loyalty_points(
            program_id,
            order_id=order_id,
            transaction_amount_money=transaction_amount_money,
            request_options=request_options,
        )
        return _response.data

    async def create_loyalty_reward(
        self, *, idempotency_key: str, reward: LoyaltyReward, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateLoyaltyRewardResponse:
        """
        Creates a loyalty reward. In the process, the endpoint does following:

        - Uses the `reward_tier_id` in the request to determine the number of points
        to lock for this reward.
        - If the request includes `order_id`, it adds the reward and related discount to the order.

        After a reward is created, the points are locked and
        not available for the buyer to redeem another reward.

        Parameters
        ----------
        idempotency_key : str
            A unique string that identifies this `CreateLoyaltyReward` request.
            Keys can be any valid string, but must be unique for every request.

        reward : LoyaltyReward

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateLoyaltyRewardResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, LoyaltyReward

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.loyalty.create_loyalty_reward(
                idempotency_key="idempotency_key",
                reward=LoyaltyReward(
                    loyalty_account_id="loyalty_account_id",
                    reward_tier_id="reward_tier_id",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_loyalty_reward(
            idempotency_key=idempotency_key, reward=reward, request_options=request_options
        )
        return _response.data

    async def search_loyalty_rewards(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchLoyaltyRewardsRequestLoyaltyRewardQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchLoyaltyRewardsResponse:
        """
        Searches for loyalty rewards in a loyalty account.

        In the current implementation, the endpoint supports search by the reward `status`.

        If you know a reward ID, use the
        [RetrieveLoyaltyReward](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/retrieve-loyalty-reward) endpoint.

        Search results are sorted by `updated_at` in descending order.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to
            this endpoint. Provide this to retrieve the next set of
            results for the original query.
            For more information,
            see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).

        limit : typing.Optional[int]
            The maximum number of results to return in the response.

        query : typing.Optional[SearchLoyaltyRewardsRequestLoyaltyRewardQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchLoyaltyRewardsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.loyalty.search_loyalty_rewards()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_loyalty_rewards(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    async def retrieve_loyalty_reward(
        self, reward_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveLoyaltyRewardResponse:
        """
        Retrieves a loyalty reward.

        Parameters
        ----------
        reward_id : str
            The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveLoyaltyRewardResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.loyalty.retrieve_loyalty_reward(
                reward_id="reward_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_loyalty_reward(reward_id, request_options=request_options)
        return _response.data

    async def delete_loyalty_reward(
        self, reward_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteLoyaltyRewardResponse:
        """
        Deletes a loyalty reward by doing the following:

        - Returns the loyalty points back to the loyalty account.
        - If an order ID was specified when the reward was created
        (see [CreateLoyaltyReward](https://developer.squareup.com/reference/square_2021-08-18/loyalty-api/create-loyalty-reward)),
        it updates the order by removing the reward and related
        discounts.

        You cannot delete a reward that has reached the terminal state (REDEEMED).

        Parameters
        ----------
        reward_id : str
            The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteLoyaltyRewardResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.loyalty.delete_loyalty_reward(
                reward_id="reward_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_loyalty_reward(reward_id, request_options=request_options)
        return _response.data

    async def redeem_loyalty_reward(
        self,
        reward_id: str,
        *,
        idempotency_key: str,
        location_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RedeemLoyaltyRewardResponse:
        """
        Redeems a loyalty reward.

        The endpoint sets the reward to the `REDEEMED` terminal state.

        If you are using your own order processing system (not using the
        Orders API), you call this endpoint after the buyer paid for the
        purchase.

        After the reward reaches the terminal state, it cannot be deleted.
        In other words, points used for the reward cannot be returned
        to the account.

        Parameters
        ----------
        reward_id : str
            The ID of the [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward) to redeem.

        idempotency_key : str
            A unique string that identifies this `RedeemLoyaltyReward` request.
            Keys can be any valid string, but must be unique for every request.

        location_id : str
            The ID of the [location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) where the reward is redeemed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedeemLoyaltyRewardResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.loyalty.redeem_loyalty_reward(
                reward_id="reward_id",
                idempotency_key="idempotency_key",
                location_id="location_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.redeem_loyalty_reward(
            reward_id, idempotency_key=idempotency_key, location_id=location_id, request_options=request_options
        )
        return _response.data
