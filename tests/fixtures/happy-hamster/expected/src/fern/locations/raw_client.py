

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
from ..errors.not_found_error import NotFoundError
from ..types.coordinates import Coordinates
from ..types.location import Location
from ..types.location_id import LocationId
from ..types.location_search_result import LocationSearchResult
from ..types.location_type import LocationType
from pydantic import ValidationError


class RawLocationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_locations_by_coordinates(
        self,
        *,
        coordinates: Coordinates,
        type: typing.Optional[typing.Union[LocationType, typing.Sequence[LocationType]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Location]]:
        """
        Searches for locations in the given range.

        Parameters
        ----------
        coordinates : Coordinates
            Latitude and Longitude

        type : typing.Optional[typing.Union[LocationType, typing.Sequence[LocationType]]]
            Location Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Location]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "locations",
            method="GET",
            params={
                "Coordinates": convert_and_respect_annotation_metadata(
                    object_=coordinates, annotation=Coordinates, direction="write"
                ),
                "type": type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Location],
                    parse_obj_as(
                        type_=typing.List[Location],
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

    def get_location_by_id(
        self, id: LocationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Location]:
        """
        Get details for a specific location.

        Parameters
        ----------
        id : LocationId
            id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Location]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"locations/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Location,
                    parse_obj_as(
                        type_=Location,
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

    def search_locations(
        self,
        query: str,
        *,
        coordinates: typing.Optional[Coordinates] = None,
        type: typing.Optional[typing.Union[LocationType, typing.Sequence[LocationType]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LocationSearchResult]:
        """
        Returns the Coordinate and Locations around the 'Search Query'.

        Parameters
        ----------
        query : str
            Search query

        coordinates : typing.Optional[Coordinates]
            Latitude and Longitude

        type : typing.Optional[typing.Union[LocationType, typing.Sequence[LocationType]]]
            Location Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LocationSearchResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"locations/search/{encode_path_param(query)}",
            method="GET",
            params={
                "Coordinates": convert_and_respect_annotation_metadata(
                    object_=coordinates, annotation=Coordinates, direction="write"
                ),
                "type": type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LocationSearchResult,
                    parse_obj_as(
                        type_=LocationSearchResult,
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


class AsyncRawLocationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_locations_by_coordinates(
        self,
        *,
        coordinates: Coordinates,
        type: typing.Optional[typing.Union[LocationType, typing.Sequence[LocationType]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Location]]:
        """
        Searches for locations in the given range.

        Parameters
        ----------
        coordinates : Coordinates
            Latitude and Longitude

        type : typing.Optional[typing.Union[LocationType, typing.Sequence[LocationType]]]
            Location Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Location]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "locations",
            method="GET",
            params={
                "Coordinates": convert_and_respect_annotation_metadata(
                    object_=coordinates, annotation=Coordinates, direction="write"
                ),
                "type": type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Location],
                    parse_obj_as(
                        type_=typing.List[Location],
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

    async def get_location_by_id(
        self, id: LocationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Location]:
        """
        Get details for a specific location.

        Parameters
        ----------
        id : LocationId
            id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Location]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"locations/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Location,
                    parse_obj_as(
                        type_=Location,
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

    async def search_locations(
        self,
        query: str,
        *,
        coordinates: typing.Optional[Coordinates] = None,
        type: typing.Optional[typing.Union[LocationType, typing.Sequence[LocationType]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LocationSearchResult]:
        """
        Returns the Coordinate and Locations around the 'Search Query'.

        Parameters
        ----------
        query : str
            Search query

        coordinates : typing.Optional[Coordinates]
            Latitude and Longitude

        type : typing.Optional[typing.Union[LocationType, typing.Sequence[LocationType]]]
            Location Type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LocationSearchResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"locations/search/{encode_path_param(query)}",
            method="GET",
            params={
                "Coordinates": convert_and_respect_annotation_metadata(
                    object_=coordinates, annotation=Coordinates, direction="write"
                ),
                "type": type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LocationSearchResult,
                    parse_obj_as(
                        type_=LocationSearchResult,
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
