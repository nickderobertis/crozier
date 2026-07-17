

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.create_gift_card_activity_response import CreateGiftCardActivityResponse
from ..types.gift_card_activity import GiftCardActivity
from ..types.list_gift_card_activities_response import ListGiftCardActivitiesResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawGiftCardActivitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[ListGiftCardActivitiesResponse]:
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
        HttpResponse[ListGiftCardActivitiesResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/gift-cards/activities",
            method="GET",
            params={
                "gift_card_id": gift_card_id,
                "type": type,
                "location_id": location_id,
                "begin_time": begin_time,
                "end_time": end_time,
                "limit": limit,
                "cursor": cursor,
                "sort_order": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListGiftCardActivitiesResponse,
                    parse_obj_as(
                        type_=ListGiftCardActivitiesResponse,
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

    def create_gift_card_activity(
        self,
        *,
        gift_card_activity: GiftCardActivity,
        idempotency_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateGiftCardActivityResponse]:
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
        HttpResponse[CreateGiftCardActivityResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/gift-cards/activities",
            method="POST",
            json={
                "gift_card_activity": convert_and_respect_annotation_metadata(
                    object_=gift_card_activity, annotation=GiftCardActivity, direction="write"
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
                    CreateGiftCardActivityResponse,
                    parse_obj_as(
                        type_=CreateGiftCardActivityResponse,
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


class AsyncRawGiftCardActivitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[ListGiftCardActivitiesResponse]:
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
        AsyncHttpResponse[ListGiftCardActivitiesResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/gift-cards/activities",
            method="GET",
            params={
                "gift_card_id": gift_card_id,
                "type": type,
                "location_id": location_id,
                "begin_time": begin_time,
                "end_time": end_time,
                "limit": limit,
                "cursor": cursor,
                "sort_order": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListGiftCardActivitiesResponse,
                    parse_obj_as(
                        type_=ListGiftCardActivitiesResponse,
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

    async def create_gift_card_activity(
        self,
        *,
        gift_card_activity: GiftCardActivity,
        idempotency_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateGiftCardActivityResponse]:
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
        AsyncHttpResponse[CreateGiftCardActivityResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/gift-cards/activities",
            method="POST",
            json={
                "gift_card_activity": convert_and_respect_annotation_metadata(
                    object_=gift_card_activity, annotation=GiftCardActivity, direction="write"
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
                    CreateGiftCardActivityResponse,
                    parse_obj_as(
                        type_=CreateGiftCardActivityResponse,
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
