

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
from ..errors.conflict_error import ConflictError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from .types.create_system_request_heaters_item import CreateSystemRequestHeatersItem
from .types.create_system_request_thermos_item import CreateSystemRequestThermosItem
from .types.create_system_response import CreateSystemResponse
from .types.delete_system_response import DeleteSystemResponse
from .types.get_system_response import GetSystemResponse
from .types.list_systems_response_item import ListSystemsResponseItem
from .types.update_system_request_heaters_item import UpdateSystemRequestHeatersItem
from .types.update_system_request_thermos_item import UpdateSystemRequestThermosItem
from .types.update_system_response import UpdateSystemResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSystemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_systems(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ListSystemsResponseItem]]:
        """
        List all registered systems with their thermometers and heaters

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ListSystemsResponseItem]]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            "systems/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ListSystemsResponseItem],
                    parse_obj_as(
                        type_=typing.List[ListSystemsResponseItem],
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

    def create_system(
        self,
        *,
        id: str,
        display_name: str,
        thermo_url: str,
        heater_url: str,
        thermos: typing.Sequence[CreateSystemRequestThermosItem],
        heaters: typing.Sequence[CreateSystemRequestHeatersItem],
        location: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateSystemResponse]:
        """
        Register a new system with thermometers and heaters

        Parameters
        ----------
        id : str
            Unique system slug

        display_name : str
            Human-readable name

        thermo_url : str
            Base URL to thermo/ls-api

        heater_url : str
            Base URL to heater-api

        thermos : typing.Sequence[CreateSystemRequestThermosItem]

        heaters : typing.Sequence[CreateSystemRequestHeatersItem]

        location : typing.Optional[str]
            Physical location

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateSystemResponse]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            "systems/",
            method="POST",
            json={
                "id": id,
                "displayName": display_name,
                "location": location,
                "thermoUrl": thermo_url,
                "heaterUrl": heater_url,
                "enabled": enabled,
                "thermos": convert_and_respect_annotation_metadata(
                    object_=thermos, annotation=typing.Sequence[CreateSystemRequestThermosItem], direction="write"
                ),
                "heaters": convert_and_respect_annotation_metadata(
                    object_=heaters, annotation=typing.Sequence[CreateSystemRequestHeatersItem], direction="write"
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
                    CreateSystemResponse,
                    parse_obj_as(
                        type_=CreateSystemResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_system(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetSystemResponse]:
        """
        Get a single system by ID with its thermometers and heaters

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSystemResponse]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"systems/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSystemResponse,
                    parse_obj_as(
                        type_=GetSystemResponse,
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

    def update_system(
        self,
        id: str,
        *,
        display_name: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        thermo_url: typing.Optional[str] = OMIT,
        heater_url: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        thermos: typing.Optional[typing.Sequence[UpdateSystemRequestThermosItem]] = OMIT,
        heaters: typing.Optional[typing.Sequence[UpdateSystemRequestHeatersItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateSystemResponse]:
        """
        Update an existing system. Thermos/heaters are replaced if provided.

        Parameters
        ----------
        id : str

        display_name : typing.Optional[str]

        location : typing.Optional[str]

        thermo_url : typing.Optional[str]

        heater_url : typing.Optional[str]

        enabled : typing.Optional[bool]

        thermos : typing.Optional[typing.Sequence[UpdateSystemRequestThermosItem]]

        heaters : typing.Optional[typing.Sequence[UpdateSystemRequestHeatersItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSystemResponse]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"systems/{encode_path_param(id)}",
            method="PUT",
            json={
                "displayName": display_name,
                "location": location,
                "thermoUrl": thermo_url,
                "heaterUrl": heater_url,
                "enabled": enabled,
                "thermos": convert_and_respect_annotation_metadata(
                    object_=thermos, annotation=typing.Sequence[UpdateSystemRequestThermosItem], direction="write"
                ),
                "heaters": convert_and_respect_annotation_metadata(
                    object_=heaters, annotation=typing.Sequence[UpdateSystemRequestHeatersItem], direction="write"
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
                    UpdateSystemResponse,
                    parse_obj_as(
                        type_=UpdateSystemResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def delete_system(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteSystemResponse]:
        """
        Delete a system and all its associated thermometers and heaters

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteSystemResponse]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"systems/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteSystemResponse,
                    parse_obj_as(
                        type_=DeleteSystemResponse,
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


class AsyncRawSystemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_systems(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ListSystemsResponseItem]]:
        """
        List all registered systems with their thermometers and heaters

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ListSystemsResponseItem]]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "systems/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ListSystemsResponseItem],
                    parse_obj_as(
                        type_=typing.List[ListSystemsResponseItem],
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

    async def create_system(
        self,
        *,
        id: str,
        display_name: str,
        thermo_url: str,
        heater_url: str,
        thermos: typing.Sequence[CreateSystemRequestThermosItem],
        heaters: typing.Sequence[CreateSystemRequestHeatersItem],
        location: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateSystemResponse]:
        """
        Register a new system with thermometers and heaters

        Parameters
        ----------
        id : str
            Unique system slug

        display_name : str
            Human-readable name

        thermo_url : str
            Base URL to thermo/ls-api

        heater_url : str
            Base URL to heater-api

        thermos : typing.Sequence[CreateSystemRequestThermosItem]

        heaters : typing.Sequence[CreateSystemRequestHeatersItem]

        location : typing.Optional[str]
            Physical location

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateSystemResponse]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "systems/",
            method="POST",
            json={
                "id": id,
                "displayName": display_name,
                "location": location,
                "thermoUrl": thermo_url,
                "heaterUrl": heater_url,
                "enabled": enabled,
                "thermos": convert_and_respect_annotation_metadata(
                    object_=thermos, annotation=typing.Sequence[CreateSystemRequestThermosItem], direction="write"
                ),
                "heaters": convert_and_respect_annotation_metadata(
                    object_=heaters, annotation=typing.Sequence[CreateSystemRequestHeatersItem], direction="write"
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
                    CreateSystemResponse,
                    parse_obj_as(
                        type_=CreateSystemResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_system(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetSystemResponse]:
        """
        Get a single system by ID with its thermometers and heaters

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSystemResponse]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"systems/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSystemResponse,
                    parse_obj_as(
                        type_=GetSystemResponse,
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

    async def update_system(
        self,
        id: str,
        *,
        display_name: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        thermo_url: typing.Optional[str] = OMIT,
        heater_url: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        thermos: typing.Optional[typing.Sequence[UpdateSystemRequestThermosItem]] = OMIT,
        heaters: typing.Optional[typing.Sequence[UpdateSystemRequestHeatersItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateSystemResponse]:
        """
        Update an existing system. Thermos/heaters are replaced if provided.

        Parameters
        ----------
        id : str

        display_name : typing.Optional[str]

        location : typing.Optional[str]

        thermo_url : typing.Optional[str]

        heater_url : typing.Optional[str]

        enabled : typing.Optional[bool]

        thermos : typing.Optional[typing.Sequence[UpdateSystemRequestThermosItem]]

        heaters : typing.Optional[typing.Sequence[UpdateSystemRequestHeatersItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSystemResponse]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"systems/{encode_path_param(id)}",
            method="PUT",
            json={
                "displayName": display_name,
                "location": location,
                "thermoUrl": thermo_url,
                "heaterUrl": heater_url,
                "enabled": enabled,
                "thermos": convert_and_respect_annotation_metadata(
                    object_=thermos, annotation=typing.Sequence[UpdateSystemRequestThermosItem], direction="write"
                ),
                "heaters": convert_and_respect_annotation_metadata(
                    object_=heaters, annotation=typing.Sequence[UpdateSystemRequestHeatersItem], direction="write"
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
                    UpdateSystemResponse,
                    parse_obj_as(
                        type_=UpdateSystemResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def delete_system(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteSystemResponse]:
        """
        Delete a system and all its associated thermometers and heaters

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteSystemResponse]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"systems/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteSystemResponse,
                    parse_obj_as(
                        type_=DeleteSystemResponse,
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
