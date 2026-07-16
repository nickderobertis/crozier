

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
from ..types.cancel_subscription_response import CancelSubscriptionResponse
from ..types.create_subscription_response import CreateSubscriptionResponse
from ..types.list_subscription_events_response import ListSubscriptionEventsResponse
from ..types.money import Money
from ..types.resume_subscription_response import ResumeSubscriptionResponse
from ..types.retrieve_subscription_response import RetrieveSubscriptionResponse
from ..types.search_subscriptions_query import SearchSubscriptionsQuery
from ..types.search_subscriptions_response import SearchSubscriptionsResponse
from ..types.subscription import Subscription
from ..types.update_subscription_response import UpdateSubscriptionResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSubscriptionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_subscription(
        self,
        *,
        customer_id: str,
        location_id: str,
        plan_id: str,
        canceled_date: typing.Optional[str] = OMIT,
        card_id: typing.Optional[str] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        price_override_money: typing.Optional[Money] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        tax_percentage: typing.Optional[str] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateSubscriptionResponse]:
        """
        Creates a subscription for a customer to a subscription plan.

        If you provide a card on file in the request, Square charges the card for
        the subscription. Otherwise, Square bills an invoice to the customer's email
        address. The subscription starts immediately, unless the request includes
        the optional `start_date`. Each individual subscription is associated with a particular location.

        Parameters
        ----------
        customer_id : str
            The ID of the [customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) profile.

        location_id : str
            The ID of the location the subscription is associated with.

        plan_id : str
            The ID of the subscription plan created using the Catalog API.
            For more information, see
            [Set Up and Manage a Subscription Plan](https://developer.squareup.com/docs/subscriptions-api/setup-plan) and
            [Subscriptions Walkthrough](https://developer.squareup.com/docs/subscriptions-api/walkthrough).

        canceled_date : typing.Optional[str]
            The date when the subscription should be canceled, in
            YYYY-MM-DD format (for example, 2025-02-29). This overrides the plan configuration
            if it comes before the date the subscription would otherwise end.

        card_id : typing.Optional[str]
            The ID of the [customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) [card](https://developer.squareup.com/reference/square_2021-08-18/objects/Card) to charge.
            If not specified, Square sends an invoice via email. For an example to
            create a customer and add a card on file, see [Subscriptions Walkthrough](https://developer.squareup.com/docs/subscriptions-api/walkthrough).

        idempotency_key : typing.Optional[str]
            A unique string that identifies this `CreateSubscription` request.
            If you do not provide a unique string (or provide an empty string as the value),
            the endpoint treats each request as independent.

            For more information, see [Idempotency keys](https://developer.squareup.com/docs/working-with-apis/idempotency).

        price_override_money : typing.Optional[Money]

        start_date : typing.Optional[str]
            The start date of the subscription, in YYYY-MM-DD format. For example,
            2013-01-15. If the start date is left empty, the subscription begins
            immediately.

        tax_percentage : typing.Optional[str]
            The tax to add when billing the subscription.
            The percentage is expressed in decimal form, using a `'.'` as the decimal
            separator and without a `'%'` sign. For example, a value of 7.5
            corresponds to 7.5%.

        timezone : typing.Optional[str]
            The timezone that is used in date calculations for the subscription. If unset, defaults to
            the location timezone. If a timezone is not configured for the location, defaults to "America/New_York".
            Format: the IANA Timezone Database identifier for the location timezone. For
            a list of time zones, see [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateSubscriptionResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/subscriptions",
            method="POST",
            json={
                "canceled_date": canceled_date,
                "card_id": card_id,
                "customer_id": customer_id,
                "idempotency_key": idempotency_key,
                "location_id": location_id,
                "plan_id": plan_id,
                "price_override_money": convert_and_respect_annotation_metadata(
                    object_=price_override_money, annotation=Money, direction="write"
                ),
                "start_date": start_date,
                "tax_percentage": tax_percentage,
                "timezone": timezone,
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
                    CreateSubscriptionResponse,
                    parse_obj_as(
                        type_=CreateSubscriptionResponse,
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

    def search_subscriptions(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchSubscriptionsQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchSubscriptionsResponse]:
        """
        Searches for subscriptions.
        Results are ordered chronologically by subscription creation date. If
        the request specifies more than one location ID,
        the endpoint orders the result
        by location ID, and then by creation date within each location. If no locations are given
        in the query, all locations are searched.

        You can also optionally specify `customer_ids` to search by customer.
        If left unset, all customers
        associated with the specified locations are returned.
        If the request specifies customer IDs, the endpoint orders results
        first by location, within location by customer ID, and within
        customer by subscription creation date.

        For more information, see
        [Retrieve subscriptions](https://developer.squareup.com/docs/subscriptions-api/overview#retrieve-subscriptions).

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The upper limit on the number of subscriptions to return
            in the response.

            Default: `200`

        query : typing.Optional[SearchSubscriptionsQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchSubscriptionsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/subscriptions/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=SearchSubscriptionsQuery, direction="write"
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
                    SearchSubscriptionsResponse,
                    parse_obj_as(
                        type_=SearchSubscriptionsResponse,
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

    def retrieve_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveSubscriptionResponse]:
        """
        Retrieves a subscription.

        Parameters
        ----------
        subscription_id : str
            The ID of the subscription to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveSubscriptionResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/subscriptions/{encode_path_param(subscription_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveSubscriptionResponse,
                    parse_obj_as(
                        type_=RetrieveSubscriptionResponse,
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

    def update_subscription(
        self,
        subscription_id: str,
        *,
        subscription: typing.Optional[Subscription] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateSubscriptionResponse]:
        """
        Updates a subscription. You can set, modify, and clear the
        `subscription` field values.

        Parameters
        ----------
        subscription_id : str
            The ID for the subscription to update.

        subscription : typing.Optional[Subscription]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSubscriptionResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/subscriptions/{encode_path_param(subscription_id)}",
            method="PUT",
            json={
                "subscription": convert_and_respect_annotation_metadata(
                    object_=subscription, annotation=Subscription, direction="write"
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
                    UpdateSubscriptionResponse,
                    parse_obj_as(
                        type_=UpdateSubscriptionResponse,
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

    def cancel_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CancelSubscriptionResponse]:
        """
        Sets the `canceled_date` field to the end of the active billing period.
        After this date, the status changes from ACTIVE to CANCELED.

        Parameters
        ----------
        subscription_id : str
            The ID of the subscription to cancel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CancelSubscriptionResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/subscriptions/{encode_path_param(subscription_id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelSubscriptionResponse,
                    parse_obj_as(
                        type_=CancelSubscriptionResponse,
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

    def list_subscription_events(
        self,
        subscription_id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListSubscriptionEventsResponse]:
        """
        Lists all events for a specific subscription.
        In the current implementation, only `START_SUBSCRIPTION` and `STOP_SUBSCRIPTION` (when the subscription was canceled) events are returned.

        Parameters
        ----------
        subscription_id : str
            The ID of the subscription to retrieve the events for.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The upper limit on the number of subscription events to return
            in the response.

            Default: `200`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListSubscriptionEventsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/subscriptions/{encode_path_param(subscription_id)}/events",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListSubscriptionEventsResponse,
                    parse_obj_as(
                        type_=ListSubscriptionEventsResponse,
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

    def resume_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResumeSubscriptionResponse]:
        """
        Resumes a deactivated subscription.

        Parameters
        ----------
        subscription_id : str
            The ID of the subscription to resume.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResumeSubscriptionResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/subscriptions/{encode_path_param(subscription_id)}/resume",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResumeSubscriptionResponse,
                    parse_obj_as(
                        type_=ResumeSubscriptionResponse,
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


class AsyncRawSubscriptionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_subscription(
        self,
        *,
        customer_id: str,
        location_id: str,
        plan_id: str,
        canceled_date: typing.Optional[str] = OMIT,
        card_id: typing.Optional[str] = OMIT,
        idempotency_key: typing.Optional[str] = OMIT,
        price_override_money: typing.Optional[Money] = OMIT,
        start_date: typing.Optional[str] = OMIT,
        tax_percentage: typing.Optional[str] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateSubscriptionResponse]:
        """
        Creates a subscription for a customer to a subscription plan.

        If you provide a card on file in the request, Square charges the card for
        the subscription. Otherwise, Square bills an invoice to the customer's email
        address. The subscription starts immediately, unless the request includes
        the optional `start_date`. Each individual subscription is associated with a particular location.

        Parameters
        ----------
        customer_id : str
            The ID of the [customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) profile.

        location_id : str
            The ID of the location the subscription is associated with.

        plan_id : str
            The ID of the subscription plan created using the Catalog API.
            For more information, see
            [Set Up and Manage a Subscription Plan](https://developer.squareup.com/docs/subscriptions-api/setup-plan) and
            [Subscriptions Walkthrough](https://developer.squareup.com/docs/subscriptions-api/walkthrough).

        canceled_date : typing.Optional[str]
            The date when the subscription should be canceled, in
            YYYY-MM-DD format (for example, 2025-02-29). This overrides the plan configuration
            if it comes before the date the subscription would otherwise end.

        card_id : typing.Optional[str]
            The ID of the [customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) [card](https://developer.squareup.com/reference/square_2021-08-18/objects/Card) to charge.
            If not specified, Square sends an invoice via email. For an example to
            create a customer and add a card on file, see [Subscriptions Walkthrough](https://developer.squareup.com/docs/subscriptions-api/walkthrough).

        idempotency_key : typing.Optional[str]
            A unique string that identifies this `CreateSubscription` request.
            If you do not provide a unique string (or provide an empty string as the value),
            the endpoint treats each request as independent.

            For more information, see [Idempotency keys](https://developer.squareup.com/docs/working-with-apis/idempotency).

        price_override_money : typing.Optional[Money]

        start_date : typing.Optional[str]
            The start date of the subscription, in YYYY-MM-DD format. For example,
            2013-01-15. If the start date is left empty, the subscription begins
            immediately.

        tax_percentage : typing.Optional[str]
            The tax to add when billing the subscription.
            The percentage is expressed in decimal form, using a `'.'` as the decimal
            separator and without a `'%'` sign. For example, a value of 7.5
            corresponds to 7.5%.

        timezone : typing.Optional[str]
            The timezone that is used in date calculations for the subscription. If unset, defaults to
            the location timezone. If a timezone is not configured for the location, defaults to "America/New_York".
            Format: the IANA Timezone Database identifier for the location timezone. For
            a list of time zones, see [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateSubscriptionResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/subscriptions",
            method="POST",
            json={
                "canceled_date": canceled_date,
                "card_id": card_id,
                "customer_id": customer_id,
                "idempotency_key": idempotency_key,
                "location_id": location_id,
                "plan_id": plan_id,
                "price_override_money": convert_and_respect_annotation_metadata(
                    object_=price_override_money, annotation=Money, direction="write"
                ),
                "start_date": start_date,
                "tax_percentage": tax_percentage,
                "timezone": timezone,
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
                    CreateSubscriptionResponse,
                    parse_obj_as(
                        type_=CreateSubscriptionResponse,
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

    async def search_subscriptions(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchSubscriptionsQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchSubscriptionsResponse]:
        """
        Searches for subscriptions.
        Results are ordered chronologically by subscription creation date. If
        the request specifies more than one location ID,
        the endpoint orders the result
        by location ID, and then by creation date within each location. If no locations are given
        in the query, all locations are searched.

        You can also optionally specify `customer_ids` to search by customer.
        If left unset, all customers
        associated with the specified locations are returned.
        If the request specifies customer IDs, the endpoint orders results
        first by location, within location by customer ID, and within
        customer by subscription creation date.

        For more information, see
        [Retrieve subscriptions](https://developer.squareup.com/docs/subscriptions-api/overview#retrieve-subscriptions).

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The upper limit on the number of subscriptions to return
            in the response.

            Default: `200`

        query : typing.Optional[SearchSubscriptionsQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchSubscriptionsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/subscriptions/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=SearchSubscriptionsQuery, direction="write"
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
                    SearchSubscriptionsResponse,
                    parse_obj_as(
                        type_=SearchSubscriptionsResponse,
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

    async def retrieve_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveSubscriptionResponse]:
        """
        Retrieves a subscription.

        Parameters
        ----------
        subscription_id : str
            The ID of the subscription to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveSubscriptionResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/subscriptions/{encode_path_param(subscription_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveSubscriptionResponse,
                    parse_obj_as(
                        type_=RetrieveSubscriptionResponse,
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

    async def update_subscription(
        self,
        subscription_id: str,
        *,
        subscription: typing.Optional[Subscription] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateSubscriptionResponse]:
        """
        Updates a subscription. You can set, modify, and clear the
        `subscription` field values.

        Parameters
        ----------
        subscription_id : str
            The ID for the subscription to update.

        subscription : typing.Optional[Subscription]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSubscriptionResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/subscriptions/{encode_path_param(subscription_id)}",
            method="PUT",
            json={
                "subscription": convert_and_respect_annotation_metadata(
                    object_=subscription, annotation=Subscription, direction="write"
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
                    UpdateSubscriptionResponse,
                    parse_obj_as(
                        type_=UpdateSubscriptionResponse,
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

    async def cancel_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CancelSubscriptionResponse]:
        """
        Sets the `canceled_date` field to the end of the active billing period.
        After this date, the status changes from ACTIVE to CANCELED.

        Parameters
        ----------
        subscription_id : str
            The ID of the subscription to cancel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CancelSubscriptionResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/subscriptions/{encode_path_param(subscription_id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelSubscriptionResponse,
                    parse_obj_as(
                        type_=CancelSubscriptionResponse,
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

    async def list_subscription_events(
        self,
        subscription_id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListSubscriptionEventsResponse]:
        """
        Lists all events for a specific subscription.
        In the current implementation, only `START_SUBSCRIPTION` and `STOP_SUBSCRIPTION` (when the subscription was canceled) events are returned.

        Parameters
        ----------
        subscription_id : str
            The ID of the subscription to retrieve the events for.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for the original query.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The upper limit on the number of subscription events to return
            in the response.

            Default: `200`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListSubscriptionEventsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/subscriptions/{encode_path_param(subscription_id)}/events",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListSubscriptionEventsResponse,
                    parse_obj_as(
                        type_=ListSubscriptionEventsResponse,
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

    async def resume_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResumeSubscriptionResponse]:
        """
        Resumes a deactivated subscription.

        Parameters
        ----------
        subscription_id : str
            The ID of the subscription to resume.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResumeSubscriptionResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/subscriptions/{encode_path_param(subscription_id)}/resume",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResumeSubscriptionResponse,
                    parse_obj_as(
                        type_=ResumeSubscriptionResponse,
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
