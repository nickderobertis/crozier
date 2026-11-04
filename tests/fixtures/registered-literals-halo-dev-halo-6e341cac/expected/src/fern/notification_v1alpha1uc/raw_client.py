

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
from ..types.notification import Notification
from ..types.notification_list import NotificationList
from ..types.reason_type_notifier_matrix import ReasonTypeNotifierMatrix
from ..types.reason_type_notifier_request import ReasonTypeNotifierRequest
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNotificationV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_user_notification_preferences(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ReasonTypeNotifierMatrix]:
        """
        List notification preferences for the authenticated user.

        Parameters
        ----------
        username : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReasonTypeNotifierMatrix]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.notification.halo.run/v1alpha1/userspaces/{encode_path_param(username)}/notification-preferences",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReasonTypeNotifierMatrix,
                    parse_obj_as(
                        type_=ReasonTypeNotifierMatrix,
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

    def save_user_notification_preferences(
        self,
        username: str,
        *,
        reason_type_notifiers: typing.Sequence[ReasonTypeNotifierRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ReasonTypeNotifierMatrix]:
        """
        Save notification preferences for the authenticated user.

        Parameters
        ----------
        username : str
            User metadata.name

        reason_type_notifiers : typing.Sequence[ReasonTypeNotifierRequest]
            notifier selections grouped by reason type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReasonTypeNotifierMatrix]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.notification.halo.run/v1alpha1/userspaces/{encode_path_param(username)}/notification-preferences",
            method="POST",
            json={
                "reasonTypeNotifiers": convert_and_respect_annotation_metadata(
                    object_=reason_type_notifiers,
                    annotation=typing.Sequence[ReasonTypeNotifierRequest],
                    direction="write",
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReasonTypeNotifierMatrix,
                    parse_obj_as(
                        type_=ReasonTypeNotifierMatrix,
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

    def list_user_notifications(
        self,
        username: str,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NotificationList]:
        """
        List notifications for the authenticated user.

        Parameters
        ----------
        username : str
            User metadata.name

        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotificationList]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.notification.halo.run/v1alpha1/userspaces/{encode_path_param(username)}/notifications",
            method="GET",
            params={
                "page": page,
                "size": size,
                "labelSelector": label_selector,
                "fieldSelector": field_selector,
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationList,
                    parse_obj_as(
                        type_=NotificationList,
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

    def mark_notifications_as_read(
        self, username: str, *, names: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        Mark the specified notifications as read.

        Parameters
        ----------
        username : str
            User metadata.name

        names : typing.Sequence[str]
            notification <code>metadata.name</code> values to mark as read

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.notification.halo.run/v1alpha1/userspaces/{encode_path_param(username)}/notifications/-/mark-specified-as-read",
            method="PUT",
            json={
                "names": names,
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
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def delete_specified_notification(
        self, username: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Notification]:
        """
        Delete the specified notification.

        Parameters
        ----------
        username : str
            User metadata.name

        name : str
            Notification metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Notification]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.notification.halo.run/v1alpha1/userspaces/{encode_path_param(username)}/notifications/{encode_path_param(name)}",
            method="DELETE",
            request_options=request_options,
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

    def mark_notification_as_read(
        self, username: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Notification]:
        """
        Mark the specified notification as read.

        Parameters
        ----------
        username : str
            User metadata.name

        name : str
            Notification metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Notification]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.notification.halo.run/v1alpha1/userspaces/{encode_path_param(username)}/notifications/{encode_path_param(name)}/mark-as-read",
            method="PUT",
            request_options=request_options,
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


class AsyncRawNotificationV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_user_notification_preferences(
        self, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ReasonTypeNotifierMatrix]:
        """
        List notification preferences for the authenticated user.

        Parameters
        ----------
        username : str
            User metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReasonTypeNotifierMatrix]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.notification.halo.run/v1alpha1/userspaces/{encode_path_param(username)}/notification-preferences",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReasonTypeNotifierMatrix,
                    parse_obj_as(
                        type_=ReasonTypeNotifierMatrix,
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

    async def save_user_notification_preferences(
        self,
        username: str,
        *,
        reason_type_notifiers: typing.Sequence[ReasonTypeNotifierRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ReasonTypeNotifierMatrix]:
        """
        Save notification preferences for the authenticated user.

        Parameters
        ----------
        username : str
            User metadata.name

        reason_type_notifiers : typing.Sequence[ReasonTypeNotifierRequest]
            notifier selections grouped by reason type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReasonTypeNotifierMatrix]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.notification.halo.run/v1alpha1/userspaces/{encode_path_param(username)}/notification-preferences",
            method="POST",
            json={
                "reasonTypeNotifiers": convert_and_respect_annotation_metadata(
                    object_=reason_type_notifiers,
                    annotation=typing.Sequence[ReasonTypeNotifierRequest],
                    direction="write",
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReasonTypeNotifierMatrix,
                    parse_obj_as(
                        type_=ReasonTypeNotifierMatrix,
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

    async def list_user_notifications(
        self,
        username: str,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NotificationList]:
        """
        List notifications for the authenticated user.

        Parameters
        ----------
        username : str
            User metadata.name

        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotificationList]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.notification.halo.run/v1alpha1/userspaces/{encode_path_param(username)}/notifications",
            method="GET",
            params={
                "page": page,
                "size": size,
                "labelSelector": label_selector,
                "fieldSelector": field_selector,
                "sort": sort,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationList,
                    parse_obj_as(
                        type_=NotificationList,
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

    async def mark_notifications_as_read(
        self, username: str, *, names: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Mark the specified notifications as read.

        Parameters
        ----------
        username : str
            User metadata.name

        names : typing.Sequence[str]
            notification <code>metadata.name</code> values to mark as read

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.notification.halo.run/v1alpha1/userspaces/{encode_path_param(username)}/notifications/-/mark-specified-as-read",
            method="PUT",
            json={
                "names": names,
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
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def delete_specified_notification(
        self, username: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Notification]:
        """
        Delete the specified notification.

        Parameters
        ----------
        username : str
            User metadata.name

        name : str
            Notification metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Notification]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.notification.halo.run/v1alpha1/userspaces/{encode_path_param(username)}/notifications/{encode_path_param(name)}",
            method="DELETE",
            request_options=request_options,
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

    async def mark_notification_as_read(
        self, username: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Notification]:
        """
        Mark the specified notification as read.

        Parameters
        ----------
        username : str
            User metadata.name

        name : str
            Notification metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Notification]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.notification.halo.run/v1alpha1/userspaces/{encode_path_param(username)}/notifications/{encode_path_param(name)}/mark-as-read",
            method="PUT",
            request_options=request_options,
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
