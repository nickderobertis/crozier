

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
from ..types.create_location_response import CreateLocationResponse
from ..types.list_locations_response import ListLocationsResponse
from ..types.location import Location
from ..types.retrieve_location_response import RetrieveLocationResponse
from ..types.update_location_response import UpdateLocationResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLocationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_locations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListLocationsResponse]:
        """
        Provides information of all locations of a business.

        Many Square API endpoints require a `location_id` parameter.
        The `id` field of the [`Location`](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) objects returned by this
        endpoint correspond to that `location_id` parameter.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListLocationsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/locations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListLocationsResponse,
                    parse_obj_as(
                        type_=ListLocationsResponse,
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

    def create_location(
        self, *, location: typing.Optional[Location] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreateLocationResponse]:
        """
        Creates a location.

        Parameters
        ----------
        location : typing.Optional[Location]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateLocationResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/locations",
            method="POST",
            json={
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=Location, direction="write"
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
                    CreateLocationResponse,
                    parse_obj_as(
                        type_=CreateLocationResponse,
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

    def retrieve_location(
        self, location_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveLocationResponse]:
        """
        Retrieves details of a location. You can specify "main"
        as the location ID to retrieve details of the
        main location.

        Parameters
        ----------
        location_id : str
            The ID of the location to retrieve. If you specify the string "main",
            then the endpoint returns the main location.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveLocationResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveLocationResponse,
                    parse_obj_as(
                        type_=RetrieveLocationResponse,
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

    def update_location(
        self,
        location_id: str,
        *,
        location: typing.Optional[Location] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateLocationResponse]:
        """
        Updates a location.

        Parameters
        ----------
        location_id : str
            The ID of the location to update.

        location : typing.Optional[Location]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateLocationResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}",
            method="PUT",
            json={
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=Location, direction="write"
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
                    UpdateLocationResponse,
                    parse_obj_as(
                        type_=UpdateLocationResponse,
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


class AsyncRawLocationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_locations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListLocationsResponse]:
        """
        Provides information of all locations of a business.

        Many Square API endpoints require a `location_id` parameter.
        The `id` field of the [`Location`](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) objects returned by this
        endpoint correspond to that `location_id` parameter.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListLocationsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/locations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListLocationsResponse,
                    parse_obj_as(
                        type_=ListLocationsResponse,
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

    async def create_location(
        self, *, location: typing.Optional[Location] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreateLocationResponse]:
        """
        Creates a location.

        Parameters
        ----------
        location : typing.Optional[Location]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateLocationResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/locations",
            method="POST",
            json={
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=Location, direction="write"
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
                    CreateLocationResponse,
                    parse_obj_as(
                        type_=CreateLocationResponse,
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

    async def retrieve_location(
        self, location_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveLocationResponse]:
        """
        Retrieves details of a location. You can specify "main"
        as the location ID to retrieve details of the
        main location.

        Parameters
        ----------
        location_id : str
            The ID of the location to retrieve. If you specify the string "main",
            then the endpoint returns the main location.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveLocationResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveLocationResponse,
                    parse_obj_as(
                        type_=RetrieveLocationResponse,
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

    async def update_location(
        self,
        location_id: str,
        *,
        location: typing.Optional[Location] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateLocationResponse]:
        """
        Updates a location.

        Parameters
        ----------
        location_id : str
            The ID of the location to update.

        location : typing.Optional[Location]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateLocationResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}",
            method="PUT",
            json={
                "location": convert_and_respect_annotation_metadata(
                    object_=location, annotation=Location, direction="write"
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
                    UpdateLocationResponse,
                    parse_obj_as(
                        type_=UpdateLocationResponse,
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
