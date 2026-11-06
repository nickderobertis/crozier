

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.location import Location
from ..types.location_id import LocationId
from .types.occupancy_report_client_type import OccupancyReportClientType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOccupancyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add_occupancy(
        self,
        id: LocationId,
        *,
        occupancy: float,
        client_type: OccupancyReportClientType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Location]:
        """
        Add or remove current capacity.

        Parameters
        ----------
        id : LocationId
            id of the place

        occupancy : float
            Occupancy

        client_type : OccupancyReportClientType
            Type of the client which reported the occupancy

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Location]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"locations/{encode_path_param(id)}/occupancy",
            method="POST",
            json={
                "occupancy": occupancy,
                "clientType": client_type,
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
                    Location,
                    parse_obj_as(
                        type_=Location,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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


class AsyncRawOccupancyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add_occupancy(
        self,
        id: LocationId,
        *,
        occupancy: float,
        client_type: OccupancyReportClientType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Location]:
        """
        Add or remove current capacity.

        Parameters
        ----------
        id : LocationId
            id of the place

        occupancy : float
            Occupancy

        client_type : OccupancyReportClientType
            Type of the client which reported the occupancy

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Location]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"locations/{encode_path_param(id)}/occupancy",
            method="POST",
            json={
                "occupancy": occupancy,
                "clientType": client_type,
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
                    Location,
                    parse_obj_as(
                        type_=Location,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
