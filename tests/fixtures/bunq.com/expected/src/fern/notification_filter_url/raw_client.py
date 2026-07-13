

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.notification_filter_url import NotificationFilterUrl
from ..types.notification_filter_url_create import NotificationFilterUrlCreate
from ..types.notification_filter_url_listing import NotificationFilterUrlListing
from ..types.notification_filter_url_monetary_account_create import NotificationFilterUrlMonetaryAccountCreate
from ..types.notification_filter_url_monetary_account_listing import NotificationFilterUrlMonetaryAccountListing


OMIT = typing.cast(typing.Any, ...)


class RawNotificationFilterUrlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_notification_filter_url_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[NotificationFilterUrlMonetaryAccountListing]]:
        """
        Manage the url notification filters for a user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[NotificationFilterUrlMonetaryAccountListing]]
            Manage the url notification filters for a user.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/notification-filter-url",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NotificationFilterUrlMonetaryAccountListing],
                    parse_obj_as(
                        type_=typing.List[NotificationFilterUrlMonetaryAccountListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_notification_filter_url_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilterUrl]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NotificationFilterUrlMonetaryAccountCreate]:
        """
        Manage the url notification filters for a user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        notification_filters : typing.Optional[typing.Sequence[NotificationFilterUrl]]
            The types of notifications that will result in a url notification for this monetary account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotificationFilterUrlMonetaryAccountCreate]
            Manage the url notification filters for a user.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/notification-filter-url",
            method="POST",
            json={
                "notification_filters": convert_and_respect_annotation_metadata(
                    object_=notification_filters, annotation=typing.Sequence[NotificationFilterUrl], direction="write"
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
                    NotificationFilterUrlMonetaryAccountCreate,
                    parse_obj_as(
                        type_=NotificationFilterUrlMonetaryAccountCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_all_notification_filter_url_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[NotificationFilterUrlListing]]:
        """
        Manage the url notification filters for a user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[NotificationFilterUrlListing]]
            Manage the url notification filters for a user.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/notification-filter-url",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NotificationFilterUrlListing],
                    parse_obj_as(
                        type_=typing.List[NotificationFilterUrlListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_notification_filter_url_for_user(
        self,
        user_id: int,
        *,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilterUrl]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NotificationFilterUrlCreate]:
        """
        Manage the url notification filters for a user.

        Parameters
        ----------
        user_id : int


        notification_filters : typing.Optional[typing.Sequence[NotificationFilterUrl]]
            The types of notifications that will result in a url notification for this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotificationFilterUrlCreate]
            Manage the url notification filters for a user.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/notification-filter-url",
            method="POST",
            json={
                "notification_filters": convert_and_respect_annotation_metadata(
                    object_=notification_filters, annotation=typing.Sequence[NotificationFilterUrl], direction="write"
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
                    NotificationFilterUrlCreate,
                    parse_obj_as(
                        type_=NotificationFilterUrlCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawNotificationFilterUrlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_notification_filter_url_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[NotificationFilterUrlMonetaryAccountListing]]:
        """
        Manage the url notification filters for a user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[NotificationFilterUrlMonetaryAccountListing]]
            Manage the url notification filters for a user.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/notification-filter-url",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NotificationFilterUrlMonetaryAccountListing],
                    parse_obj_as(
                        type_=typing.List[NotificationFilterUrlMonetaryAccountListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_notification_filter_url_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        *,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilterUrl]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NotificationFilterUrlMonetaryAccountCreate]:
        """
        Manage the url notification filters for a user.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        notification_filters : typing.Optional[typing.Sequence[NotificationFilterUrl]]
            The types of notifications that will result in a url notification for this monetary account.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotificationFilterUrlMonetaryAccountCreate]
            Manage the url notification filters for a user.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/notification-filter-url",
            method="POST",
            json={
                "notification_filters": convert_and_respect_annotation_metadata(
                    object_=notification_filters, annotation=typing.Sequence[NotificationFilterUrl], direction="write"
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
                    NotificationFilterUrlMonetaryAccountCreate,
                    parse_obj_as(
                        type_=NotificationFilterUrlMonetaryAccountCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_all_notification_filter_url_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[NotificationFilterUrlListing]]:
        """
        Manage the url notification filters for a user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[NotificationFilterUrlListing]]
            Manage the url notification filters for a user.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/notification-filter-url",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NotificationFilterUrlListing],
                    parse_obj_as(
                        type_=typing.List[NotificationFilterUrlListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_notification_filter_url_for_user(
        self,
        user_id: int,
        *,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilterUrl]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NotificationFilterUrlCreate]:
        """
        Manage the url notification filters for a user.

        Parameters
        ----------
        user_id : int


        notification_filters : typing.Optional[typing.Sequence[NotificationFilterUrl]]
            The types of notifications that will result in a url notification for this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotificationFilterUrlCreate]
            Manage the url notification filters for a user.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/notification-filter-url",
            method="POST",
            json={
                "notification_filters": convert_and_respect_annotation_metadata(
                    object_=notification_filters, annotation=typing.Sequence[NotificationFilterUrl], direction="write"
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
                    NotificationFilterUrlCreate,
                    parse_obj_as(
                        type_=NotificationFilterUrlCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
