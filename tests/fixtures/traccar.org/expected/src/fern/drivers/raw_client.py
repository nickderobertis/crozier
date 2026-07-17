

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
from ..types.driver import Driver
from ..types.driver_attributes import DriverAttributes
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDriversClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def fetch_a_list_of_drivers(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Driver]]:
        """
        Without params, it returns a list of Drivers the user has access to

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
        HttpResponse[typing.List[Driver]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "drivers",
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
                    typing.List[Driver],
                    parse_obj_as(
                        type_=typing.List[Driver],
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

    def create_a_driver(
        self,
        *,
        attributes: typing.Optional[DriverAttributes] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        unique_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Driver]:
        """
        Parameters
        ----------
        attributes : typing.Optional[DriverAttributes]

        id : typing.Optional[int]

        name : typing.Optional[str]

        unique_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Driver]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "drivers",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=DriverAttributes, direction="write"
                ),
                "id": id,
                "name": name,
                "uniqueId": unique_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Driver,
                    parse_obj_as(
                        type_=Driver,
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

    def update_a_driver(
        self,
        id_: int,
        *,
        attributes: typing.Optional[DriverAttributes] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        unique_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Driver]:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[DriverAttributes]

        id : typing.Optional[int]

        name : typing.Optional[str]

        unique_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Driver]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"drivers/{encode_path_param(id_)}",
            method="PUT",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=DriverAttributes, direction="write"
                ),
                "id": id,
                "name": name,
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
                    Driver,
                    parse_obj_as(
                        type_=Driver,
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

    def delete_a_driver(
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
            f"drivers/{encode_path_param(id)}",
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


class AsyncRawDriversClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def fetch_a_list_of_drivers(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Driver]]:
        """
        Without params, it returns a list of Drivers the user has access to

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
        AsyncHttpResponse[typing.List[Driver]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "drivers",
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
                    typing.List[Driver],
                    parse_obj_as(
                        type_=typing.List[Driver],
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

    async def create_a_driver(
        self,
        *,
        attributes: typing.Optional[DriverAttributes] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        unique_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Driver]:
        """
        Parameters
        ----------
        attributes : typing.Optional[DriverAttributes]

        id : typing.Optional[int]

        name : typing.Optional[str]

        unique_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Driver]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "drivers",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=DriverAttributes, direction="write"
                ),
                "id": id,
                "name": name,
                "uniqueId": unique_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Driver,
                    parse_obj_as(
                        type_=Driver,
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

    async def update_a_driver(
        self,
        id_: int,
        *,
        attributes: typing.Optional[DriverAttributes] = OMIT,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        unique_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Driver]:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[DriverAttributes]

        id : typing.Optional[int]

        name : typing.Optional[str]

        unique_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Driver]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"drivers/{encode_path_param(id_)}",
            method="PUT",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=DriverAttributes, direction="write"
                ),
                "id": id,
                "name": name,
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
                    Driver,
                    parse_obj_as(
                        type_=Driver,
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

    async def delete_a_driver(
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
            f"drivers/{encode_path_param(id)}",
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
