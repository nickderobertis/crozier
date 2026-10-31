

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.convert_geo_json_response import ConvertGeoJsonResponse
from ..types.convert_points_response import ConvertPointsResponse
from ..types.convert_trajectory_response import ConvertTrajectoryResponse
from ..types.geo_json_feature_collection import GeoJsonFeatureCollection
from ..types.point import Point
from ..types.trajectory_station_in import TrajectoryStationIn
from .raw_client import AsyncRawCrsConverterApiV2Client, RawCrsConverterApiV2Client


OMIT = typing.cast(typing.Any, ...)


class CrsConverterApiV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCrsConverterApiV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCrsConverterApiV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCrsConverterApiV2Client
        """
        return self._raw_client

    def convert_point1(
        self,
        *,
        from_crs: str,
        points: typing.Sequence[Point],
        to_crs: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConvertPointsResponse:
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
        ConvertPointsResponse
            OK

        Examples
        --------
        from fern import FernApi, Point

        client = FernApi(
            data_partition_id="YOUR_DATA_PARTITION_ID",
            token="YOUR_TOKEN",
        )
        client.crs_converter_api_v2.convert_point1(
            from_crs="fromCRS",
            points=[
                Point(
                    x=1.1,
                    y=1.1,
                    z=1.1,
                )
            ],
            to_crs="toCRS",
        )
        """
        _response = self._raw_client.convert_point1(
            from_crs=from_crs, points=points, to_crs=to_crs, request_options=request_options
        )
        return _response.data

    def convert_geo_json1(
        self,
        *,
        to_crs: str,
        feature_collection: typing.Optional[GeoJsonFeatureCollection] = OMIT,
        to_unit_z: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConvertGeoJsonResponse:
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
        ConvertGeoJsonResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            data_partition_id="YOUR_DATA_PARTITION_ID",
            token="YOUR_TOKEN",
        )
        client.crs_converter_api_v2.convert_geo_json1(
            to_crs="toCRS",
        )
        """
        _response = self._raw_client.convert_geo_json1(
            to_crs=to_crs, feature_collection=feature_collection, to_unit_z=to_unit_z, request_options=request_options
        )
        return _response.data

    def convert_trajectory1(
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
    ) -> ConvertTrajectoryResponse:
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
        ConvertTrajectoryResponse
            OK

        Examples
        --------
        from fern import FernApi, TrajectoryStationIn

        client = FernApi(
            data_partition_id="YOUR_DATA_PARTITION_ID",
            token="YOUR_TOKEN",
        )
        client.crs_converter_api_v2.convert_trajectory1(
            azimuth_reference="azimuthReference",
            input_stations=[
                TrajectoryStationIn(
                    azimuth=1.1,
                    inclination=1.1,
                    md=1.1,
                )
            ],
            method="method",
            trajectory_crs="trajectoryCRS",
            unit_z="unitZ",
        )
        """
        _response = self._raw_client.convert_trajectory1(
            azimuth_reference=azimuth_reference,
            input_stations=input_stations,
            method=method,
            trajectory_crs=trajectory_crs,
            unit_z=unit_z,
            input_kind=input_kind,
            interpolate=interpolate,
            reference_point=reference_point,
            unit_xy=unit_xy,
            request_options=request_options,
        )
        return _response.data


class AsyncCrsConverterApiV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCrsConverterApiV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCrsConverterApiV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCrsConverterApiV2Client
        """
        return self._raw_client

    async def convert_point1(
        self,
        *,
        from_crs: str,
        points: typing.Sequence[Point],
        to_crs: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConvertPointsResponse:
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
        ConvertPointsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Point

        client = AsyncFernApi(
            data_partition_id="YOUR_DATA_PARTITION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.crs_converter_api_v2.convert_point1(
                from_crs="fromCRS",
                points=[
                    Point(
                        x=1.1,
                        y=1.1,
                        z=1.1,
                    )
                ],
                to_crs="toCRS",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.convert_point1(
            from_crs=from_crs, points=points, to_crs=to_crs, request_options=request_options
        )
        return _response.data

    async def convert_geo_json1(
        self,
        *,
        to_crs: str,
        feature_collection: typing.Optional[GeoJsonFeatureCollection] = OMIT,
        to_unit_z: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConvertGeoJsonResponse:
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
        ConvertGeoJsonResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            data_partition_id="YOUR_DATA_PARTITION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.crs_converter_api_v2.convert_geo_json1(
                to_crs="toCRS",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.convert_geo_json1(
            to_crs=to_crs, feature_collection=feature_collection, to_unit_z=to_unit_z, request_options=request_options
        )
        return _response.data

    async def convert_trajectory1(
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
    ) -> ConvertTrajectoryResponse:
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
        ConvertTrajectoryResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TrajectoryStationIn

        client = AsyncFernApi(
            data_partition_id="YOUR_DATA_PARTITION_ID",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.crs_converter_api_v2.convert_trajectory1(
                azimuth_reference="azimuthReference",
                input_stations=[
                    TrajectoryStationIn(
                        azimuth=1.1,
                        inclination=1.1,
                        md=1.1,
                    )
                ],
                method="method",
                trajectory_crs="trajectoryCRS",
                unit_z="unitZ",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.convert_trajectory1(
            azimuth_reference=azimuth_reference,
            input_stations=input_stations,
            method=method,
            trajectory_crs=trajectory_crs,
            unit_z=unit_z,
            input_kind=input_kind,
            interpolate=interpolate,
            reference_point=reference_point,
            unit_xy=unit_xy,
            request_options=request_options,
        )
        return _response.data
