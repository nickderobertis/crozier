

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_gift_card_activity_response import CreateGiftCardActivityResponse
from ..types.gift_card_activity import GiftCardActivity
from ..types.list_gift_card_activities_response import ListGiftCardActivitiesResponse
from .raw_client import AsyncRawGiftCardActivitiesClient, RawGiftCardActivitiesClient


OMIT = typing.cast(typing.Any, ...)


class GiftCardActivitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGiftCardActivitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGiftCardActivitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGiftCardActivitiesClient
        """
        return self._raw_client

    def list_gift_card_activities(
        self,
        *,
        gift_card_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListGiftCardActivitiesResponse:
        """
        Lists gift card activities. By default, you get gift card activities for all
        gift cards in the seller's account. You can optionally specify query parameters to
        filter the list. For example, you can get a list of gift card activities for a gift card,
        for all gift cards in a specific region, or for activities within a time window.

        Parameters
        ----------
        gift_card_id : typing.Optional[str]
            If you provide a gift card ID, the endpoint returns activities that belong
            to the specified gift card. Otherwise, the endpoint returns all gift card activities for
            the seller.

        type : typing.Optional[str]
            If you provide a type, the endpoint returns gift card activities of this type.
            Otherwise, the endpoint returns all types of gift card activities.

        location_id : typing.Optional[str]
            If you provide a location ID, the endpoint returns gift card activities for that location.
            Otherwise, the endpoint returns gift card activities for all locations.

        begin_time : typing.Optional[str]
            The timestamp for the beginning of the reporting period, in RFC 3339 format.
            Inclusive. Default: The current time minus one year.

        end_time : typing.Optional[str]
            The timestamp for the end of the reporting period, in RFC 3339 format.
            Inclusive. Default: The current time.

        limit : typing.Optional[int]
            If you provide a limit value, the endpoint returns the specified number
            of results (or less) per page. A maximum value is 100. The default value is 50.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            If you do not provide the cursor, the call returns the first page of the results.

        sort_order : typing.Optional[str]
            The order in which the endpoint returns the activities, based on `created_at`.
            - `ASC` - Oldest to newest.
            - `DESC` - Newest to oldest (default).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListGiftCardActivitiesResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.gift_card_activities.list_gift_card_activities()
        """
        _response = self._raw_client.list_gift_card_activities(
            gift_card_id=gift_card_id,
            type=type,
            location_id=location_id,
            begin_time=begin_time,
            end_time=end_time,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

    def create_gift_card_activity(
        self,
        *,
        gift_card_activity: GiftCardActivity,
        idempotency_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateGiftCardActivityResponse:
        """
        Creates a gift card activity. For more information, see
        [GiftCardActivity](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#giftcardactivity) and
        [Using activated gift cards](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#using-activated-gift-cards).

        Parameters
        ----------
        gift_card_activity : GiftCardActivity

        idempotency_key : str
            A unique string that identifies the `CreateGiftCardActivity` request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateGiftCardActivityResponse
            Success

        Examples
        --------
        from fern import FernApi, GiftCardActivity

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.gift_card_activities.create_gift_card_activity(
            gift_card_activity=GiftCardActivity(
                location_id="location_id",
                type={"key": "value"},
            ),
            idempotency_key="x",
        )
        """
        _response = self._raw_client.create_gift_card_activity(
            gift_card_activity=gift_card_activity, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data


class AsyncGiftCardActivitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGiftCardActivitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGiftCardActivitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGiftCardActivitiesClient
        """
        return self._raw_client

    async def list_gift_card_activities(
        self,
        *,
        gift_card_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        begin_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListGiftCardActivitiesResponse:
        """
        Lists gift card activities. By default, you get gift card activities for all
        gift cards in the seller's account. You can optionally specify query parameters to
        filter the list. For example, you can get a list of gift card activities for a gift card,
        for all gift cards in a specific region, or for activities within a time window.

        Parameters
        ----------
        gift_card_id : typing.Optional[str]
            If you provide a gift card ID, the endpoint returns activities that belong
            to the specified gift card. Otherwise, the endpoint returns all gift card activities for
            the seller.

        type : typing.Optional[str]
            If you provide a type, the endpoint returns gift card activities of this type.
            Otherwise, the endpoint returns all types of gift card activities.

        location_id : typing.Optional[str]
            If you provide a location ID, the endpoint returns gift card activities for that location.
            Otherwise, the endpoint returns gift card activities for all locations.

        begin_time : typing.Optional[str]
            The timestamp for the beginning of the reporting period, in RFC 3339 format.
            Inclusive. Default: The current time minus one year.

        end_time : typing.Optional[str]
            The timestamp for the end of the reporting period, in RFC 3339 format.
            Inclusive. Default: The current time.

        limit : typing.Optional[int]
            If you provide a limit value, the endpoint returns the specified number
            of results (or less) per page. A maximum value is 100. The default value is 50.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            If you do not provide the cursor, the call returns the first page of the results.

        sort_order : typing.Optional[str]
            The order in which the endpoint returns the activities, based on `created_at`.
            - `ASC` - Oldest to newest.
            - `DESC` - Newest to oldest (default).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListGiftCardActivitiesResponse
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
            await client.gift_card_activities.list_gift_card_activities()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_gift_card_activities(
            gift_card_id=gift_card_id,
            type=type,
            location_id=location_id,
            begin_time=begin_time,
            end_time=end_time,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

    async def create_gift_card_activity(
        self,
        *,
        gift_card_activity: GiftCardActivity,
        idempotency_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateGiftCardActivityResponse:
        """
        Creates a gift card activity. For more information, see
        [GiftCardActivity](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#giftcardactivity) and
        [Using activated gift cards](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#using-activated-gift-cards).

        Parameters
        ----------
        gift_card_activity : GiftCardActivity

        idempotency_key : str
            A unique string that identifies the `CreateGiftCardActivity` request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateGiftCardActivityResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GiftCardActivity

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.gift_card_activities.create_gift_card_activity(
                gift_card_activity=GiftCardActivity(
                    location_id="location_id",
                    type={"key": "value"},
                ),
                idempotency_key="x",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_gift_card_activity(
            gift_card_activity=gift_card_activity, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data
