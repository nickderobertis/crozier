

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.averages_v2get_v2averages_get_request_date_from import AveragesV2GetV2AveragesGetRequestDateFrom
from ..types.averages_v2get_v2averages_get_request_date_to import AveragesV2GetV2AveragesGetRequestDateTo
from ..types.cities_order import CitiesOrder
from ..types.countries_order import CountriesOrder
from ..types.entity_types import EntityTypes
from ..types.get_mobilegentile_v2locations_tiles_mobile_generalized_zxy_pbf_get_request_last_updated_from import (
    GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedFrom,
)
from ..types.get_mobilegentile_v2locations_tiles_mobile_generalized_zxy_pbf_get_request_last_updated_to import (
    GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedTo,
)
from ..types.get_mobilegentile_v2locations_tiles_mobile_generalized_zxy_pbf_get_request_parameter import (
    GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestParameter,
)
from ..types.get_mobiletile_v2locations_tiles_mobile_zxy_pbf_get_request_last_updated_from import (
    GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedFrom,
)
from ..types.get_mobiletile_v2locations_tiles_mobile_zxy_pbf_get_request_last_updated_to import (
    GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedTo,
)
from ..types.get_mobiletile_v2locations_tiles_mobile_zxy_pbf_get_request_parameter import (
    GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestParameter,
)
from ..types.get_tile_v2locations_tiles_zxy_pbf_get_request_last_updated_from import (
    GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedFrom,
)
from ..types.get_tile_v2locations_tiles_zxy_pbf_get_request_last_updated_to import (
    GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedTo,
)
from ..types.get_tile_v2locations_tiles_zxy_pbf_get_request_parameter import (
    GetTileV2LocationsTilesZxyPbfGetRequestParameter,
)
from ..types.locations_order import LocationsOrder
from ..types.meas_order import MeasOrder
from ..types.measurements_get_v2measurements_get_request_date_from import (
    MeasurementsGetV2MeasurementsGetRequestDateFrom,
)
from ..types.measurements_get_v2measurements_get_request_date_to import MeasurementsGetV2MeasurementsGetRequestDateTo
from ..types.open_aq_cities_result import OpenAqCitiesResult
from ..types.open_aq_countries_result import OpenAqCountriesResult
from ..types.open_aq_parameters_result import OpenAqParametersResult
from ..types.open_aq_projects_result import OpenAqProjectsResult
from ..types.open_aq_result import OpenAqResult
from ..types.projects_order import ProjectsOrder
from ..types.sensor_types import SensorTypes
from ..types.sort import Sort
from ..types.sources_order import SourcesOrder
from ..types.spatial import Spatial
from ..types.temporal import Temporal
from ..types.tile_json import TileJson
from .raw_client import AsyncRawV2Client, RawV2Client
from .types.averages_v2get_v2averages_get_request_parameter_item import AveragesV2GetV2AveragesGetRequestParameterItem
from .types.averages_v2get_v2averages_get_request_project_item import AveragesV2GetV2AveragesGetRequestProjectItem
from .types.get_mobiletile_v2locations_tiles_mobile_zxy_pbf_get_request_date_from import (
    GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateFrom,
)
from .types.get_mobiletile_v2locations_tiles_mobile_zxy_pbf_get_request_date_to import (
    GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateTo,
)
from .types.latest_get_v2latest_location_id_get_request_location_item import (
    LatestGetV2LatestLocationIdGetRequestLocationItem,
)
from .types.latest_get_v2latest_location_id_get_request_parameter_item import (
    LatestGetV2LatestLocationIdGetRequestParameterItem,
)
from .types.locations_get_v2locations_location_id_get_request_location_item import (
    LocationsGetV2LocationsLocationIdGetRequestLocationItem,
)
from .types.locations_get_v2locations_location_id_get_request_parameter_item import (
    LocationsGetV2LocationsLocationIdGetRequestParameterItem,
)
from .types.measurements_get_v2measurements_get_request_location_item import (
    MeasurementsGetV2MeasurementsGetRequestLocationItem,
)
from .types.measurements_get_v2measurements_get_request_parameter_item import (
    MeasurementsGetV2MeasurementsGetRequestParameterItem,
)
from .types.projects_get_v2projects_project_id_get_request_parameter_item import (
    ProjectsGetV2ProjectsProjectIdGetRequestParameterItem,
)
from .types.projects_get_v2projects_project_id_get_request_project_item import (
    ProjectsGetV2ProjectsProjectIdGetRequestProjectItem,
)


