

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.notification_response import NotificationResponse
from ..types.notifications_response import NotificationsResponse
from pydantic import ValidationError


class RawNotificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_own_notifications(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        unread_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NotificationsResponse]:
        """
        Get all notifications for the authenticated user

        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of results to return (default: 50)

        offset : typing.Optional[int]
            Number of results to skip for pagination (default: 0)

        unread_only : typing.Optional[bool]
            Whether to return only unread notifications (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotificationsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/users/me/notifications",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "unread_only": unread_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationsResponse,
                    parse_obj_as(
                        type_=NotificationsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_own_notification_count(
        self, *, unread_only: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[int]:
        """
        Get the count of notifications for the authenticated user

        Parameters
        ----------
        unread_only : typing.Optional[bool]
            Whether to return only unread notifications (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/users/me/notifications/count",
            method="GET",
            params={
                "unread_only": unread_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def mark_own_notification_as_read(
        self, notification_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NotificationResponse]:
        """
        Mark the authenticated user's own notification as read

        Parameters
        ----------
        notification_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotificationResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/users/me/notifications/{encode_path_param(notification_id)}/dismiss",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationResponse,
                    parse_obj_as(
                        type_=NotificationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_notifications(
        self,
        user_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        unread_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NotificationsResponse]:
        """
        Get all notifications for the specified user

        Parameters
        ----------
        user_id : int
            ID of the user whose notifications will be fetched

        limit : typing.Optional[int]
            Maximum number of results to return (default: 50)

        offset : typing.Optional[int]
            Number of results to skip for pagination (default: 0)

        unread_only : typing.Optional[bool]
            Whether to return only unread notifications (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotificationsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/users/{encode_path_param(user_id)}/notifications",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "unread_only": unread_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationsResponse,
                    parse_obj_as(
                        type_=NotificationsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_notification_count(
        self,
        user_id: int,
        *,
        unread_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        Get the count of notifications for the specified user

        Parameters
        ----------
        user_id : int
            ID of the user whose notification count will be fetched

        unread_only : typing.Optional[bool]
            Whether to return only unread notifications (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/users/{encode_path_param(user_id)}/notifications/count",
            method="GET",
            params={
                "unread_only": unread_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def mark_notification_as_read(
        self, user_id: int, notification_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NotificationResponse]:
        """
        Mark a notification as read

        Parameters
        ----------
        user_id : int
            ID of the user whose notification will be dismissed

        notification_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotificationResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/users/{encode_path_param(user_id)}/notifications/{encode_path_param(notification_id)}/dismiss",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationResponse,
                    parse_obj_as(
                        type_=NotificationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawNotificationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_own_notifications(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        unread_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NotificationsResponse]:
        """
        Get all notifications for the authenticated user

        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of results to return (default: 50)

        offset : typing.Optional[int]
            Number of results to skip for pagination (default: 0)

        unread_only : typing.Optional[bool]
            Whether to return only unread notifications (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotificationsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/users/me/notifications",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "unread_only": unread_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationsResponse,
                    parse_obj_as(
                        type_=NotificationsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_own_notification_count(
        self, *, unread_only: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[int]:
        """
        Get the count of notifications for the authenticated user

        Parameters
        ----------
        unread_only : typing.Optional[bool]
            Whether to return only unread notifications (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/users/me/notifications/count",
            method="GET",
            params={
                "unread_only": unread_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def mark_own_notification_as_read(
        self, notification_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NotificationResponse]:
        """
        Mark the authenticated user's own notification as read

        Parameters
        ----------
        notification_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotificationResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/users/me/notifications/{encode_path_param(notification_id)}/dismiss",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationResponse,
                    parse_obj_as(
                        type_=NotificationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_notifications(
        self,
        user_id: int,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        unread_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NotificationsResponse]:
        """
        Get all notifications for the specified user

        Parameters
        ----------
        user_id : int
            ID of the user whose notifications will be fetched

        limit : typing.Optional[int]
            Maximum number of results to return (default: 50)

        offset : typing.Optional[int]
            Number of results to skip for pagination (default: 0)

        unread_only : typing.Optional[bool]
            Whether to return only unread notifications (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotificationsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/users/{encode_path_param(user_id)}/notifications",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "unread_only": unread_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationsResponse,
                    parse_obj_as(
                        type_=NotificationsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_notification_count(
        self,
        user_id: int,
        *,
        unread_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        Get the count of notifications for the specified user

        Parameters
        ----------
        user_id : int
            ID of the user whose notification count will be fetched

        unread_only : typing.Optional[bool]
            Whether to return only unread notifications (default: false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/users/{encode_path_param(user_id)}/notifications/count",
            method="GET",
            params={
                "unread_only": unread_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def mark_notification_as_read(
        self, user_id: int, notification_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NotificationResponse]:
        """
        Mark a notification as read

        Parameters
        ----------
        user_id : int
            ID of the user whose notification will be dismissed

        notification_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotificationResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/users/{encode_path_param(user_id)}/notifications/{encode_path_param(notification_id)}/dismiss",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationResponse,
                    parse_obj_as(
                        type_=NotificationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
