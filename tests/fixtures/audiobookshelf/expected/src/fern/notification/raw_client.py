

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..types.apprise_api_url import AppriseApiUrl
from ..types.body_template import BodyTemplate
from ..types.enabled import Enabled
from ..types.library_id import LibraryId
from ..types.library_id_nullable import LibraryIdNullable
from ..types.max_failed_attempts import MaxFailedAttempts
from ..types.max_notification_queue import MaxNotificationQueue
from ..types.notification_event_name import NotificationEventName
from ..types.notification_id import NotificationId
from ..types.notification_type import NotificationType
from ..types.title_template import TitleTemplate
from ..types.urls import Urls
from .types.create_notification_response import CreateNotificationResponse
from .types.delete_notification_response import DeleteNotificationResponse
from .types.get_notification_event_data_response import GetNotificationEventDataResponse
from .types.get_notifications_response import GetNotificationsResponse
from .types.update_notification_response import UpdateNotificationResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNotificationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_notifications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetNotificationsResponse]:
        """
        Get all Apprise notification events and notification settings for server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetNotificationsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/notifications",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetNotificationsResponse,
                    parse_obj_as(
                        type_=GetNotificationsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def create_notification(
        self,
        *,
        event_name: NotificationEventName,
        urls: Urls,
        title_template: TitleTemplate,
        body_template: BodyTemplate,
        library_id: typing.Optional[LibraryIdNullable] = OMIT,
        enabled: typing.Optional[Enabled] = OMIT,
        type: typing.Optional[NotificationType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateNotificationResponse]:
        """
        Create or update Notification settings.

        Parameters
        ----------
        event_name : NotificationEventName

        urls : Urls

        title_template : TitleTemplate

        body_template : BodyTemplate

        library_id : typing.Optional[LibraryIdNullable]

        enabled : typing.Optional[Enabled]

        type : typing.Optional[NotificationType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateNotificationResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/notifications",
            method="POST",
            json={
                "libraryId": library_id,
                "eventName": event_name,
                "urls": urls,
                "titleTemplate": title_template,
                "bodyTemplate": body_template,
                "enabled": enabled,
                "type": type,
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
                    CreateNotificationResponse,
                    parse_obj_as(
                        type_=CreateNotificationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def configure_notification_settings(
        self,
        *,
        apprise_api_url: typing.Optional[AppriseApiUrl] = OMIT,
        max_failed_attempts: typing.Optional[MaxFailedAttempts] = OMIT,
        max_notification_queue: typing.Optional[MaxNotificationQueue] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Update the URL, max failed attempts, and maximum notifications that can be queued for Apprise.

        Parameters
        ----------
        apprise_api_url : typing.Optional[AppriseApiUrl]

        max_failed_attempts : typing.Optional[MaxFailedAttempts]

        max_notification_queue : typing.Optional[MaxNotificationQueue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Notification endpoint success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/notifications",
            method="PATCH",
            json={
                "appriseApiUrl": apprise_api_url,
                "maxFailedAttempts": max_failed_attempts,
                "maxNotificationQueue": max_notification_queue,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_notification_event_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetNotificationEventDataResponse]:
        """
        Get all Apprise notification event data for the server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetNotificationEventDataResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/notificationdata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetNotificationEventDataResponse,
                    parse_obj_as(
                        type_=GetNotificationEventDataResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def send_default_test_notification(
        self, *, fail: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Send a test notification.

        Parameters
        ----------
        fail : typing.Optional[int]
            Whether to intentionally cause the notification to fail. `0` for false, `1` for true.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Notification endpoint success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/notifications/test",
            method="GET",
            params={
                "fail": fail,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def delete_notification(
        self, id: NotificationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteNotificationResponse]:
        """
        Delete the notification by ID and return the notification settings.

        Parameters
        ----------
        id : NotificationId
            The ID of the notification.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteNotificationResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/notifications/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteNotificationResponse,
                    parse_obj_as(
                        type_=DeleteNotificationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def update_notification(
        self,
        id: NotificationId,
        *,
        library_id: typing.Optional[LibraryId] = OMIT,
        event_name: typing.Optional[NotificationEventName] = OMIT,
        urls: typing.Optional[Urls] = OMIT,
        title_template: typing.Optional[TitleTemplate] = OMIT,
        body_template: typing.Optional[BodyTemplate] = OMIT,
        enabled: typing.Optional[Enabled] = OMIT,
        type: typing.Optional[NotificationType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateNotificationResponse]:
        """
        Update an individual Notification by ID

        Parameters
        ----------
        id : NotificationId
            The ID of the notification.

        library_id : typing.Optional[LibraryId]

        event_name : typing.Optional[NotificationEventName]

        urls : typing.Optional[Urls]

        title_template : typing.Optional[TitleTemplate]

        body_template : typing.Optional[BodyTemplate]

        enabled : typing.Optional[Enabled]

        type : typing.Optional[NotificationType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateNotificationResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/notifications/{encode_path_param(id)}",
            method="PATCH",
            json={
                "libraryId": library_id,
                "eventName": event_name,
                "urls": urls,
                "titleTemplate": title_template,
                "bodyTemplate": body_template,
                "enabled": enabled,
                "type": type,
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
                    UpdateNotificationResponse,
                    parse_obj_as(
                        type_=UpdateNotificationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def send_test_notification(
        self, id: NotificationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Send a test to the given notification by ID.

        Parameters
        ----------
        id : NotificationId
            The ID of the notification.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Notification endpoint success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/notifications/{encode_path_param(id)}/test",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawNotificationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_notifications(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetNotificationsResponse]:
        """
        Get all Apprise notification events and notification settings for server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetNotificationsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/notifications",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetNotificationsResponse,
                    parse_obj_as(
                        type_=GetNotificationsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def create_notification(
        self,
        *,
        event_name: NotificationEventName,
        urls: Urls,
        title_template: TitleTemplate,
        body_template: BodyTemplate,
        library_id: typing.Optional[LibraryIdNullable] = OMIT,
        enabled: typing.Optional[Enabled] = OMIT,
        type: typing.Optional[NotificationType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateNotificationResponse]:
        """
        Create or update Notification settings.

        Parameters
        ----------
        event_name : NotificationEventName

        urls : Urls

        title_template : TitleTemplate

        body_template : BodyTemplate

        library_id : typing.Optional[LibraryIdNullable]

        enabled : typing.Optional[Enabled]

        type : typing.Optional[NotificationType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateNotificationResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/notifications",
            method="POST",
            json={
                "libraryId": library_id,
                "eventName": event_name,
                "urls": urls,
                "titleTemplate": title_template,
                "bodyTemplate": body_template,
                "enabled": enabled,
                "type": type,
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
                    CreateNotificationResponse,
                    parse_obj_as(
                        type_=CreateNotificationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def configure_notification_settings(
        self,
        *,
        apprise_api_url: typing.Optional[AppriseApiUrl] = OMIT,
        max_failed_attempts: typing.Optional[MaxFailedAttempts] = OMIT,
        max_notification_queue: typing.Optional[MaxNotificationQueue] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Update the URL, max failed attempts, and maximum notifications that can be queued for Apprise.

        Parameters
        ----------
        apprise_api_url : typing.Optional[AppriseApiUrl]

        max_failed_attempts : typing.Optional[MaxFailedAttempts]

        max_notification_queue : typing.Optional[MaxNotificationQueue]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Notification endpoint success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/notifications",
            method="PATCH",
            json={
                "appriseApiUrl": apprise_api_url,
                "maxFailedAttempts": max_failed_attempts,
                "maxNotificationQueue": max_notification_queue,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_notification_event_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetNotificationEventDataResponse]:
        """
        Get all Apprise notification event data for the server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetNotificationEventDataResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/notificationdata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetNotificationEventDataResponse,
                    parse_obj_as(
                        type_=GetNotificationEventDataResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def send_default_test_notification(
        self, *, fail: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Send a test notification.

        Parameters
        ----------
        fail : typing.Optional[int]
            Whether to intentionally cause the notification to fail. `0` for false, `1` for true.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Notification endpoint success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/notifications/test",
            method="GET",
            params={
                "fail": fail,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def delete_notification(
        self, id: NotificationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteNotificationResponse]:
        """
        Delete the notification by ID and return the notification settings.

        Parameters
        ----------
        id : NotificationId
            The ID of the notification.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteNotificationResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/notifications/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteNotificationResponse,
                    parse_obj_as(
                        type_=DeleteNotificationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def update_notification(
        self,
        id: NotificationId,
        *,
        library_id: typing.Optional[LibraryId] = OMIT,
        event_name: typing.Optional[NotificationEventName] = OMIT,
        urls: typing.Optional[Urls] = OMIT,
        title_template: typing.Optional[TitleTemplate] = OMIT,
        body_template: typing.Optional[BodyTemplate] = OMIT,
        enabled: typing.Optional[Enabled] = OMIT,
        type: typing.Optional[NotificationType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateNotificationResponse]:
        """
        Update an individual Notification by ID

        Parameters
        ----------
        id : NotificationId
            The ID of the notification.

        library_id : typing.Optional[LibraryId]

        event_name : typing.Optional[NotificationEventName]

        urls : typing.Optional[Urls]

        title_template : typing.Optional[TitleTemplate]

        body_template : typing.Optional[BodyTemplate]

        enabled : typing.Optional[Enabled]

        type : typing.Optional[NotificationType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateNotificationResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/notifications/{encode_path_param(id)}",
            method="PATCH",
            json={
                "libraryId": library_id,
                "eventName": event_name,
                "urls": urls,
                "titleTemplate": title_template,
                "bodyTemplate": body_template,
                "enabled": enabled,
                "type": type,
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
                    UpdateNotificationResponse,
                    parse_obj_as(
                        type_=UpdateNotificationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def send_test_notification(
        self, id: NotificationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Send a test to the given notification by ID.

        Parameters
        ----------
        id : NotificationId
            The ID of the notification.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Notification endpoint success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/notifications/{encode_path_param(id)}/test",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
