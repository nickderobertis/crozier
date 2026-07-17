

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.permission import Permission
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPermissionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def link_an_object_to_another_object(
        self,
        *,
        attribute_id: typing.Optional[int] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        driver_id: typing.Optional[int] = OMIT,
        geofence_id: typing.Optional[int] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        managed_user_id: typing.Optional[int] = OMIT,
        notification_id: typing.Optional[int] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Permission]:
        """
        Parameters
        ----------
        attribute_id : typing.Optional[int]
            Computed Attribute Id, can be second parameter only

        calendar_id : typing.Optional[int]
            Calendar Id, can be second parameter only and only in combination with userId

        device_id : typing.Optional[int]
            Device Id, can be first parameter or second only in combination with userId

        driver_id : typing.Optional[int]
            Driver Id, can be second parameter only

        geofence_id : typing.Optional[int]
            Geofence Id, can be second parameter only

        group_id : typing.Optional[int]
            Group Id, can be first parameter or second only in combination with userId

        managed_user_id : typing.Optional[int]
            User Id, can be second parameter only and only in combination with userId

        notification_id : typing.Optional[int]
            Notification Id, can be second parameter only

        user_id : typing.Optional[int]
            User Id, can be only first parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Permission]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "permissions",
            method="POST",
            json={
                "attributeId": attribute_id,
                "calendarId": calendar_id,
                "deviceId": device_id,
                "driverId": driver_id,
                "geofenceId": geofence_id,
                "groupId": group_id,
                "managedUserId": managed_user_id,
                "notificationId": notification_id,
                "userId": user_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Permission,
                    parse_obj_as(
                        type_=Permission,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def unlink_an_object_from_another_object(
        self,
        *,
        attribute_id: typing.Optional[int] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        driver_id: typing.Optional[int] = OMIT,
        geofence_id: typing.Optional[int] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        managed_user_id: typing.Optional[int] = OMIT,
        notification_id: typing.Optional[int] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        attribute_id : typing.Optional[int]
            Computed Attribute Id, can be second parameter only

        calendar_id : typing.Optional[int]
            Calendar Id, can be second parameter only and only in combination with userId

        device_id : typing.Optional[int]
            Device Id, can be first parameter or second only in combination with userId

        driver_id : typing.Optional[int]
            Driver Id, can be second parameter only

        geofence_id : typing.Optional[int]
            Geofence Id, can be second parameter only

        group_id : typing.Optional[int]
            Group Id, can be first parameter or second only in combination with userId

        managed_user_id : typing.Optional[int]
            User Id, can be second parameter only and only in combination with userId

        notification_id : typing.Optional[int]
            Notification Id, can be second parameter only

        user_id : typing.Optional[int]
            User Id, can be only first parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "permissions",
            method="DELETE",
            json={
                "attributeId": attribute_id,
                "calendarId": calendar_id,
                "deviceId": device_id,
                "driverId": driver_id,
                "geofenceId": geofence_id,
                "groupId": group_id,
                "managedUserId": managed_user_id,
                "notificationId": notification_id,
                "userId": user_id,
            },
            request_options=request_options,
            omit=OMIT,
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


class AsyncRawPermissionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def link_an_object_to_another_object(
        self,
        *,
        attribute_id: typing.Optional[int] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        driver_id: typing.Optional[int] = OMIT,
        geofence_id: typing.Optional[int] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        managed_user_id: typing.Optional[int] = OMIT,
        notification_id: typing.Optional[int] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Permission]:
        """
        Parameters
        ----------
        attribute_id : typing.Optional[int]
            Computed Attribute Id, can be second parameter only

        calendar_id : typing.Optional[int]
            Calendar Id, can be second parameter only and only in combination with userId

        device_id : typing.Optional[int]
            Device Id, can be first parameter or second only in combination with userId

        driver_id : typing.Optional[int]
            Driver Id, can be second parameter only

        geofence_id : typing.Optional[int]
            Geofence Id, can be second parameter only

        group_id : typing.Optional[int]
            Group Id, can be first parameter or second only in combination with userId

        managed_user_id : typing.Optional[int]
            User Id, can be second parameter only and only in combination with userId

        notification_id : typing.Optional[int]
            Notification Id, can be second parameter only

        user_id : typing.Optional[int]
            User Id, can be only first parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Permission]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "permissions",
            method="POST",
            json={
                "attributeId": attribute_id,
                "calendarId": calendar_id,
                "deviceId": device_id,
                "driverId": driver_id,
                "geofenceId": geofence_id,
                "groupId": group_id,
                "managedUserId": managed_user_id,
                "notificationId": notification_id,
                "userId": user_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Permission,
                    parse_obj_as(
                        type_=Permission,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def unlink_an_object_from_another_object(
        self,
        *,
        attribute_id: typing.Optional[int] = OMIT,
        calendar_id: typing.Optional[int] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        driver_id: typing.Optional[int] = OMIT,
        geofence_id: typing.Optional[int] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        managed_user_id: typing.Optional[int] = OMIT,
        notification_id: typing.Optional[int] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        attribute_id : typing.Optional[int]
            Computed Attribute Id, can be second parameter only

        calendar_id : typing.Optional[int]
            Calendar Id, can be second parameter only and only in combination with userId

        device_id : typing.Optional[int]
            Device Id, can be first parameter or second only in combination with userId

        driver_id : typing.Optional[int]
            Driver Id, can be second parameter only

        geofence_id : typing.Optional[int]
            Geofence Id, can be second parameter only

        group_id : typing.Optional[int]
            Group Id, can be first parameter or second only in combination with userId

        managed_user_id : typing.Optional[int]
            User Id, can be second parameter only and only in combination with userId

        notification_id : typing.Optional[int]
            Notification Id, can be second parameter only

        user_id : typing.Optional[int]
            User Id, can be only first parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "permissions",
            method="DELETE",
            json={
                "attributeId": attribute_id,
                "calendarId": calendar_id,
                "deviceId": device_id,
                "driverId": driver_id,
                "geofenceId": geofence_id,
                "groupId": group_id,
                "managedUserId": managed_user_id,
                "notificationId": notification_id,
                "userId": user_id,
            },
            request_options=request_options,
            omit=OMIT,
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
