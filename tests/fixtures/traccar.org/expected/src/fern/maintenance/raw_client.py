

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
from ..types.maintenance import Maintenance
from ..types.maintenance_attributes import MaintenanceAttributes
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMaintenanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def fetch_a_list_of_maintenance(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Maintenance]]:
        """
        Without params, it returns a list of Maintenance the user has access to

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
        HttpResponse[typing.List[Maintenance]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "maintenance",
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
                    typing.List[Maintenance],
                    parse_obj_as(
                        type_=typing.List[Maintenance],
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

    def create_a_maintenance(
        self,
        *,
        attributes: typing.Optional[MaintenanceAttributes] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        period: typing.Optional[float] = OMIT,
        start: typing.Optional[float] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Maintenance]:
        """
        Parameters
        ----------
        attributes : typing.Optional[MaintenanceAttributes]

        id : typing.Optional[int]

        name : typing.Optional[str]

        period : typing.Optional[float]

        start : typing.Optional[float]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Maintenance]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "maintenance",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=MaintenanceAttributes, direction="write"
                ),
                "id": id,
                "name": name,
                "period": period,
                "start": start,
                "type": type,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Maintenance,
                    parse_obj_as(
                        type_=Maintenance,
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

    def update_a_maintenance(
        self,
        id_: int,
        *,
        attributes: typing.Optional[MaintenanceAttributes] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        period: typing.Optional[float] = OMIT,
        start: typing.Optional[float] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Maintenance]:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[MaintenanceAttributes]

        id : typing.Optional[int]

        name : typing.Optional[str]

        period : typing.Optional[float]

        start : typing.Optional[float]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Maintenance]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"maintenance/{encode_path_param(id_)}",
            method="PUT",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=MaintenanceAttributes, direction="write"
                ),
                "id": id,
                "name": name,
                "period": period,
                "start": start,
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
                    Maintenance,
                    parse_obj_as(
                        type_=Maintenance,
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

    def delete_a_maintenance(
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
            f"maintenance/{encode_path_param(id)}",
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


class AsyncRawMaintenanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def fetch_a_list_of_maintenance(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Maintenance]]:
        """
        Without params, it returns a list of Maintenance the user has access to

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
        AsyncHttpResponse[typing.List[Maintenance]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "maintenance",
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
                    typing.List[Maintenance],
                    parse_obj_as(
                        type_=typing.List[Maintenance],
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

    async def create_a_maintenance(
        self,
        *,
        attributes: typing.Optional[MaintenanceAttributes] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        period: typing.Optional[float] = OMIT,
        start: typing.Optional[float] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Maintenance]:
        """
        Parameters
        ----------
        attributes : typing.Optional[MaintenanceAttributes]

        id : typing.Optional[int]

        name : typing.Optional[str]

        period : typing.Optional[float]

        start : typing.Optional[float]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Maintenance]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "maintenance",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=MaintenanceAttributes, direction="write"
                ),
                "id": id,
                "name": name,
                "period": period,
                "start": start,
                "type": type,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Maintenance,
                    parse_obj_as(
                        type_=Maintenance,
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

    async def update_a_maintenance(
        self,
        id_: int,
        *,
        attributes: typing.Optional[MaintenanceAttributes] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        period: typing.Optional[float] = OMIT,
        start: typing.Optional[float] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Maintenance]:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[MaintenanceAttributes]

        id : typing.Optional[int]

        name : typing.Optional[str]

        period : typing.Optional[float]

        start : typing.Optional[float]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Maintenance]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"maintenance/{encode_path_param(id_)}",
            method="PUT",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=MaintenanceAttributes, direction="write"
                ),
                "id": id,
                "name": name,
                "period": period,
                "start": start,
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
                    Maintenance,
                    parse_obj_as(
                        type_=Maintenance,
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

    async def delete_a_maintenance(
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
            f"maintenance/{encode_path_param(id)}",
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
