

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
from ..errors.bad_request_error import BadRequestError
from ..types.notification import Notification
from ..types.notification_attributes import NotificationAttributes
from ..types.notification_type import NotificationType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNotificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def fetch_a_list_of_notifications(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Notification]]:
        """
        Without params, it returns a list of Notifications the user has access to

        Parameters
        ----------
        all_ : typing.Optional[bool]
            Can only be used by admins or managers to fetch all entities

        user_id : typing.Optional[int]
            Standard users can use this only with their own _userId_

        device_id : typing.Optional[int]
            Standard users can use this only with _deviceId_s, they have access to

        group_id : typing.Optional[int]
            Standard users can use this only with _groupId_s, they have access to

        refresh : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Notification]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "notifications",
            method="GET",
            params={
                "all": all_,
                "userId": user_id,
                "deviceId": device_id,
                "groupId": group_id,
                "refresh": refresh,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Notification],
                    parse_obj_as(
                        type_=typing.List[Notification],
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

    def create_a_notification(
        self,
        *,
        always: typing.Optional[bool] = OMIT,
        attributes: typing.Optional[NotificationAttributes] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        mail: typing.Optional[bool] = OMIT,
        sms: typing.Optional[bool] = OMIT,
        type: typing.Optional[str] = OMIT,
        web: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Notification]:
        """
        Parameters
        ----------
        always : typing.Optional[bool]

        attributes : typing.Optional[NotificationAttributes]

        calendar_id : typing.Optional[int]

        id : typing.Optional[int]

        mail : typing.Optional[bool]

        sms : typing.Optional[bool]

        type : typing.Optional[str]

        web : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Notification]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "notifications",
            method="POST",
            json={
                "always": always,
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=NotificationAttributes, direction="write"
                ),
                "calendarId": calendar_id,
                "id": id,
                "mail": mail,
                "sms": sms,
                "type": type,
                "web": web,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Notification,
                    parse_obj_as(
                        type_=Notification,
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

    def send_test_notification_to_current_user_via_email_and_sms(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "notifications/test",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def fetch_a_list_of_available_notification_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[NotificationType]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[NotificationType]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "notifications/types",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NotificationType],
                    parse_obj_as(
                        type_=typing.List[NotificationType],
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

    def update_a_notification(
        self,
        id_: int,
        *,
        always: typing.Optional[bool] = OMIT,
        attributes: typing.Optional[NotificationAttributes] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        mail: typing.Optional[bool] = OMIT,
        sms: typing.Optional[bool] = OMIT,
        type: typing.Optional[str] = OMIT,
        web: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Notification]:
        """
        Parameters
        ----------
        id_ : int

        always : typing.Optional[bool]

        attributes : typing.Optional[NotificationAttributes]

        calendar_id : typing.Optional[int]

        id : typing.Optional[int]

        mail : typing.Optional[bool]

        sms : typing.Optional[bool]

        type : typing.Optional[str]

        web : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Notification]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"notifications/{encode_path_param(id_)}",
            method="PUT",
            json={
                "always": always,
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=NotificationAttributes, direction="write"
                ),
                "calendarId": calendar_id,
                "id": id,
                "mail": mail,
                "sms": sms,
                "type": type,
                "web": web,
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
                    Notification,
                    parse_obj_as(
                        type_=Notification,
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

    def delete_a_notification(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"notifications/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    async def fetch_a_list_of_notifications(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Notification]]:
        """
        Without params, it returns a list of Notifications the user has access to

        Parameters
        ----------
        all_ : typing.Optional[bool]
            Can only be used by admins or managers to fetch all entities

        user_id : typing.Optional[int]
            Standard users can use this only with their own _userId_

        device_id : typing.Optional[int]
            Standard users can use this only with _deviceId_s, they have access to

        group_id : typing.Optional[int]
            Standard users can use this only with _groupId_s, they have access to

        refresh : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Notification]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "notifications",
            method="GET",
            params={
                "all": all_,
                "userId": user_id,
                "deviceId": device_id,
                "groupId": group_id,
                "refresh": refresh,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Notification],
                    parse_obj_as(
                        type_=typing.List[Notification],
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

    async def create_a_notification(
        self,
        *,
        always: typing.Optional[bool] = OMIT,
        attributes: typing.Optional[NotificationAttributes] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        mail: typing.Optional[bool] = OMIT,
        sms: typing.Optional[bool] = OMIT,
        type: typing.Optional[str] = OMIT,
        web: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Notification]:
        """
        Parameters
        ----------
        always : typing.Optional[bool]

        attributes : typing.Optional[NotificationAttributes]

        calendar_id : typing.Optional[int]

        id : typing.Optional[int]

        mail : typing.Optional[bool]

        sms : typing.Optional[bool]

        type : typing.Optional[str]

        web : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Notification]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "notifications",
            method="POST",
            json={
                "always": always,
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=NotificationAttributes, direction="write"
                ),
                "calendarId": calendar_id,
                "id": id,
                "mail": mail,
                "sms": sms,
                "type": type,
                "web": web,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Notification,
                    parse_obj_as(
                        type_=Notification,
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

    async def send_test_notification_to_current_user_via_email_and_sms(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "notifications/test",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def fetch_a_list_of_available_notification_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[NotificationType]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[NotificationType]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "notifications/types",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NotificationType],
                    parse_obj_as(
                        type_=typing.List[NotificationType],
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

    async def update_a_notification(
        self,
        id_: int,
        *,
        always: typing.Optional[bool] = OMIT,
        attributes: typing.Optional[NotificationAttributes] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        mail: typing.Optional[bool] = OMIT,
        sms: typing.Optional[bool] = OMIT,
        type: typing.Optional[str] = OMIT,
        web: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Notification]:
        """
        Parameters
        ----------
        id_ : int

        always : typing.Optional[bool]

        attributes : typing.Optional[NotificationAttributes]

        calendar_id : typing.Optional[int]

        id : typing.Optional[int]

        mail : typing.Optional[bool]

        sms : typing.Optional[bool]

        type : typing.Optional[str]

        web : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Notification]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"notifications/{encode_path_param(id_)}",
            method="PUT",
            json={
                "always": always,
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=NotificationAttributes, direction="write"
                ),
                "calendarId": calendar_id,
                "id": id,
                "mail": mail,
                "sms": sms,
                "type": type,
                "web": web,
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
                    Notification,
                    parse_obj_as(
                        type_=Notification,
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

    async def delete_a_notification(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"notifications/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
