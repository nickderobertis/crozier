

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLoyaltyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_loyalty_account(
        self,
        *,
        idempotency_key: str,
        loyalty_account: LoyaltyAccount,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateLoyaltyAccountResponse]:
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
        HttpResponse[CreateLoyaltyAccountResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/loyalty/accounts",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "loyalty_account": convert_and_respect_annotation_metadata(
                    object_=loyalty_account, annotation=LoyaltyAccount, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateLoyaltyAccountResponse,
                    parse_obj_as(
                        type_=CreateLoyaltyAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_loyalty_accounts(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchLoyaltyAccountsRequestLoyaltyAccountQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchLoyaltyAccountsResponse]:
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
        HttpResponse[SearchLoyaltyAccountsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/loyalty/accounts/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=SearchLoyaltyAccountsRequestLoyaltyAccountQuery, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchLoyaltyAccountsResponse,
                    parse_obj_as(
                        type_=SearchLoyaltyAccountsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_loyalty_account(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveLoyaltyAccountResponse]:
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
        HttpResponse[RetrieveLoyaltyAccountResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/loyalty/accounts/{encode_path_param(account_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveLoyaltyAccountResponse,
                    parse_obj_as(
                        type_=RetrieveLoyaltyAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def accumulate_loyalty_points(
        self,
        account_id: str,
        *,
        accumulate_points: LoyaltyEventAccumulatePoints,
        idempotency_key: str,
        location_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AccumulateLoyaltyPointsResponse]:
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
        HttpResponse[AccumulateLoyaltyPointsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/loyalty/accounts/{encode_path_param(account_id)}/accumulate",
            method="POST",
            json={
                "accumulate_points": convert_and_respect_annotation_metadata(
                    object_=accumulate_points, annotation=LoyaltyEventAccumulatePoints, direction="write"
                ),
                "idempotency_key": idempotency_key,
                "location_id": location_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccumulateLoyaltyPointsResponse,
                    parse_obj_as(
                        type_=AccumulateLoyaltyPointsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def adjust_loyalty_points(
        self,
        account_id: str,
        *,
        adjust_points: LoyaltyEventAdjustPoints,
        idempotency_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AdjustLoyaltyPointsResponse]:
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
        HttpResponse[AdjustLoyaltyPointsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/loyalty/accounts/{encode_path_param(account_id)}/adjust",
            method="POST",
            json={
                "adjust_points": convert_and_respect_annotation_metadata(
                    object_=adjust_points, annotation=LoyaltyEventAdjustPoints, direction="write"
                ),
                "idempotency_key": idempotency_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AdjustLoyaltyPointsResponse,
                    parse_obj_as(
                        type_=AdjustLoyaltyPointsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_loyalty_events(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[LoyaltyEventQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchLoyaltyEventsResponse]:
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
        HttpResponse[SearchLoyaltyEventsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/loyalty/events/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=LoyaltyEventQuery, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchLoyaltyEventsResponse,
                    parse_obj_as(
                        type_=SearchLoyaltyEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_loyalty_programs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListLoyaltyProgramsResponse]:
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
        HttpResponse[ListLoyaltyProgramsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/loyalty/programs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListLoyaltyProgramsResponse,
                    parse_obj_as(
                        type_=ListLoyaltyProgramsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_loyalty_program(
        self, program_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveLoyaltyProgramResponse]:
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
        HttpResponse[RetrieveLoyaltyProgramResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/loyalty/programs/{encode_path_param(program_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveLoyaltyProgramResponse,
                    parse_obj_as(
                        type_=RetrieveLoyaltyProgramResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def calculate_loyalty_points(
        self,
        program_id: str,
        *,
        order_id: typing.Optional[str] = OMIT,
        transaction_amount_money: typing.Optional[Money] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CalculateLoyaltyPointsResponse]:
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
        HttpResponse[CalculateLoyaltyPointsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/loyalty/programs/{encode_path_param(program_id)}/calculate",
            method="POST",
            json={
                "order_id": order_id,
                "transaction_amount_money": convert_and_respect_annotation_metadata(
                    object_=transaction_amount_money, annotation=Money, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CalculateLoyaltyPointsResponse,
                    parse_obj_as(
                        type_=CalculateLoyaltyPointsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_loyalty_reward(
        self, *, idempotency_key: str, reward: LoyaltyReward, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreateLoyaltyRewardResponse]:
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
        HttpResponse[CreateLoyaltyRewardResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/loyalty/rewards",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "reward": convert_and_respect_annotation_metadata(
                    object_=reward, annotation=LoyaltyReward, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateLoyaltyRewardResponse,
                    parse_obj_as(
                        type_=CreateLoyaltyRewardResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_loyalty_rewards(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchLoyaltyRewardsRequestLoyaltyRewardQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchLoyaltyRewardsResponse]:
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
        HttpResponse[SearchLoyaltyRewardsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/loyalty/rewards/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=SearchLoyaltyRewardsRequestLoyaltyRewardQuery, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchLoyaltyRewardsResponse,
                    parse_obj_as(
                        type_=SearchLoyaltyRewardsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_loyalty_reward(
        self, reward_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveLoyaltyRewardResponse]:
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
        HttpResponse[RetrieveLoyaltyRewardResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/loyalty/rewards/{encode_path_param(reward_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveLoyaltyRewardResponse,
                    parse_obj_as(
                        type_=RetrieveLoyaltyRewardResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_loyalty_reward(
        self, reward_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteLoyaltyRewardResponse]:
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
        HttpResponse[DeleteLoyaltyRewardResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/loyalty/rewards/{encode_path_param(reward_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteLoyaltyRewardResponse,
                    parse_obj_as(
                        type_=DeleteLoyaltyRewardResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def redeem_loyalty_reward(
        self,
        reward_id: str,
        *,
        idempotency_key: str,
        location_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RedeemLoyaltyRewardResponse]:
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
        HttpResponse[RedeemLoyaltyRewardResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/loyalty/rewards/{encode_path_param(reward_id)}/redeem",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "location_id": location_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RedeemLoyaltyRewardResponse,
                    parse_obj_as(
                        type_=RedeemLoyaltyRewardResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawLoyaltyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_loyalty_account(
        self,
        *,
        idempotency_key: str,
        loyalty_account: LoyaltyAccount,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateLoyaltyAccountResponse]:
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
        AsyncHttpResponse[CreateLoyaltyAccountResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/loyalty/accounts",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "loyalty_account": convert_and_respect_annotation_metadata(
                    object_=loyalty_account, annotation=LoyaltyAccount, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateLoyaltyAccountResponse,
                    parse_obj_as(
                        type_=CreateLoyaltyAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_loyalty_accounts(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchLoyaltyAccountsRequestLoyaltyAccountQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchLoyaltyAccountsResponse]:
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
        AsyncHttpResponse[SearchLoyaltyAccountsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/loyalty/accounts/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=SearchLoyaltyAccountsRequestLoyaltyAccountQuery, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchLoyaltyAccountsResponse,
                    parse_obj_as(
                        type_=SearchLoyaltyAccountsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_loyalty_account(
        self, account_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveLoyaltyAccountResponse]:
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
        AsyncHttpResponse[RetrieveLoyaltyAccountResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/loyalty/accounts/{encode_path_param(account_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveLoyaltyAccountResponse,
                    parse_obj_as(
                        type_=RetrieveLoyaltyAccountResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def accumulate_loyalty_points(
        self,
        account_id: str,
        *,
        accumulate_points: LoyaltyEventAccumulatePoints,
        idempotency_key: str,
        location_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AccumulateLoyaltyPointsResponse]:
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
        AsyncHttpResponse[AccumulateLoyaltyPointsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/loyalty/accounts/{encode_path_param(account_id)}/accumulate",
            method="POST",
            json={
                "accumulate_points": convert_and_respect_annotation_metadata(
                    object_=accumulate_points, annotation=LoyaltyEventAccumulatePoints, direction="write"
                ),
                "idempotency_key": idempotency_key,
                "location_id": location_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccumulateLoyaltyPointsResponse,
                    parse_obj_as(
                        type_=AccumulateLoyaltyPointsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def adjust_loyalty_points(
        self,
        account_id: str,
        *,
        adjust_points: LoyaltyEventAdjustPoints,
        idempotency_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AdjustLoyaltyPointsResponse]:
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
        AsyncHttpResponse[AdjustLoyaltyPointsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/loyalty/accounts/{encode_path_param(account_id)}/adjust",
            method="POST",
            json={
                "adjust_points": convert_and_respect_annotation_metadata(
                    object_=adjust_points, annotation=LoyaltyEventAdjustPoints, direction="write"
                ),
                "idempotency_key": idempotency_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AdjustLoyaltyPointsResponse,
                    parse_obj_as(
                        type_=AdjustLoyaltyPointsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_loyalty_events(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[LoyaltyEventQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchLoyaltyEventsResponse]:
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
        AsyncHttpResponse[SearchLoyaltyEventsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/loyalty/events/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=LoyaltyEventQuery, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchLoyaltyEventsResponse,
                    parse_obj_as(
                        type_=SearchLoyaltyEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_loyalty_programs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListLoyaltyProgramsResponse]:
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
        AsyncHttpResponse[ListLoyaltyProgramsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/loyalty/programs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListLoyaltyProgramsResponse,
                    parse_obj_as(
                        type_=ListLoyaltyProgramsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_loyalty_program(
        self, program_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveLoyaltyProgramResponse]:
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
        AsyncHttpResponse[RetrieveLoyaltyProgramResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/loyalty/programs/{encode_path_param(program_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveLoyaltyProgramResponse,
                    parse_obj_as(
                        type_=RetrieveLoyaltyProgramResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def calculate_loyalty_points(
        self,
        program_id: str,
        *,
        order_id: typing.Optional[str] = OMIT,
        transaction_amount_money: typing.Optional[Money] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CalculateLoyaltyPointsResponse]:
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
        AsyncHttpResponse[CalculateLoyaltyPointsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/loyalty/programs/{encode_path_param(program_id)}/calculate",
            method="POST",
            json={
                "order_id": order_id,
                "transaction_amount_money": convert_and_respect_annotation_metadata(
                    object_=transaction_amount_money, annotation=Money, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CalculateLoyaltyPointsResponse,
                    parse_obj_as(
                        type_=CalculateLoyaltyPointsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_loyalty_reward(
        self, *, idempotency_key: str, reward: LoyaltyReward, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreateLoyaltyRewardResponse]:
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
        AsyncHttpResponse[CreateLoyaltyRewardResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/loyalty/rewards",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "reward": convert_and_respect_annotation_metadata(
                    object_=reward, annotation=LoyaltyReward, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateLoyaltyRewardResponse,
                    parse_obj_as(
                        type_=CreateLoyaltyRewardResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_loyalty_rewards(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchLoyaltyRewardsRequestLoyaltyRewardQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchLoyaltyRewardsResponse]:
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
        AsyncHttpResponse[SearchLoyaltyRewardsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/loyalty/rewards/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=SearchLoyaltyRewardsRequestLoyaltyRewardQuery, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchLoyaltyRewardsResponse,
                    parse_obj_as(
                        type_=SearchLoyaltyRewardsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_loyalty_reward(
        self, reward_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveLoyaltyRewardResponse]:
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
        AsyncHttpResponse[RetrieveLoyaltyRewardResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/loyalty/rewards/{encode_path_param(reward_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveLoyaltyRewardResponse,
                    parse_obj_as(
                        type_=RetrieveLoyaltyRewardResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_loyalty_reward(
        self, reward_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteLoyaltyRewardResponse]:
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
        AsyncHttpResponse[DeleteLoyaltyRewardResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/loyalty/rewards/{encode_path_param(reward_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteLoyaltyRewardResponse,
                    parse_obj_as(
                        type_=DeleteLoyaltyRewardResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def redeem_loyalty_reward(
        self,
        reward_id: str,
        *,
        idempotency_key: str,
        location_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RedeemLoyaltyRewardResponse]:
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
        AsyncHttpResponse[RedeemLoyaltyRewardResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/loyalty/rewards/{encode_path_param(reward_id)}/redeem",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "location_id": location_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RedeemLoyaltyRewardResponse,
                    parse_obj_as(
                        type_=RedeemLoyaltyRewardResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