class V2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawV2Client
        """
        return self._raw_client

    def averages_v2get(
        self,
        *,
        spatial: Spatial,
        temporal: Temporal,
        date_from: typing.Optional[AveragesV2GetV2AveragesGetRequestDateFrom] = None,
        date_to: typing.Optional[AveragesV2GetV2AveragesGetRequestDateTo] = None,
        parameter_id: typing.Optional[int] = None,
        parameter: typing.Optional[
            typing.Union[
                AveragesV2GetV2AveragesGetRequestParameterItem,
                typing.Sequence[AveragesV2GetV2AveragesGetRequestParameterItem],
            ]
        ] = None,
        unit: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        project_id: typing.Optional[int] = None,
        project: typing.Optional[
            typing.Union[
                AveragesV2GetV2AveragesGetRequestProjectItem,
                typing.Sequence[AveragesV2GetV2AveragesGetRequestProjectItem],
            ]
        ] = None,
        country_id: typing.Optional[str] = None,
        country: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        group: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAqResult:
        """
        Parameters
        ----------
        spatial : Spatial

        temporal : Temporal

        date_from : typing.Optional[AveragesV2GetV2AveragesGetRequestDateFrom]

        date_to : typing.Optional[AveragesV2GetV2AveragesGetRequestDateTo]

        parameter_id : typing.Optional[int]

        parameter : typing.Optional[typing.Union[AveragesV2GetV2AveragesGetRequestParameterItem, typing.Sequence[AveragesV2GetV2AveragesGetRequestParameterItem]]]

        unit : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        project_id : typing.Optional[int]

        project : typing.Optional[typing.Union[AveragesV2GetV2AveragesGetRequestProjectItem, typing.Sequence[AveragesV2GetV2AveragesGetRequestProjectItem]]]

        country_id : typing.Optional[str]

                    Limit results by a certain country using two letter country code.
                    (ex. /US)


        country : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain country using two letter country code.
                    (ex. ?country=US or ?country=US&country=MX)


        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]
            Define sort order.

        location : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        group : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqResult
            Successful Response

        Examples
        --------
        from fern import FernApi, Spatial, Temporal

        client = FernApi()
        client.v2.averages_v2get(
            spatial=Spatial.COUNTRY,
            temporal=Temporal.DAY,
        )
        """
        _response = self._raw_client.averages_v2get(
            spatial=spatial,
            temporal=temporal,
            date_from=date_from,
            date_to=date_to,
            parameter_id=parameter_id,
            parameter=parameter,
            unit=unit,
            project_id=project_id,
            project=project,
            country_id=country_id,
            country=country,
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            location=location,
            group=group,
            request_options=request_options,
        )
        return _response.data

    def cities_get(
        self,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        country_id: typing.Optional[str] = None,
        country: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        city: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[CitiesOrder] = None,
        entity: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAqCitiesResult:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]
            Define sort order.

        country_id : typing.Optional[str]

                    Limit results by a certain country using two letter country code.
                    (ex. /US)


        country : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain country using two letter country code.
                    (ex. ?country=US or ?country=US&country=MX)


        city : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain city or cities.
                    (ex. ?city=Chicago or ?city=Chicago&city=Boston)


        order_by : typing.Optional[CitiesOrder]
            Order by a field

        entity : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqCitiesResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.cities_get()
        """
        _response = self._raw_client.cities_get(
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            country_id=country_id,
            country=country,
            city=city,
            order_by=order_by,
            entity=entity,
            request_options=request_options,
        )
        return _response.data

    def countries_get(
        self,
        country_id: str,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        country: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[CountriesOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAqCountriesResult:
        """
        Parameters
        ----------
        country_id : str

        limit : typing.Optional[int]

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]
            Define sort order.

        country : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain country using two letter country code.
                    (ex. ?country=US or ?country=US&country=MX)


        order_by : typing.Optional[CountriesOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqCountriesResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.countries_get(
            country_id="country_id",
        )
        """
        _response = self._raw_client.countries_get(
            country_id,
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            country=country,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    def latest_get(
        self,
        location_id: int,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        has_geo: typing.Optional[bool] = None,
        parameter_id: typing.Optional[int] = None,
        parameter: typing.Optional[
            typing.Union[
                LatestGetV2LatestLocationIdGetRequestParameterItem,
                typing.Sequence[LatestGetV2LatestLocationIdGetRequestParameterItem],
            ]
        ] = None,
        unit: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        coordinates: typing.Optional[str] = None,
        radius: typing.Optional[int] = None,
        country_id: typing.Optional[str] = None,
        country: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        city: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[
            typing.Union[
                LatestGetV2LatestLocationIdGetRequestLocationItem,
                typing.Sequence[LatestGetV2LatestLocationIdGetRequestLocationItem],
            ]
        ] = None,
        order_by: typing.Optional[LocationsOrder] = None,
        is_mobile: typing.Optional[bool] = None,
        is_analysis: typing.Optional[bool] = None,
        source_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        entity: typing.Optional[EntityTypes] = None,
        sensor_type: typing.Optional[SensorTypes] = None,
        model_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        manufacturer_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        dump_raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAqResult:
        """
        Parameters
        ----------
        location_id : int

        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]
            Sort Direction

        has_geo : typing.Optional[bool]

        parameter_id : typing.Optional[int]

        parameter : typing.Optional[typing.Union[LatestGetV2LatestLocationIdGetRequestParameterItem, typing.Sequence[LatestGetV2LatestLocationIdGetRequestParameterItem]]]

        unit : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        coordinates : typing.Optional[str]

        radius : typing.Optional[int]

        country_id : typing.Optional[str]

                    Limit results by a certain country using two letter country code.
                    (ex. /US)


        country : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain country using two letter country code.
                    (ex. ?country=US or ?country=US&country=MX)


        city : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain city or cities.
                    (ex. ?city=Chicago or ?city=Chicago&city=Boston)


        location : typing.Optional[typing.Union[LatestGetV2LatestLocationIdGetRequestLocationItem, typing.Sequence[LatestGetV2LatestLocationIdGetRequestLocationItem]]]

        order_by : typing.Optional[LocationsOrder]
            Order by a field

        is_mobile : typing.Optional[bool]
            Location is mobile

        is_analysis : typing.Optional[bool]
            Data is the product of a previous analysis/aggregation and not raw measurements

        source_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Name of the data source

        entity : typing.Optional[EntityTypes]
            Source entity type.

        sensor_type : typing.Optional[SensorTypes]
            Type of Sensor

        model_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Model Name of Sensor

        manufacturer_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Manufacturer of Sensor

        dump_raw : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.latest_get(
            location_id=1,
        )
        """
        _response = self._raw_client.latest_get(
            location_id,
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            has_geo=has_geo,
            parameter_id=parameter_id,
            parameter=parameter,
            unit=unit,
            coordinates=coordinates,
            radius=radius,
            country_id=country_id,
            country=country,
            city=city,
            location=location,
            order_by=order_by,
            is_mobile=is_mobile,
            is_analysis=is_analysis,
            source_name=source_name,
            entity=entity,
            sensor_type=sensor_type,
            model_name=model_name,
            manufacturer_name=manufacturer_name,
            dump_raw=dump_raw,
            request_options=request_options,
        )
        return _response.data

    def locations_get(
        self,
        location_id: int,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        has_geo: typing.Optional[bool] = None,
        parameter_id: typing.Optional[int] = None,
        parameter: typing.Optional[
            typing.Union[
                LocationsGetV2LocationsLocationIdGetRequestParameterItem,
                typing.Sequence[LocationsGetV2LocationsLocationIdGetRequestParameterItem],
            ]
        ] = None,
        unit: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        coordinates: typing.Optional[str] = None,
        radius: typing.Optional[int] = None,
        country_id: typing.Optional[str] = None,
        country: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        city: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[
            typing.Union[
                LocationsGetV2LocationsLocationIdGetRequestLocationItem,
                typing.Sequence[LocationsGetV2LocationsLocationIdGetRequestLocationItem],
            ]
        ] = None,
        order_by: typing.Optional[LocationsOrder] = None,
        is_mobile: typing.Optional[bool] = None,
        is_analysis: typing.Optional[bool] = None,
        source_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        entity: typing.Optional[EntityTypes] = None,
        sensor_type: typing.Optional[SensorTypes] = None,
        model_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        manufacturer_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        dump_raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAqResult:
        """
        Parameters
        ----------
        location_id : int

        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]
            Sort Direction

        has_geo : typing.Optional[bool]

        parameter_id : typing.Optional[int]

        parameter : typing.Optional[typing.Union[LocationsGetV2LocationsLocationIdGetRequestParameterItem, typing.Sequence[LocationsGetV2LocationsLocationIdGetRequestParameterItem]]]

        unit : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        coordinates : typing.Optional[str]

        radius : typing.Optional[int]

        country_id : typing.Optional[str]

                    Limit results by a certain country using two letter country code.
                    (ex. /US)


        country : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain country using two letter country code.
                    (ex. ?country=US or ?country=US&country=MX)


        city : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain city or cities.
                    (ex. ?city=Chicago or ?city=Chicago&city=Boston)


        location : typing.Optional[typing.Union[LocationsGetV2LocationsLocationIdGetRequestLocationItem, typing.Sequence[LocationsGetV2LocationsLocationIdGetRequestLocationItem]]]

        order_by : typing.Optional[LocationsOrder]
            Order by a field

        is_mobile : typing.Optional[bool]
            Location is mobile

        is_analysis : typing.Optional[bool]
            Data is the product of a previous analysis/aggregation and not raw measurements

        source_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Name of the data source

        entity : typing.Optional[EntityTypes]
            Source entity type.

        sensor_type : typing.Optional[SensorTypes]
            Type of Sensor

        model_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Model Name of Sensor

        manufacturer_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Manufacturer of Sensor

        dump_raw : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.locations_get(
            location_id=1,
        )
        """
        _response = self._raw_client.locations_get(
            location_id,
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            has_geo=has_geo,
            parameter_id=parameter_id,
            parameter=parameter,
            unit=unit,
            coordinates=coordinates,
            radius=radius,
            country_id=country_id,
            country=country,
            city=city,
            location=location,
            order_by=order_by,
            is_mobile=is_mobile,
            is_analysis=is_analysis,
            source_name=source_name,
            entity=entity,
            sensor_type=sensor_type,
            model_name=model_name,
            manufacturer_name=manufacturer_name,
            dump_raw=dump_raw,
            request_options=request_options,
        )
        return _response.data

    def mobilegentilejson(self, *, request_options: typing.Optional[RequestOptions] = None) -> TileJson:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TileJson
            Return a tilejson

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.mobilegentilejson()
        """
        _response = self._raw_client.mobilegentilejson(request_options=request_options)
        return _response.data

    def get_mobilegentile(
        self,
        z: int,
        x: int,
        y: int,
        *,
        parameter: typing.Optional[GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestParameter] = None,
        location: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        last_updated_from: typing.Optional[
            GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedFrom
        ] = None,
        last_updated_to: typing.Optional[
            GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedTo
        ] = None,
        is_mobile: typing.Optional[bool] = None,
        project: typing.Optional[int] = None,
        is_analysis: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        z : int

        x : int

        y : int

        parameter : typing.Optional[GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestParameter]

        location : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            limit data to location id

        last_updated_from : typing.Optional[GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedFrom]

        last_updated_to : typing.Optional[GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedTo]

        is_mobile : typing.Optional[bool]

        project : typing.Optional[int]

        is_analysis : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.get_mobilegentile(
            z=1,
            x=1,
            y=1,
        )
        """
        _response = self._raw_client.get_mobilegentile(
            z,
            x,
            y,
            parameter=parameter,
            location=location,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            is_mobile=is_mobile,
            project=project,
            is_analysis=is_analysis,
            request_options=request_options,
        )
        return _response.data

    def mobiletilejson(self, *, request_options: typing.Optional[RequestOptions] = None) -> TileJson:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TileJson
            Return a tilejson

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.mobiletilejson()
        """
        _response = self._raw_client.mobiletilejson(request_options=request_options)
        return _response.data

    def get_mobiletile(
        self,
        z: int,
        x: int,
        y: int,
        *,
        date_from: GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateFrom,
        date_to: GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateTo,
        parameter: typing.Optional[GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestParameter] = None,
        location: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        last_updated_from: typing.Optional[GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedFrom] = None,
        last_updated_to: typing.Optional[GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedTo] = None,
        is_mobile: typing.Optional[bool] = None,
        project: typing.Optional[int] = None,
        is_analysis: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        z : int

        x : int

        y : int

        date_from : GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateFrom

        date_to : GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateTo

        parameter : typing.Optional[GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestParameter]

        location : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            limit data to location id

        last_updated_from : typing.Optional[GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedFrom]

        last_updated_to : typing.Optional[GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedTo]

        is_mobile : typing.Optional[bool]

        project : typing.Optional[int]

        is_analysis : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi()
        client.v2.get_mobiletile(
            z=1,
            x=1,
            y=1,
            date_from=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            date_to=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.get_mobiletile(
            z,
            x,
            y,
            date_from=date_from,
            date_to=date_to,
            parameter=parameter,
            location=location,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            is_mobile=is_mobile,
            project=project,
            is_analysis=is_analysis,
            request_options=request_options,
        )
        return _response.data

    def tilejson(self, *, request_options: typing.Optional[RequestOptions] = None) -> TileJson:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TileJson
            Return a tilejson

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.tilejson()
        """
        _response = self._raw_client.tilejson(request_options=request_options)
        return _response.data

    def demo(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.demo()
        """
        _response = self._raw_client.demo(request_options=request_options)
        return _response.data

    def get_tile(
        self,
        z: int,
        x: int,
        y: int,
        *,
        parameter: typing.Optional[GetTileV2LocationsTilesZxyPbfGetRequestParameter] = None,
        location: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        last_updated_from: typing.Optional[GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedFrom] = None,
        last_updated_to: typing.Optional[GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedTo] = None,
        is_mobile: typing.Optional[bool] = None,
        project: typing.Optional[int] = None,
        is_analysis: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        z : int

        x : int

        y : int

        parameter : typing.Optional[GetTileV2LocationsTilesZxyPbfGetRequestParameter]

        location : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            limit data to location id

        last_updated_from : typing.Optional[GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedFrom]

        last_updated_to : typing.Optional[GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedTo]

        is_mobile : typing.Optional[bool]

        project : typing.Optional[int]

        is_analysis : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.get_tile(
            z=1,
            x=1,
            y=1,
        )
        """
        _response = self._raw_client.get_tile(
            z,
            x,
            y,
            parameter=parameter,
            location=location,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            is_mobile=is_mobile,
            project=project,
            is_analysis=is_analysis,
            request_options=request_options,
        )
        return _response.data

    def mfr_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> OpenAqResult:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.mfr_get()
        """
        _response = self._raw_client.mfr_get(request_options=request_options)
        return _response.data

    def measurements_get(
        self,
        *,
        format: typing.Optional[str] = None,
        date_from: typing.Optional[MeasurementsGetV2MeasurementsGetRequestDateFrom] = None,
        date_to: typing.Optional[MeasurementsGetV2MeasurementsGetRequestDateTo] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        has_geo: typing.Optional[bool] = None,
        parameter_id: typing.Optional[int] = None,
        parameter: typing.Optional[
            typing.Union[
                MeasurementsGetV2MeasurementsGetRequestParameterItem,
                typing.Sequence[MeasurementsGetV2MeasurementsGetRequestParameterItem],
            ]
        ] = None,
        unit: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        coordinates: typing.Optional[str] = None,
        radius: typing.Optional[int] = None,
        country_id: typing.Optional[str] = None,
        country: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        city: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location_id: typing.Optional[int] = None,
        location: typing.Optional[
            typing.Union[
                MeasurementsGetV2MeasurementsGetRequestLocationItem,
                typing.Sequence[MeasurementsGetV2MeasurementsGetRequestLocationItem],
            ]
        ] = None,
        order_by: typing.Optional[MeasOrder] = None,
        is_mobile: typing.Optional[bool] = None,
        is_analysis: typing.Optional[bool] = None,
        project: typing.Optional[int] = None,
        entity: typing.Optional[EntityTypes] = None,
        sensor_type: typing.Optional[SensorTypes] = None,
        value_from: typing.Optional[float] = None,
        value_to: typing.Optional[float] = None,
        include_fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        format : typing.Optional[str]

        date_from : typing.Optional[MeasurementsGetV2MeasurementsGetRequestDateFrom]

        date_to : typing.Optional[MeasurementsGetV2MeasurementsGetRequestDateTo]

        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]

        has_geo : typing.Optional[bool]

        parameter_id : typing.Optional[int]

        parameter : typing.Optional[typing.Union[MeasurementsGetV2MeasurementsGetRequestParameterItem, typing.Sequence[MeasurementsGetV2MeasurementsGetRequestParameterItem]]]

        unit : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        coordinates : typing.Optional[str]

        radius : typing.Optional[int]

        country_id : typing.Optional[str]

                    Limit results by a certain country using two letter country code.
                    (ex. /US)


        country : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain country using two letter country code.
                    (ex. ?country=US or ?country=US&country=MX)


        city : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain city or cities.
                    (ex. ?city=Chicago or ?city=Chicago&city=Boston)


        location_id : typing.Optional[int]

        location : typing.Optional[typing.Union[MeasurementsGetV2MeasurementsGetRequestLocationItem, typing.Sequence[MeasurementsGetV2MeasurementsGetRequestLocationItem]]]

        order_by : typing.Optional[MeasOrder]

        is_mobile : typing.Optional[bool]

        is_analysis : typing.Optional[bool]

        project : typing.Optional[int]

        entity : typing.Optional[EntityTypes]

        sensor_type : typing.Optional[SensorTypes]

        value_from : typing.Optional[float]

        value_to : typing.Optional[float]

        include_fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.measurements_get()
        """
        _response = self._raw_client.measurements_get(
            format=format,
            date_from=date_from,
            date_to=date_to,
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            has_geo=has_geo,
            parameter_id=parameter_id,
            parameter=parameter,
            unit=unit,
            coordinates=coordinates,
            radius=radius,
            country_id=country_id,
            country=country,
            city=city,
            location_id=location_id,
            location=location,
            order_by=order_by,
            is_mobile=is_mobile,
            is_analysis=is_analysis,
            project=project,
            entity=entity,
            sensor_type=sensor_type,
            value_from=value_from,
            value_to=value_to,
            include_fields=include_fields,
            request_options=request_options,
        )
        return _response.data

    def model_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> OpenAqResult:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.model_get()
        """
        _response = self._raw_client.model_get(request_options=request_options)
        return _response.data

    def parameters_get(
        self,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        source_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        source_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        source_slug: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAqParametersResult:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]
            Define sort order.

        source_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        source_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        source_slug : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        order_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqParametersResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.parameters_get()
        """
        _response = self._raw_client.parameters_get(
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            source_name=source_name,
            source_id=source_id,
            source_slug=source_slug,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    def projects_get(
        self,
        project_id: int,
        *,
        country_id: typing.Optional[str] = None,
        country: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        parameter_id: typing.Optional[int] = None,
        parameter: typing.Optional[
            typing.Union[
                ProjectsGetV2ProjectsProjectIdGetRequestParameterItem,
                typing.Sequence[ProjectsGetV2ProjectsProjectIdGetRequestParameterItem],
            ]
        ] = None,
        unit: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        project: typing.Optional[
            typing.Union[
                ProjectsGetV2ProjectsProjectIdGetRequestProjectItem,
                typing.Sequence[ProjectsGetV2ProjectsProjectIdGetRequestProjectItem],
            ]
        ] = None,
        order_by: typing.Optional[ProjectsOrder] = None,
        is_mobile: typing.Optional[bool] = None,
        is_analysis: typing.Optional[bool] = None,
        entity: typing.Optional[str] = None,
        sensor_type: typing.Optional[str] = None,
        source_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAqProjectsResult:
        """
        Parameters
        ----------
        project_id : int

        country_id : typing.Optional[str]

                    Limit results by a certain country using two letter country code.
                    (ex. /US)


        country : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain country using two letter country code.
                    (ex. ?country=US or ?country=US&country=MX)


        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]
            Define sort order.

        parameter_id : typing.Optional[int]

        parameter : typing.Optional[typing.Union[ProjectsGetV2ProjectsProjectIdGetRequestParameterItem, typing.Sequence[ProjectsGetV2ProjectsProjectIdGetRequestParameterItem]]]

        unit : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        project : typing.Optional[typing.Union[ProjectsGetV2ProjectsProjectIdGetRequestProjectItem, typing.Sequence[ProjectsGetV2ProjectsProjectIdGetRequestProjectItem]]]

        order_by : typing.Optional[ProjectsOrder]

        is_mobile : typing.Optional[bool]

        is_analysis : typing.Optional[bool]

        entity : typing.Optional[str]

        sensor_type : typing.Optional[str]

        source_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqProjectsResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.projects_get(
            project_id=1,
        )
        """
        _response = self._raw_client.projects_get(
            project_id,
            country_id=country_id,
            country=country,
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            parameter_id=parameter_id,
            parameter=parameter,
            unit=unit,
            project=project,
            order_by=order_by,
            is_mobile=is_mobile,
            is_analysis=is_analysis,
            entity=entity,
            sensor_type=sensor_type,
            source_name=source_name,
            request_options=request_options,
        )
        return _response.data

    def sources_get(
        self,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        source_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        source_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        source_slug: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[SourcesOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAqResult:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]
            Define sort order.

        source_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        source_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        source_slug : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        order_by : typing.Optional[SourcesOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.sources_get()
        """
        _response = self._raw_client.sources_get(
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            source_name=source_name,
            source_id=source_id,
            source_slug=source_slug,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    def readme_get(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.readme_get(
            slug="slug",
        )
        """
        _response = self._raw_client.readme_get(slug, request_options=request_options)
        return _response.data

    def summary_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> OpenAqResult:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v2.summary_get()
        """
        _response = self._raw_client.summary_get(request_options=request_options)
        return _response.data


class AsyncV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawV2Client
        """
        return self._raw_client

    async def averages_v2get(
        self,
        *,
        spatial: Spatial,
        temporal: Temporal,
        date_from: typing.Optional[AveragesV2GetV2AveragesGetRequestDateFrom] = None,
        date_to: typing.Optional[AveragesV2GetV2AveragesGetRequestDateTo] = None,
        parameter_id: typing.Optional[int] = None,
        parameter: typing.Optional[
            typing.Union[
                AveragesV2GetV2AveragesGetRequestParameterItem,
                typing.Sequence[AveragesV2GetV2AveragesGetRequestParameterItem],
            ]
        ] = None,
        unit: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        project_id: typing.Optional[int] = None,
        project: typing.Optional[
            typing.Union[
                AveragesV2GetV2AveragesGetRequestProjectItem,
                typing.Sequence[AveragesV2GetV2AveragesGetRequestProjectItem],
            ]
        ] = None,
        country_id: typing.Optional[str] = None,
        country: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        group: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAqResult:
        """
        Parameters
        ----------
        spatial : Spatial

        temporal : Temporal

        date_from : typing.Optional[AveragesV2GetV2AveragesGetRequestDateFrom]

        date_to : typing.Optional[AveragesV2GetV2AveragesGetRequestDateTo]

        parameter_id : typing.Optional[int]

        parameter : typing.Optional[typing.Union[AveragesV2GetV2AveragesGetRequestParameterItem, typing.Sequence[AveragesV2GetV2AveragesGetRequestParameterItem]]]

        unit : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        project_id : typing.Optional[int]

        project : typing.Optional[typing.Union[AveragesV2GetV2AveragesGetRequestProjectItem, typing.Sequence[AveragesV2GetV2AveragesGetRequestProjectItem]]]

        country_id : typing.Optional[str]

                    Limit results by a certain country using two letter country code.
                    (ex. /US)


        country : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain country using two letter country code.
                    (ex. ?country=US or ?country=US&country=MX)


        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]
            Define sort order.

        location : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        group : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Spatial, Temporal

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.averages_v2get(
                spatial=Spatial.COUNTRY,
                temporal=Temporal.DAY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.averages_v2get(
            spatial=spatial,
            temporal=temporal,
            date_from=date_from,
            date_to=date_to,
            parameter_id=parameter_id,
            parameter=parameter,
            unit=unit,
            project_id=project_id,
            project=project,
            country_id=country_id,
            country=country,
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            location=location,
            group=group,
            request_options=request_options,
        )
        return _response.data

    async def cities_get(
        self,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        country_id: typing.Optional[str] = None,
        country: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        city: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[CitiesOrder] = None,
        entity: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAqCitiesResult:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]
            Define sort order.

        country_id : typing.Optional[str]

                    Limit results by a certain country using two letter country code.
                    (ex. /US)


        country : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain country using two letter country code.
                    (ex. ?country=US or ?country=US&country=MX)


        city : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain city or cities.
                    (ex. ?city=Chicago or ?city=Chicago&city=Boston)


        order_by : typing.Optional[CitiesOrder]
            Order by a field

        entity : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqCitiesResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.cities_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.cities_get(
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            country_id=country_id,
            country=country,
            city=city,
            order_by=order_by,
            entity=entity,
            request_options=request_options,
        )
        return _response.data

    async def countries_get(
        self,
        country_id: str,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        country: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[CountriesOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAqCountriesResult:
        """
        Parameters
        ----------
        country_id : str

        limit : typing.Optional[int]

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]
            Define sort order.

        country : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain country using two letter country code.
                    (ex. ?country=US or ?country=US&country=MX)


        order_by : typing.Optional[CountriesOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqCountriesResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.countries_get(
                country_id="country_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.countries_get(
            country_id,
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            country=country,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    async def latest_get(
        self,
        location_id: int,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        has_geo: typing.Optional[bool] = None,
        parameter_id: typing.Optional[int] = None,
        parameter: typing.Optional[
            typing.Union[
                LatestGetV2LatestLocationIdGetRequestParameterItem,
                typing.Sequence[LatestGetV2LatestLocationIdGetRequestParameterItem],
            ]
        ] = None,
        unit: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        coordinates: typing.Optional[str] = None,
        radius: typing.Optional[int] = None,
        country_id: typing.Optional[str] = None,
        country: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        city: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[
            typing.Union[
                LatestGetV2LatestLocationIdGetRequestLocationItem,
                typing.Sequence[LatestGetV2LatestLocationIdGetRequestLocationItem],
            ]
        ] = None,
        order_by: typing.Optional[LocationsOrder] = None,
        is_mobile: typing.Optional[bool] = None,
        is_analysis: typing.Optional[bool] = None,
        source_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        entity: typing.Optional[EntityTypes] = None,
        sensor_type: typing.Optional[SensorTypes] = None,
        model_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        manufacturer_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        dump_raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAqResult:
        """
        Parameters
        ----------
        location_id : int

        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]
            Sort Direction

        has_geo : typing.Optional[bool]

        parameter_id : typing.Optional[int]

        parameter : typing.Optional[typing.Union[LatestGetV2LatestLocationIdGetRequestParameterItem, typing.Sequence[LatestGetV2LatestLocationIdGetRequestParameterItem]]]

        unit : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        coordinates : typing.Optional[str]

        radius : typing.Optional[int]

        country_id : typing.Optional[str]

                    Limit results by a certain country using two letter country code.
                    (ex. /US)


        country : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain country using two letter country code.
                    (ex. ?country=US or ?country=US&country=MX)


        city : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain city or cities.
                    (ex. ?city=Chicago or ?city=Chicago&city=Boston)


        location : typing.Optional[typing.Union[LatestGetV2LatestLocationIdGetRequestLocationItem, typing.Sequence[LatestGetV2LatestLocationIdGetRequestLocationItem]]]

        order_by : typing.Optional[LocationsOrder]
            Order by a field

        is_mobile : typing.Optional[bool]
            Location is mobile

        is_analysis : typing.Optional[bool]
            Data is the product of a previous analysis/aggregation and not raw measurements

        source_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Name of the data source

        entity : typing.Optional[EntityTypes]
            Source entity type.

        sensor_type : typing.Optional[SensorTypes]
            Type of Sensor

        model_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Model Name of Sensor

        manufacturer_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Manufacturer of Sensor

        dump_raw : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.latest_get(
                location_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.latest_get(
            location_id,
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            has_geo=has_geo,
            parameter_id=parameter_id,
            parameter=parameter,
            unit=unit,
            coordinates=coordinates,
            radius=radius,
            country_id=country_id,
            country=country,
            city=city,
            location=location,
            order_by=order_by,
            is_mobile=is_mobile,
            is_analysis=is_analysis,
            source_name=source_name,
            entity=entity,
            sensor_type=sensor_type,
            model_name=model_name,
            manufacturer_name=manufacturer_name,
            dump_raw=dump_raw,
            request_options=request_options,
        )
        return _response.data

    async def locations_get(
        self,
        location_id: int,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        has_geo: typing.Optional[bool] = None,
        parameter_id: typing.Optional[int] = None,
        parameter: typing.Optional[
            typing.Union[
                LocationsGetV2LocationsLocationIdGetRequestParameterItem,
                typing.Sequence[LocationsGetV2LocationsLocationIdGetRequestParameterItem],
            ]
        ] = None,
        unit: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        coordinates: typing.Optional[str] = None,
        radius: typing.Optional[int] = None,
        country_id: typing.Optional[str] = None,
        country: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        city: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[
            typing.Union[
                LocationsGetV2LocationsLocationIdGetRequestLocationItem,
                typing.Sequence[LocationsGetV2LocationsLocationIdGetRequestLocationItem],
            ]
        ] = None,
        order_by: typing.Optional[LocationsOrder] = None,
        is_mobile: typing.Optional[bool] = None,
        is_analysis: typing.Optional[bool] = None,
        source_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        entity: typing.Optional[EntityTypes] = None,
        sensor_type: typing.Optional[SensorTypes] = None,
        model_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        manufacturer_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        dump_raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAqResult:
        """
        Parameters
        ----------
        location_id : int

        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]
            Sort Direction

        has_geo : typing.Optional[bool]

        parameter_id : typing.Optional[int]

        parameter : typing.Optional[typing.Union[LocationsGetV2LocationsLocationIdGetRequestParameterItem, typing.Sequence[LocationsGetV2LocationsLocationIdGetRequestParameterItem]]]

        unit : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        coordinates : typing.Optional[str]

        radius : typing.Optional[int]

        country_id : typing.Optional[str]

                    Limit results by a certain country using two letter country code.
                    (ex. /US)


        country : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain country using two letter country code.
                    (ex. ?country=US or ?country=US&country=MX)


        city : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain city or cities.
                    (ex. ?city=Chicago or ?city=Chicago&city=Boston)


        location : typing.Optional[typing.Union[LocationsGetV2LocationsLocationIdGetRequestLocationItem, typing.Sequence[LocationsGetV2LocationsLocationIdGetRequestLocationItem]]]

        order_by : typing.Optional[LocationsOrder]
            Order by a field

        is_mobile : typing.Optional[bool]
            Location is mobile

        is_analysis : typing.Optional[bool]
            Data is the product of a previous analysis/aggregation and not raw measurements

        source_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Name of the data source

        entity : typing.Optional[EntityTypes]
            Source entity type.

        sensor_type : typing.Optional[SensorTypes]
            Type of Sensor

        model_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Model Name of Sensor

        manufacturer_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Manufacturer of Sensor

        dump_raw : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.locations_get(
                location_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.locations_get(
            location_id,
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            has_geo=has_geo,
            parameter_id=parameter_id,
            parameter=parameter,
            unit=unit,
            coordinates=coordinates,
            radius=radius,
            country_id=country_id,
            country=country,
            city=city,
            location=location,
            order_by=order_by,
            is_mobile=is_mobile,
            is_analysis=is_analysis,
            source_name=source_name,
            entity=entity,
            sensor_type=sensor_type,
            model_name=model_name,
            manufacturer_name=manufacturer_name,
            dump_raw=dump_raw,
            request_options=request_options,
        )
        return _response.data

    async def mobilegentilejson(self, *, request_options: typing.Optional[RequestOptions] = None) -> TileJson:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TileJson
            Return a tilejson

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.mobilegentilejson()


        asyncio.run(main())
        """
        _response = await self._raw_client.mobilegentilejson(request_options=request_options)
        return _response.data

    async def get_mobilegentile(
        self,
        z: int,
        x: int,
        y: int,
        *,
        parameter: typing.Optional[GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestParameter] = None,
        location: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        last_updated_from: typing.Optional[
            GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedFrom
        ] = None,
        last_updated_to: typing.Optional[
            GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedTo
        ] = None,
        is_mobile: typing.Optional[bool] = None,
        project: typing.Optional[int] = None,
        is_analysis: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        z : int

        x : int

        y : int

        parameter : typing.Optional[GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestParameter]

        location : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            limit data to location id

        last_updated_from : typing.Optional[GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedFrom]

        last_updated_to : typing.Optional[GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedTo]

        is_mobile : typing.Optional[bool]

        project : typing.Optional[int]

        is_analysis : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.get_mobilegentile(
                z=1,
                x=1,
                y=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mobilegentile(
            z,
            x,
            y,
            parameter=parameter,
            location=location,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            is_mobile=is_mobile,
            project=project,
            is_analysis=is_analysis,
            request_options=request_options,
        )
        return _response.data

    async def mobiletilejson(self, *, request_options: typing.Optional[RequestOptions] = None) -> TileJson:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TileJson
            Return a tilejson

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.mobiletilejson()


        asyncio.run(main())
        """
        _response = await self._raw_client.mobiletilejson(request_options=request_options)
        return _response.data

    async def get_mobiletile(
        self,
        z: int,
        x: int,
        y: int,
        *,
        date_from: GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateFrom,
        date_to: GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateTo,
        parameter: typing.Optional[GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestParameter] = None,
        location: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        last_updated_from: typing.Optional[GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedFrom] = None,
        last_updated_to: typing.Optional[GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedTo] = None,
        is_mobile: typing.Optional[bool] = None,
        project: typing.Optional[int] = None,
        is_analysis: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        z : int

        x : int

        y : int

        date_from : GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateFrom

        date_to : GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateTo

        parameter : typing.Optional[GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestParameter]

        location : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            limit data to location id

        last_updated_from : typing.Optional[GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedFrom]

        last_updated_to : typing.Optional[GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedTo]

        is_mobile : typing.Optional[bool]

        project : typing.Optional[int]

        is_analysis : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.get_mobiletile(
                z=1,
                x=1,
                y=1,
                date_from=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                date_to=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mobiletile(
            z,
            x,
            y,
            date_from=date_from,
            date_to=date_to,
            parameter=parameter,
            location=location,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            is_mobile=is_mobile,
            project=project,
            is_analysis=is_analysis,
            request_options=request_options,
        )
        return _response.data

    async def tilejson(self, *, request_options: typing.Optional[RequestOptions] = None) -> TileJson:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TileJson
            Return a tilejson

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.tilejson()


        asyncio.run(main())
        """
        _response = await self._raw_client.tilejson(request_options=request_options)
        return _response.data

    async def demo(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.demo()


        asyncio.run(main())
        """
        _response = await self._raw_client.demo(request_options=request_options)
        return _response.data

    async def get_tile(
        self,
        z: int,
        x: int,
        y: int,
        *,
        parameter: typing.Optional[GetTileV2LocationsTilesZxyPbfGetRequestParameter] = None,
        location: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        last_updated_from: typing.Optional[GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedFrom] = None,
        last_updated_to: typing.Optional[GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedTo] = None,
        is_mobile: typing.Optional[bool] = None,
        project: typing.Optional[int] = None,
        is_analysis: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        z : int

        x : int

        y : int

        parameter : typing.Optional[GetTileV2LocationsTilesZxyPbfGetRequestParameter]

        location : typing.Optional[typing.Union[int, typing.Sequence[int]]]
            limit data to location id

        last_updated_from : typing.Optional[GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedFrom]

        last_updated_to : typing.Optional[GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedTo]

        is_mobile : typing.Optional[bool]

        project : typing.Optional[int]

        is_analysis : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.get_tile(
                z=1,
                x=1,
                y=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tile(
            z,
            x,
            y,
            parameter=parameter,
            location=location,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            is_mobile=is_mobile,
            project=project,
            is_analysis=is_analysis,
            request_options=request_options,
        )
        return _response.data

    async def mfr_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> OpenAqResult:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.mfr_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.mfr_get(request_options=request_options)
        return _response.data

    async def measurements_get(
        self,
        *,
        format: typing.Optional[str] = None,
        date_from: typing.Optional[MeasurementsGetV2MeasurementsGetRequestDateFrom] = None,
        date_to: typing.Optional[MeasurementsGetV2MeasurementsGetRequestDateTo] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        has_geo: typing.Optional[bool] = None,
        parameter_id: typing.Optional[int] = None,
        parameter: typing.Optional[
            typing.Union[
                MeasurementsGetV2MeasurementsGetRequestParameterItem,
                typing.Sequence[MeasurementsGetV2MeasurementsGetRequestParameterItem],
            ]
        ] = None,
        unit: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        coordinates: typing.Optional[str] = None,
        radius: typing.Optional[int] = None,
        country_id: typing.Optional[str] = None,
        country: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        city: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location_id: typing.Optional[int] = None,
        location: typing.Optional[
            typing.Union[
                MeasurementsGetV2MeasurementsGetRequestLocationItem,
                typing.Sequence[MeasurementsGetV2MeasurementsGetRequestLocationItem],
            ]
        ] = None,
        order_by: typing.Optional[MeasOrder] = None,
        is_mobile: typing.Optional[bool] = None,
        is_analysis: typing.Optional[bool] = None,
        project: typing.Optional[int] = None,
        entity: typing.Optional[EntityTypes] = None,
        sensor_type: typing.Optional[SensorTypes] = None,
        value_from: typing.Optional[float] = None,
        value_to: typing.Optional[float] = None,
        include_fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        format : typing.Optional[str]

        date_from : typing.Optional[MeasurementsGetV2MeasurementsGetRequestDateFrom]

        date_to : typing.Optional[MeasurementsGetV2MeasurementsGetRequestDateTo]

        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]

        has_geo : typing.Optional[bool]

        parameter_id : typing.Optional[int]

        parameter : typing.Optional[typing.Union[MeasurementsGetV2MeasurementsGetRequestParameterItem, typing.Sequence[MeasurementsGetV2MeasurementsGetRequestParameterItem]]]

        unit : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        coordinates : typing.Optional[str]

        radius : typing.Optional[int]

        country_id : typing.Optional[str]

                    Limit results by a certain country using two letter country code.
                    (ex. /US)


        country : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain country using two letter country code.
                    (ex. ?country=US or ?country=US&country=MX)


        city : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain city or cities.
                    (ex. ?city=Chicago or ?city=Chicago&city=Boston)


        location_id : typing.Optional[int]

        location : typing.Optional[typing.Union[MeasurementsGetV2MeasurementsGetRequestLocationItem, typing.Sequence[MeasurementsGetV2MeasurementsGetRequestLocationItem]]]

        order_by : typing.Optional[MeasOrder]

        is_mobile : typing.Optional[bool]

        is_analysis : typing.Optional[bool]

        project : typing.Optional[int]

        entity : typing.Optional[EntityTypes]

        sensor_type : typing.Optional[SensorTypes]

        value_from : typing.Optional[float]

        value_to : typing.Optional[float]

        include_fields : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.measurements_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.measurements_get(
            format=format,
            date_from=date_from,
            date_to=date_to,
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            has_geo=has_geo,
            parameter_id=parameter_id,
            parameter=parameter,
            unit=unit,
            coordinates=coordinates,
            radius=radius,
            country_id=country_id,
            country=country,
            city=city,
            location_id=location_id,
            location=location,
            order_by=order_by,
            is_mobile=is_mobile,
            is_analysis=is_analysis,
            project=project,
            entity=entity,
            sensor_type=sensor_type,
            value_from=value_from,
            value_to=value_to,
            include_fields=include_fields,
            request_options=request_options,
        )
        return _response.data

    async def model_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> OpenAqResult:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.model_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.model_get(request_options=request_options)
        return _response.data

    async def parameters_get(
        self,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        source_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        source_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        source_slug: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAqParametersResult:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]
            Define sort order.

        source_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        source_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        source_slug : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        order_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqParametersResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.parameters_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.parameters_get(
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            source_name=source_name,
            source_id=source_id,
            source_slug=source_slug,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    async def projects_get(
        self,
        project_id: int,
        *,
        country_id: typing.Optional[str] = None,
        country: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        parameter_id: typing.Optional[int] = None,
        parameter: typing.Optional[
            typing.Union[
                ProjectsGetV2ProjectsProjectIdGetRequestParameterItem,
                typing.Sequence[ProjectsGetV2ProjectsProjectIdGetRequestParameterItem],
            ]
        ] = None,
        unit: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        project: typing.Optional[
            typing.Union[
                ProjectsGetV2ProjectsProjectIdGetRequestProjectItem,
                typing.Sequence[ProjectsGetV2ProjectsProjectIdGetRequestProjectItem],
            ]
        ] = None,
        order_by: typing.Optional[ProjectsOrder] = None,
        is_mobile: typing.Optional[bool] = None,
        is_analysis: typing.Optional[bool] = None,
        entity: typing.Optional[str] = None,
        sensor_type: typing.Optional[str] = None,
        source_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAqProjectsResult:
        """
        Parameters
        ----------
        project_id : int

        country_id : typing.Optional[str]

                    Limit results by a certain country using two letter country code.
                    (ex. /US)


        country : typing.Optional[typing.Union[str, typing.Sequence[str]]]

                    Limit results by a certain country using two letter country code.
                    (ex. ?country=US or ?country=US&country=MX)


        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]
            Define sort order.

        parameter_id : typing.Optional[int]

        parameter : typing.Optional[typing.Union[ProjectsGetV2ProjectsProjectIdGetRequestParameterItem, typing.Sequence[ProjectsGetV2ProjectsProjectIdGetRequestParameterItem]]]

        unit : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        project : typing.Optional[typing.Union[ProjectsGetV2ProjectsProjectIdGetRequestProjectItem, typing.Sequence[ProjectsGetV2ProjectsProjectIdGetRequestProjectItem]]]

        order_by : typing.Optional[ProjectsOrder]

        is_mobile : typing.Optional[bool]

        is_analysis : typing.Optional[bool]

        entity : typing.Optional[str]

        sensor_type : typing.Optional[str]

        source_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqProjectsResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.projects_get(
                project_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.projects_get(
            project_id,
            country_id=country_id,
            country=country,
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            parameter_id=parameter_id,
            parameter=parameter,
            unit=unit,
            project=project,
            order_by=order_by,
            is_mobile=is_mobile,
            is_analysis=is_analysis,
            entity=entity,
            sensor_type=sensor_type,
            source_name=source_name,
            request_options=request_options,
        )
        return _response.data

    async def sources_get(
        self,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        source_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        source_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        source_slug: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[SourcesOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OpenAqResult:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]
            Define sort order.

        source_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        source_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        source_slug : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        order_by : typing.Optional[SourcesOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.sources_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.sources_get(
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            source_name=source_name,
            source_id=source_id,
            source_slug=source_slug,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    async def readme_get(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.readme_get(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.readme_get(slug, request_options=request_options)
        return _response.data

    async def summary_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> OpenAqResult:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OpenAqResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v2.summary_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.summary_get(request_options=request_options)
        return _response.data
