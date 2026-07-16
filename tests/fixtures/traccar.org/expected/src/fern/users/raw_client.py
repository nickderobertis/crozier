

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
from ..types.user import User
from ..types.user_attributes import UserAttributes
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def fetch_a_list_of_users(
        self, *, user_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[User]]:
        """
        Parameters
        ----------
        user_id : typing.Optional[str]
            Can only be used by admin or manager users

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[User]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={
                "userId": user_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[User],
                    parse_obj_as(
                        type_=typing.List[User],
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

    def create_a_user(
        self,
        *,
        administrator: typing.Optional[bool] = OMIT,
        attributes: typing.Optional[UserAttributes] = OMIT,
        coordinate_format: typing.Optional[str] = OMIT,
        device_limit: typing.Optional[int] = OMIT,
        device_readonly: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        expiration_time: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        latitude: typing.Optional[float] = OMIT,
        limit_commands: typing.Optional[bool] = OMIT,
        longitude: typing.Optional[float] = OMIT,
        map_: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        poi_layer: typing.Optional[str] = OMIT,
        readonly: typing.Optional[bool] = OMIT,
        twelve_hour_format: typing.Optional[bool] = OMIT,
        user_limit: typing.Optional[int] = OMIT,
        zoom: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[User]:
        """
        Parameters
        ----------
        administrator : typing.Optional[bool]

        attributes : typing.Optional[UserAttributes]

        coordinate_format : typing.Optional[str]

        device_limit : typing.Optional[int]

        device_readonly : typing.Optional[bool]

        disabled : typing.Optional[bool]

        email : typing.Optional[str]

        expiration_time : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        id : typing.Optional[int]

        latitude : typing.Optional[float]

        limit_commands : typing.Optional[bool]

        longitude : typing.Optional[float]

        map_ : typing.Optional[str]

        name : typing.Optional[str]

        password : typing.Optional[str]

        phone : typing.Optional[str]

        poi_layer : typing.Optional[str]

        readonly : typing.Optional[bool]

        twelve_hour_format : typing.Optional[bool]

        user_limit : typing.Optional[int]

        zoom : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "users",
            method="POST",
            json={
                "administrator": administrator,
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=UserAttributes, direction="write"
                ),
                "coordinateFormat": coordinate_format,
                "deviceLimit": device_limit,
                "deviceReadonly": device_readonly,
                "disabled": disabled,
                "email": email,
                "expirationTime": expiration_time,
                "id": id,
                "latitude": latitude,
                "limitCommands": limit_commands,
                "longitude": longitude,
                "map": map_,
                "name": name,
                "password": password,
                "phone": phone,
                "poiLayer": poi_layer,
                "readonly": readonly,
                "twelveHourFormat": twelve_hour_format,
                "userLimit": user_limit,
                "zoom": zoom,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    User,
                    parse_obj_as(
                        type_=User,
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

    def update_a_user(
        self,
        id_: int,
        *,
        administrator: typing.Optional[bool] = OMIT,
        attributes: typing.Optional[UserAttributes] = OMIT,
        coordinate_format: typing.Optional[str] = OMIT,
        device_limit: typing.Optional[int] = OMIT,
        device_readonly: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        expiration_time: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        latitude: typing.Optional[float] = OMIT,
        limit_commands: typing.Optional[bool] = OMIT,
        longitude: typing.Optional[float] = OMIT,
        map_: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        poi_layer: typing.Optional[str] = OMIT,
        readonly: typing.Optional[bool] = OMIT,
        twelve_hour_format: typing.Optional[bool] = OMIT,
        user_limit: typing.Optional[int] = OMIT,
        zoom: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[User]:
        """
        Parameters
        ----------
        id_ : int

        administrator : typing.Optional[bool]

        attributes : typing.Optional[UserAttributes]

        coordinate_format : typing.Optional[str]

        device_limit : typing.Optional[int]

        device_readonly : typing.Optional[bool]

        disabled : typing.Optional[bool]

        email : typing.Optional[str]

        expiration_time : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        id : typing.Optional[int]

        latitude : typing.Optional[float]

        limit_commands : typing.Optional[bool]

        longitude : typing.Optional[float]

        map_ : typing.Optional[str]

        name : typing.Optional[str]

        password : typing.Optional[str]

        phone : typing.Optional[str]

        poi_layer : typing.Optional[str]

        readonly : typing.Optional[bool]

        twelve_hour_format : typing.Optional[bool]

        user_limit : typing.Optional[int]

        zoom : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[User]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id_)}",
            method="PUT",
            json={
                "administrator": administrator,
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=UserAttributes, direction="write"
                ),
                "coordinateFormat": coordinate_format,
                "deviceLimit": device_limit,
                "deviceReadonly": device_readonly,
                "disabled": disabled,
                "email": email,
                "expirationTime": expiration_time,
                "id": id,
                "latitude": latitude,
                "limitCommands": limit_commands,
                "longitude": longitude,
                "map": map_,
                "name": name,
                "password": password,
                "phone": phone,
                "poiLayer": poi_layer,
                "readonly": readonly,
                "twelveHourFormat": twelve_hour_format,
                "userLimit": user_limit,
                "zoom": zoom,
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
                    User,
                    parse_obj_as(
                        type_=User,
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

    def delete_a_user(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
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
            f"users/{encode_path_param(id)}",
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


class AsyncRawUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def fetch_a_list_of_users(
        self, *, user_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[User]]:
        """
        Parameters
        ----------
        user_id : typing.Optional[str]
            Can only be used by admin or manager users

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[User]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="GET",
            params={
                "userId": user_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[User],
                    parse_obj_as(
                        type_=typing.List[User],
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

    async def create_a_user(
        self,
        *,
        administrator: typing.Optional[bool] = OMIT,
        attributes: typing.Optional[UserAttributes] = OMIT,
        coordinate_format: typing.Optional[str] = OMIT,
        device_limit: typing.Optional[int] = OMIT,
        device_readonly: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        expiration_time: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        latitude: typing.Optional[float] = OMIT,
        limit_commands: typing.Optional[bool] = OMIT,
        longitude: typing.Optional[float] = OMIT,
        map_: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        poi_layer: typing.Optional[str] = OMIT,
        readonly: typing.Optional[bool] = OMIT,
        twelve_hour_format: typing.Optional[bool] = OMIT,
        user_limit: typing.Optional[int] = OMIT,
        zoom: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[User]:
        """
        Parameters
        ----------
        administrator : typing.Optional[bool]

        attributes : typing.Optional[UserAttributes]

        coordinate_format : typing.Optional[str]

        device_limit : typing.Optional[int]

        device_readonly : typing.Optional[bool]

        disabled : typing.Optional[bool]

        email : typing.Optional[str]

        expiration_time : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        id : typing.Optional[int]

        latitude : typing.Optional[float]

        limit_commands : typing.Optional[bool]

        longitude : typing.Optional[float]

        map_ : typing.Optional[str]

        name : typing.Optional[str]

        password : typing.Optional[str]

        phone : typing.Optional[str]

        poi_layer : typing.Optional[str]

        readonly : typing.Optional[bool]

        twelve_hour_format : typing.Optional[bool]

        user_limit : typing.Optional[int]

        zoom : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users",
            method="POST",
            json={
                "administrator": administrator,
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=UserAttributes, direction="write"
                ),
                "coordinateFormat": coordinate_format,
                "deviceLimit": device_limit,
                "deviceReadonly": device_readonly,
                "disabled": disabled,
                "email": email,
                "expirationTime": expiration_time,
                "id": id,
                "latitude": latitude,
                "limitCommands": limit_commands,
                "longitude": longitude,
                "map": map_,
                "name": name,
                "password": password,
                "phone": phone,
                "poiLayer": poi_layer,
                "readonly": readonly,
                "twelveHourFormat": twelve_hour_format,
                "userLimit": user_limit,
                "zoom": zoom,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    User,
                    parse_obj_as(
                        type_=User,
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

    async def update_a_user(
        self,
        id_: int,
        *,
        administrator: typing.Optional[bool] = OMIT,
        attributes: typing.Optional[UserAttributes] = OMIT,
        coordinate_format: typing.Optional[str] = OMIT,
        device_limit: typing.Optional[int] = OMIT,
        device_readonly: typing.Optional[bool] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        expiration_time: typing.Optional[dt.datetime] = OMIT,
        id: typing.Optional[int] = OMIT,
        latitude: typing.Optional[float] = OMIT,
        limit_commands: typing.Optional[bool] = OMIT,
        longitude: typing.Optional[float] = OMIT,
        map_: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        poi_layer: typing.Optional[str] = OMIT,
        readonly: typing.Optional[bool] = OMIT,
        twelve_hour_format: typing.Optional[bool] = OMIT,
        user_limit: typing.Optional[int] = OMIT,
        zoom: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[User]:
        """
        Parameters
        ----------
        id_ : int

        administrator : typing.Optional[bool]

        attributes : typing.Optional[UserAttributes]

        coordinate_format : typing.Optional[str]

        device_limit : typing.Optional[int]

        device_readonly : typing.Optional[bool]

        disabled : typing.Optional[bool]

        email : typing.Optional[str]

        expiration_time : typing.Optional[dt.datetime]
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        id : typing.Optional[int]

        latitude : typing.Optional[float]

        limit_commands : typing.Optional[bool]

        longitude : typing.Optional[float]

        map_ : typing.Optional[str]

        name : typing.Optional[str]

        password : typing.Optional[str]

        phone : typing.Optional[str]

        poi_layer : typing.Optional[str]

        readonly : typing.Optional[bool]

        twelve_hour_format : typing.Optional[bool]

        user_limit : typing.Optional[int]

        zoom : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[User]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(id_)}",
            method="PUT",
            json={
                "administrator": administrator,
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=UserAttributes, direction="write"
                ),
                "coordinateFormat": coordinate_format,
                "deviceLimit": device_limit,
                "deviceReadonly": device_readonly,
                "disabled": disabled,
                "email": email,
                "expirationTime": expiration_time,
                "id": id,
                "latitude": latitude,
                "limitCommands": limit_commands,
                "longitude": longitude,
                "map": map_,
                "name": name,
                "password": password,
                "phone": phone,
                "poiLayer": poi_layer,
                "readonly": readonly,
                "twelveHourFormat": twelve_hour_format,
                "userLimit": user_limit,
                "zoom": zoom,
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
                    User,
                    parse_obj_as(
                        type_=User,
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

    async def delete_a_user(
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
            f"users/{encode_path_param(id)}",
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
