

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from .raw_client import AsyncRawSubscriptionsClient, RawSubscriptionsClient


OMIT = typing.cast(typing.Any, ...)


class SubscriptionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSubscriptionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSubscriptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSubscriptionsClient
        """
        return self._raw_client

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
    ) -> CreateSubscriptionResponse:
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
        CreateSubscriptionResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.subscriptions.create_subscription(
            customer_id="customer_id",
            location_id="location_id",
            plan_id="plan_id",
        )
        """
        _response = self._raw_client.create_subscription(
            customer_id=customer_id,
            location_id=location_id,
            plan_id=plan_id,
            canceled_date=canceled_date,
            card_id=card_id,
            idempotency_key=idempotency_key,
            price_override_money=price_override_money,
            start_date=start_date,
            tax_percentage=tax_percentage,
            timezone=timezone,
            request_options=request_options,
        )
        return _response.data

    def search_subscriptions(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchSubscriptionsQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchSubscriptionsResponse:
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
        SearchSubscriptionsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.subscriptions.search_subscriptions()
        """
        _response = self._raw_client.search_subscriptions(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    def retrieve_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveSubscriptionResponse:
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
        RetrieveSubscriptionResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.subscriptions.retrieve_subscription(
            subscription_id="subscription_id",
        )
        """
        _response = self._raw_client.retrieve_subscription(subscription_id, request_options=request_options)
        return _response.data

    def update_subscription(
        self,
        subscription_id: str,
        *,
        subscription: typing.Optional[Subscription] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSubscriptionResponse:
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
        UpdateSubscriptionResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.subscriptions.update_subscription(
            subscription_id="subscription_id",
        )
        """
        _response = self._raw_client.update_subscription(
            subscription_id, subscription=subscription, request_options=request_options
        )
        return _response.data

    def cancel_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelSubscriptionResponse:
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
        CancelSubscriptionResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.subscriptions.cancel_subscription(
            subscription_id="subscription_id",
        )
        """
        _response = self._raw_client.cancel_subscription(subscription_id, request_options=request_options)
        return _response.data

    def list_subscription_events(
        self,
        subscription_id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSubscriptionEventsResponse:
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
        ListSubscriptionEventsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.subscriptions.list_subscription_events(
            subscription_id="subscription_id",
        )
        """
        _response = self._raw_client.list_subscription_events(
            subscription_id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    def resume_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResumeSubscriptionResponse:
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
        ResumeSubscriptionResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.subscriptions.resume_subscription(
            subscription_id="subscription_id",
        )
        """
        _response = self._raw_client.resume_subscription(subscription_id, request_options=request_options)
        return _response.data


class AsyncSubscriptionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSubscriptionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSubscriptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSubscriptionsClient
        """
        return self._raw_client

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
    ) -> CreateSubscriptionResponse:
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
        CreateSubscriptionResponse
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
            await client.subscriptions.create_subscription(
                customer_id="customer_id",
                location_id="location_id",
                plan_id="plan_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_subscription(
            customer_id=customer_id,
            location_id=location_id,
            plan_id=plan_id,
            canceled_date=canceled_date,
            card_id=card_id,
            idempotency_key=idempotency_key,
            price_override_money=price_override_money,
            start_date=start_date,
            tax_percentage=tax_percentage,
            timezone=timezone,
            request_options=request_options,
        )
        return _response.data

    async def search_subscriptions(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[SearchSubscriptionsQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchSubscriptionsResponse:
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
        SearchSubscriptionsResponse
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
            await client.subscriptions.search_subscriptions()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_subscriptions(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    async def retrieve_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveSubscriptionResponse:
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
        RetrieveSubscriptionResponse
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
            await client.subscriptions.retrieve_subscription(
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_subscription(subscription_id, request_options=request_options)
        return _response.data

    async def update_subscription(
        self,
        subscription_id: str,
        *,
        subscription: typing.Optional[Subscription] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSubscriptionResponse:
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
        UpdateSubscriptionResponse
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
            await client.subscriptions.update_subscription(
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_subscription(
            subscription_id, subscription=subscription, request_options=request_options
        )
        return _response.data

    async def cancel_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelSubscriptionResponse:
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
        CancelSubscriptionResponse
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
            await client.subscriptions.cancel_subscription(
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_subscription(subscription_id, request_options=request_options)
        return _response.data

    async def list_subscription_events(
        self,
        subscription_id: str,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSubscriptionEventsResponse:
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
        ListSubscriptionEventsResponse
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
            await client.subscriptions.list_subscription_events(
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_subscription_events(
            subscription_id, cursor=cursor, limit=limit, request_options=request_options
        )
        return _response.data

    async def resume_subscription(
        self, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ResumeSubscriptionResponse:
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
        ResumeSubscriptionResponse
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
            await client.subscriptions.resume_subscription(
                subscription_id="subscription_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resume_subscription(subscription_id, request_options=request_options)
        return _response.data
