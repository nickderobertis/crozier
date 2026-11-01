

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.abstract_bin_grid import AbstractBinGrid
from ..types.convert_bin_grid_response import ConvertBinGridResponse
from ..types.convert_geo_json_response import ConvertGeoJsonResponse
from ..types.convert_points_response import ConvertPointsResponse
from ..types.convert_trajectory_response import ConvertTrajectoryResponse
from ..types.geo_json_feature_collection import GeoJsonFeatureCollection
from ..types.point import Point
from ..types.trajectory_station_in import TrajectoryStationIn
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCrsConverterApiV3Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def convert_point(
        self,
        *,
        from_crs: str,
        points: typing.Sequence[Point],
        to_crs: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConvertPointsResponse]:
        """
        Parameters
        ----------
        from_crs : str

        points : typing.Sequence[Point]

        to_crs : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConvertPointsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/convert",
            method="POST",
            json={
                "fromCRS": from_crs,
                "points": convert_and_respect_annotation_metadata(
                    object_=points, annotation=typing.Sequence[Point], direction="write"
                ),
                "toCRS": to_crs,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConvertPointsResponse,
                    parse_obj_as(
                        type_=ConvertPointsResponse,
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

    def convert_bin_grid(
        self,
        *,
        in_bin_grid: typing.Optional[AbstractBinGrid] = OMIT,
        to_crs: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConvertBinGridResponse]:
        """
        Parameters
        ----------
        in_bin_grid : typing.Optional[AbstractBinGrid]

        to_crs : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConvertBinGridResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/convertBinGrid",
            method="POST",
            json={
                "inBinGrid": convert_and_respect_annotation_metadata(
                    object_=in_bin_grid, annotation=AbstractBinGrid, direction="write"
                ),
                "toCRS": to_crs,
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
                    ConvertBinGridResponse,
                    parse_obj_as(
                        type_=ConvertBinGridResponse,
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

    def convert_geo_json(
        self,
        *,
        to_crs: str,
        feature_collection: typing.Optional[GeoJsonFeatureCollection] = OMIT,
        to_unit_z: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConvertGeoJsonResponse]:
        """
        Parameters
        ----------
        to_crs : str

        feature_collection : typing.Optional[GeoJsonFeatureCollection]

        to_unit_z : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConvertGeoJsonResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/convertGeoJson",
            method="POST",
            json={
                "featureCollection": convert_and_respect_annotation_metadata(
                    object_=feature_collection, annotation=GeoJsonFeatureCollection, direction="write"
                ),
                "toCRS": to_crs,
                "toUnitZ": to_unit_z,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConvertGeoJsonResponse,
                    parse_obj_as(
                        type_=ConvertGeoJsonResponse,
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

    def convert_trajectory(
        self,
        *,
        azimuth_reference: str,
        input_stations: typing.Sequence[TrajectoryStationIn],
        method: str,
        trajectory_crs: str,
        unit_z: str,
        input_kind: typing.Optional[str] = OMIT,
        interpolate: typing.Optional[bool] = OMIT,
        reference_point: typing.Optional[Point] = OMIT,
        unit_xy: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConvertTrajectoryResponse]:
        """
        Parameters
        ----------
        azimuth_reference : str

        input_stations : typing.Sequence[TrajectoryStationIn]

        method : str

        trajectory_crs : str

        unit_z : str

        input_kind : typing.Optional[str]

        interpolate : typing.Optional[bool]

        reference_point : typing.Optional[Point]

        unit_xy : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConvertTrajectoryResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/convertTrajectory",
            method="POST",
            json={
                "azimuthReference": azimuth_reference,
                "inputKind": input_kind,
                "inputStations": convert_and_respect_annotation_metadata(
                    object_=input_stations, annotation=typing.Sequence[TrajectoryStationIn], direction="write"
                ),
                "interpolate": interpolate,
                "method": method,
                "referencePoint": convert_and_respect_annotation_metadata(
                    object_=reference_point, annotation=Point, direction="write"
                ),
                "trajectoryCRS": trajectory_crs,
                "unitXY": unit_xy,
                "unitZ": unit_z,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConvertTrajectoryResponse,
                    parse_obj_as(
                        type_=ConvertTrajectoryResponse,
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


class AsyncRawCrsConverterApiV3Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def convert_point(
        self,
        *,
        from_crs: str,
        points: typing.Sequence[Point],
        to_crs: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConvertPointsResponse]:
        """
        Parameters
        ----------
        from_crs : str

        points : typing.Sequence[Point]

        to_crs : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConvertPointsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/convert",
            method="POST",
            json={
                "fromCRS": from_crs,
                "points": convert_and_respect_annotation_metadata(
                    object_=points, annotation=typing.Sequence[Point], direction="write"
                ),
                "toCRS": to_crs,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConvertPointsResponse,
                    parse_obj_as(
                        type_=ConvertPointsResponse,
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

    async def convert_bin_grid(
        self,
        *,
        in_bin_grid: typing.Optional[AbstractBinGrid] = OMIT,
        to_crs: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConvertBinGridResponse]:
        """
        Parameters
        ----------
        in_bin_grid : typing.Optional[AbstractBinGrid]

        to_crs : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConvertBinGridResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/convertBinGrid",
            method="POST",
            json={
                "inBinGrid": convert_and_respect_annotation_metadata(
                    object_=in_bin_grid, annotation=AbstractBinGrid, direction="write"
                ),
                "toCRS": to_crs,
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
                    ConvertBinGridResponse,
                    parse_obj_as(
                        type_=ConvertBinGridResponse,
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

    async def convert_geo_json(
        self,
        *,
        to_crs: str,
        feature_collection: typing.Optional[GeoJsonFeatureCollection] = OMIT,
        to_unit_z: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConvertGeoJsonResponse]:
        """
        Parameters
        ----------
        to_crs : str

        feature_collection : typing.Optional[GeoJsonFeatureCollection]

        to_unit_z : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConvertGeoJsonResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/convertGeoJson",
            method="POST",
            json={
                "featureCollection": convert_and_respect_annotation_metadata(
                    object_=feature_collection, annotation=GeoJsonFeatureCollection, direction="write"
                ),
                "toCRS": to_crs,
                "toUnitZ": to_unit_z,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConvertGeoJsonResponse,
                    parse_obj_as(
                        type_=ConvertGeoJsonResponse,
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

    async def convert_trajectory(
        self,
        *,
        azimuth_reference: str,
        input_stations: typing.Sequence[TrajectoryStationIn],
        method: str,
        trajectory_crs: str,
        unit_z: str,
        input_kind: typing.Optional[str] = OMIT,
        interpolate: typing.Optional[bool] = OMIT,
        reference_point: typing.Optional[Point] = OMIT,
        unit_xy: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConvertTrajectoryResponse]:
        """
        Parameters
        ----------
        azimuth_reference : str

        input_stations : typing.Sequence[TrajectoryStationIn]

        method : str

        trajectory_crs : str

        unit_z : str

        input_kind : typing.Optional[str]

        interpolate : typing.Optional[bool]

        reference_point : typing.Optional[Point]

        unit_xy : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConvertTrajectoryResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/convertTrajectory",
            method="POST",
            json={
                "azimuthReference": azimuth_reference,
                "inputKind": input_kind,
                "inputStations": convert_and_respect_annotation_metadata(
                    object_=input_stations, annotation=typing.Sequence[TrajectoryStationIn], direction="write"
                ),
                "interpolate": interpolate,
                "method": method,
                "referencePoint": convert_and_respect_annotation_metadata(
                    object_=reference_point, annotation=Point, direction="write"
                ),
                "trajectoryCRS": trajectory_crs,
                "unitXY": unit_xy,
                "unitZ": unit_z,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConvertTrajectoryResponse,
                    parse_obj_as(
                        type_=ConvertTrajectoryResponse,
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
