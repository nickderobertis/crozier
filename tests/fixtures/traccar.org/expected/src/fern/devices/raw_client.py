

import datetime as dt
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
from ..types.device import Device
from ..types.device_attributes import DeviceAttributes
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDevicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def fetch_a_list_of_devices(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        id: typing.Optional[int] = None,
        unique_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Device]]:
        """
        Without any params, returns a list of the user's devices

        Parameters
        ----------
        all_ : typing.Optional[bool]
            Can only be used by admins or managers to fetch all entities

        user_id : typing.Optional[int]
            Standard users can use this only with their own _userId_

        id : typing.Optional[int]
            To fetch one or more devices. Multiple params can be passed like `id=31&id=42`

        unique_id : typing.Optional[str]
            To fetch one or more devices. Multiple params can be passed like `uniqueId=333331&uniqieId=44442`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Device]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "devices",
            method="GET",
            params={
                "all": all_,
                "userId": user_id,
                "id": id,
                "uniqueId": unique_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Device],
                    parse_obj_as(
                        type_=typing.List[Device],
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

    def create_a_device(
        self,
        *,
        attributes: typing.Optional[DeviceAttributes] = OMIT,
        category: typing.Optional[str] = OMIT,
        contact: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        geofence_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_update: typing.Optional[dt.datetime] = OMIT,
        model: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        position_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        unique_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Device]:
        """
        Parameters
        ----------
        attributes : typing.Optional[DeviceAttributes]

        category : typing.Optional[str]

        contact : typing.Optional[str]

        disabled : typing.Optional[bool]

        geofence_ids : typing.Optional[typing.Sequence[int]]

        group_id : typing.Optional[int]

        id : typing.Optional[int]

        last_update : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        model : typing.Optional[str]

        name : typing.Optional[str]

        phone : typing.Optional[str]

        position_id : typing.Optional[int]

        status : typing.Optional[str]

        unique_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Device]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "devices",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=DeviceAttributes, direction="write"
                ),
                "category": category,
                "contact": contact,
                "disabled": disabled,
                "geofenceIds": geofence_ids,
                "groupId": group_id,
                "id": id,
                "lastUpdate": last_update,
                "model": model,
                "name": name,
                "phone": phone,
                "positionId": position_id,
                "status": status,
                "uniqueId": unique_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Device,
                    parse_obj_as(
                        type_=Device,
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

    def update_a_device(
        self,
        id_: int,
        *,
        attributes: typing.Optional[DeviceAttributes] = OMIT,
        category: typing.Optional[str] = OMIT,
        contact: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        geofence_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_update: typing.Optional[dt.datetime] = OMIT,
        model: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        position_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        unique_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Device]:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[DeviceAttributes]

        category : typing.Optional[str]

        contact : typing.Optional[str]

        disabled : typing.Optional[bool]

        geofence_ids : typing.Optional[typing.Sequence[int]]

        group_id : typing.Optional[int]

        id : typing.Optional[int]

        last_update : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        model : typing.Optional[str]

        name : typing.Optional[str]

        phone : typing.Optional[str]

        position_id : typing.Optional[int]

        status : typing.Optional[str]

        unique_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Device]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"devices/{encode_path_param(id_)}",
            method="PUT",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=DeviceAttributes, direction="write"
                ),
                "category": category,
                "contact": contact,
                "disabled": disabled,
                "geofenceIds": geofence_ids,
                "groupId": group_id,
                "id": id,
                "lastUpdate": last_update,
                "model": model,
                "name": name,
                "phone": phone,
                "positionId": position_id,
                "status": status,
                "uniqueId": unique_id,
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
                    Device,
                    parse_obj_as(
                        type_=Device,
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

    def delete_a_device(
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
            f"devices/{encode_path_param(id)}",
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

    def update_total_distance_and_hours_of_the_device(
        self,
        id: int,
        *,
        device_id: typing.Optional[int] = OMIT,
        hours: typing.Optional[float] = OMIT,
        total_distance: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        device_id : typing.Optional[int]

        hours : typing.Optional[float]

        total_distance : typing.Optional[float]
            in meters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"devices/{encode_path_param(id)}/accumulators",
            method="PUT",
            json={
                "deviceId": device_id,
                "hours": hours,
                "totalDistance": total_distance,
            },
            headers={
                "content-type": "application/json",
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


class AsyncRawDevicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def fetch_a_list_of_devices(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        id: typing.Optional[int] = None,
        unique_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Device]]:
        """
        Without any params, returns a list of the user's devices

        Parameters
        ----------
        all_ : typing.Optional[bool]
            Can only be used by admins or managers to fetch all entities

        user_id : typing.Optional[int]
            Standard users can use this only with their own _userId_

        id : typing.Optional[int]
            To fetch one or more devices. Multiple params can be passed like `id=31&id=42`

        unique_id : typing.Optional[str]
            To fetch one or more devices. Multiple params can be passed like `uniqueId=333331&uniqieId=44442`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Device]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "devices",
            method="GET",
            params={
                "all": all_,
                "userId": user_id,
                "id": id,
                "uniqueId": unique_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Device],
                    parse_obj_as(
                        type_=typing.List[Device],
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

    async def create_a_device(
        self,
        *,
        attributes: typing.Optional[DeviceAttributes] = OMIT,
        category: typing.Optional[str] = OMIT,
        contact: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        geofence_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_update: typing.Optional[dt.datetime] = OMIT,
        model: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        position_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        unique_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Device]:
        """
        Parameters
        ----------
        attributes : typing.Optional[DeviceAttributes]

        category : typing.Optional[str]

        contact : typing.Optional[str]

        disabled : typing.Optional[bool]

        geofence_ids : typing.Optional[typing.Sequence[int]]

        group_id : typing.Optional[int]

        id : typing.Optional[int]

        last_update : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        model : typing.Optional[str]

        name : typing.Optional[str]

        phone : typing.Optional[str]

        position_id : typing.Optional[int]

        status : typing.Optional[str]

        unique_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Device]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "devices",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=DeviceAttributes, direction="write"
                ),
                "category": category,
                "contact": contact,
                "disabled": disabled,
                "geofenceIds": geofence_ids,
                "groupId": group_id,
                "id": id,
                "lastUpdate": last_update,
                "model": model,
                "name": name,
                "phone": phone,
                "positionId": position_id,
                "status": status,
                "uniqueId": unique_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Device,
                    parse_obj_as(
                        type_=Device,
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

    async def update_a_device(
        self,
        id_: int,
        *,
        attributes: typing.Optional[DeviceAttributes] = OMIT,
        category: typing.Optional[str] = OMIT,
        contact: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        geofence_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        group_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_update: typing.Optional[dt.datetime] = OMIT,
        model: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        position_id: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        unique_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Device]:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[DeviceAttributes]

        category : typing.Optional[str]

        contact : typing.Optional[str]

        disabled : typing.Optional[bool]

        geofence_ids : typing.Optional[typing.Sequence[int]]

        group_id : typing.Optional[int]

        id : typing.Optional[int]

        last_update : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        model : typing.Optional[str]

        name : typing.Optional[str]

        phone : typing.Optional[str]

        position_id : typing.Optional[int]

        status : typing.Optional[str]

        unique_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Device]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"devices/{encode_path_param(id_)}",
            method="PUT",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=DeviceAttributes, direction="write"
                ),
                "category": category,
                "contact": contact,
                "disabled": disabled,
                "geofenceIds": geofence_ids,
                "groupId": group_id,
                "id": id,
                "lastUpdate": last_update,
                "model": model,
                "name": name,
                "phone": phone,
                "positionId": position_id,
                "status": status,
                "uniqueId": unique_id,
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
                    Device,
                    parse_obj_as(
                        type_=Device,
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

    async def delete_a_device(
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
            f"devices/{encode_path_param(id)}",
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

    async def update_total_distance_and_hours_of_the_device(
        self,
        id: int,
        *,
        device_id: typing.Optional[int] = OMIT,
        hours: typing.Optional[float] = OMIT,
        total_distance: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        device_id : typing.Optional[int]

        hours : typing.Optional[float]

        total_distance : typing.Optional[float]
            in meters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"devices/{encode_path_param(id)}/accumulators",
            method="PUT",
            json={
                "deviceId": device_id,
                "hours": hours,
                "totalDistance": total_distance,
            },
            headers={
                "content-type": "application/json",
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
