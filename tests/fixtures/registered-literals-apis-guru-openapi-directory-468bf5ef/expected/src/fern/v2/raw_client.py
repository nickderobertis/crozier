

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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
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
from ..types.http_validation_error import HttpValidationError
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
from pydantic import ValidationError


class RawV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[OpenAqResult]:
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
        HttpResponse[OpenAqResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/averages",
            method="GET",
            params={
                "date_from": convert_and_respect_annotation_metadata(
                    object_=date_from, annotation=AveragesV2GetV2AveragesGetRequestDateFrom, direction="write"
                ),
                "date_to": convert_and_respect_annotation_metadata(
                    object_=date_to, annotation=AveragesV2GetV2AveragesGetRequestDateTo, direction="write"
                ),
                "parameter_id": parameter_id,
                "parameter": parameter,
                "unit": unit,
                "project_id": project_id,
                "project": project,
                "country_id": country_id,
                "country": country,
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "spatial": spatial,
                "temporal": temporal,
                "location": location,
                "group": group,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqResult,
                    parse_obj_as(
                        type_=OpenAqResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
    ) -> HttpResponse[OpenAqCitiesResult]:
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
        HttpResponse[OpenAqCitiesResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/cities",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "country_id": country_id,
                "country": country,
                "city": city,
                "order_by": order_by,
                "entity": entity,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqCitiesResult,
                    parse_obj_as(
                        type_=OpenAqCitiesResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
    ) -> HttpResponse[OpenAqCountriesResult]:
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
        HttpResponse[OpenAqCountriesResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/countries/{encode_path_param(country_id)}",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "country": country,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqCountriesResult,
                    parse_obj_as(
                        type_=OpenAqCountriesResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
    ) -> HttpResponse[OpenAqResult]:
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
        HttpResponse[OpenAqResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/latest/{encode_path_param(location_id)}",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "has_geo": has_geo,
                "parameter_id": parameter_id,
                "parameter": parameter,
                "unit": unit,
                "coordinates": coordinates,
                "radius": radius,
                "country_id": country_id,
                "country": country,
                "city": city,
                "location": location,
                "order_by": order_by,
                "isMobile": is_mobile,
                "isAnalysis": is_analysis,
                "sourceName": source_name,
                "entity": entity,
                "sensorType": sensor_type,
                "modelName": model_name,
                "manufacturerName": manufacturer_name,
                "dumpRaw": dump_raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqResult,
                    parse_obj_as(
                        type_=OpenAqResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
    ) -> HttpResponse[OpenAqResult]:
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
        HttpResponse[OpenAqResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "has_geo": has_geo,
                "parameter_id": parameter_id,
                "parameter": parameter,
                "unit": unit,
                "coordinates": coordinates,
                "radius": radius,
                "country_id": country_id,
                "country": country,
                "city": city,
                "location": location,
                "order_by": order_by,
                "isMobile": is_mobile,
                "isAnalysis": is_analysis,
                "sourceName": source_name,
                "entity": entity,
                "sensorType": sensor_type,
                "modelName": model_name,
                "manufacturerName": manufacturer_name,
                "dumpRaw": dump_raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqResult,
                    parse_obj_as(
                        type_=OpenAqResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def mobilegentilejson(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[TileJson]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TileJson]
            Return a tilejson
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/locations/tiles/mobile-generalized/tiles.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TileJson,
                    parse_obj_as(
                        type_=TileJson,
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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/tiles/mobile-generalized/{encode_path_param(z)}/{encode_path_param(x)}/{encode_path_param(y)}.pbf",
            method="GET",
            params={
                "parameter": parameter,
                "location": location,
                "lastUpdatedFrom": convert_and_respect_annotation_metadata(
                    object_=last_updated_from,
                    annotation=GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedFrom,
                    direction="write",
                ),
                "lastUpdatedTo": convert_and_respect_annotation_metadata(
                    object_=last_updated_to,
                    annotation=GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedTo,
                    direction="write",
                ),
                "isMobile": is_mobile,
                "project": project,
                "isAnalysis": is_analysis,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def mobiletilejson(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[TileJson]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TileJson]
            Return a tilejson
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/locations/tiles/mobile/tiles.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TileJson,
                    parse_obj_as(
                        type_=TileJson,
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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/tiles/mobile/{encode_path_param(z)}/{encode_path_param(x)}/{encode_path_param(y)}.pbf",
            method="GET",
            params={
                "dateFrom": convert_and_respect_annotation_metadata(
                    object_=date_from,
                    annotation=GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateFrom,
                    direction="write",
                ),
                "dateTo": convert_and_respect_annotation_metadata(
                    object_=date_to,
                    annotation=GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateTo,
                    direction="write",
                ),
                "parameter": parameter,
                "location": location,
                "lastUpdatedFrom": convert_and_respect_annotation_metadata(
                    object_=last_updated_from,
                    annotation=GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedFrom,
                    direction="write",
                ),
                "lastUpdatedTo": convert_and_respect_annotation_metadata(
                    object_=last_updated_to,
                    annotation=GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedTo,
                    direction="write",
                ),
                "isMobile": is_mobile,
                "project": project,
                "isAnalysis": is_analysis,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def tilejson(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[TileJson]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TileJson]
            Return a tilejson
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/locations/tiles/tiles.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TileJson,
                    parse_obj_as(
                        type_=TileJson,
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

    def demo(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/locations/tiles/viewer",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/locations/tiles/{encode_path_param(z)}/{encode_path_param(x)}/{encode_path_param(y)}.pbf",
            method="GET",
            params={
                "parameter": parameter,
                "location": location,
                "lastUpdatedFrom": convert_and_respect_annotation_metadata(
                    object_=last_updated_from,
                    annotation=GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedFrom,
                    direction="write",
                ),
                "lastUpdatedTo": convert_and_respect_annotation_metadata(
                    object_=last_updated_to,
                    annotation=GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedTo,
                    direction="write",
                ),
                "isMobile": is_mobile,
                "project": project,
                "isAnalysis": is_analysis,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def mfr_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[OpenAqResult]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OpenAqResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/manufacturers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqResult,
                    parse_obj_as(
                        type_=OpenAqResult,
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
    ) -> HttpResponse[typing.Any]:
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
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/measurements",
            method="GET",
            params={
                "format": format,
                "date_from": convert_and_respect_annotation_metadata(
                    object_=date_from, annotation=MeasurementsGetV2MeasurementsGetRequestDateFrom, direction="write"
                ),
                "date_to": convert_and_respect_annotation_metadata(
                    object_=date_to, annotation=MeasurementsGetV2MeasurementsGetRequestDateTo, direction="write"
                ),
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "has_geo": has_geo,
                "parameter_id": parameter_id,
                "parameter": parameter,
                "unit": unit,
                "coordinates": coordinates,
                "radius": radius,
                "country_id": country_id,
                "country": country,
                "city": city,
                "location_id": location_id,
                "location": location,
                "order_by": order_by,
                "isMobile": is_mobile,
                "isAnalysis": is_analysis,
                "project": project,
                "entity": entity,
                "sensorType": sensor_type,
                "value_from": value_from,
                "value_to": value_to,
                "include_fields": include_fields,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def model_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[OpenAqResult]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OpenAqResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/models",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqResult,
                    parse_obj_as(
                        type_=OpenAqResult,
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
    ) -> HttpResponse[OpenAqParametersResult]:
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
        HttpResponse[OpenAqParametersResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/parameters",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "sourceName": source_name,
                "sourceId": source_id,
                "sourceSlug": source_slug,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqParametersResult,
                    parse_obj_as(
                        type_=OpenAqParametersResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
    ) -> HttpResponse[OpenAqProjectsResult]:
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
        HttpResponse[OpenAqProjectsResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/projects/{encode_path_param(project_id)}",
            method="GET",
            params={
                "country_id": country_id,
                "country": country,
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "parameter_id": parameter_id,
                "parameter": parameter,
                "unit": unit,
                "project": project,
                "order_by": order_by,
                "isMobile": is_mobile,
                "isAnalysis": is_analysis,
                "entity": entity,
                "sensorType": sensor_type,
                "sourceName": source_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqProjectsResult,
                    parse_obj_as(
                        type_=OpenAqProjectsResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
    ) -> HttpResponse[OpenAqResult]:
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
        HttpResponse[OpenAqResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/sources",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "sourceName": source_name,
                "sourceId": source_id,
                "sourceSlug": source_slug,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqResult,
                    parse_obj_as(
                        type_=OpenAqResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def readme_get(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/sources/readme/{encode_path_param(slug)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def summary_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[OpenAqResult]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OpenAqResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/summary",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqResult,
                    parse_obj_as(
                        type_=OpenAqResult,
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


class AsyncRawV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[OpenAqResult]:
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
        AsyncHttpResponse[OpenAqResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/averages",
            method="GET",
            params={
                "date_from": convert_and_respect_annotation_metadata(
                    object_=date_from, annotation=AveragesV2GetV2AveragesGetRequestDateFrom, direction="write"
                ),
                "date_to": convert_and_respect_annotation_metadata(
                    object_=date_to, annotation=AveragesV2GetV2AveragesGetRequestDateTo, direction="write"
                ),
                "parameter_id": parameter_id,
                "parameter": parameter,
                "unit": unit,
                "project_id": project_id,
                "project": project,
                "country_id": country_id,
                "country": country,
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "spatial": spatial,
                "temporal": temporal,
                "location": location,
                "group": group,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqResult,
                    parse_obj_as(
                        type_=OpenAqResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
    ) -> AsyncHttpResponse[OpenAqCitiesResult]:
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
        AsyncHttpResponse[OpenAqCitiesResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/cities",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "country_id": country_id,
                "country": country,
                "city": city,
                "order_by": order_by,
                "entity": entity,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqCitiesResult,
                    parse_obj_as(
                        type_=OpenAqCitiesResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
    ) -> AsyncHttpResponse[OpenAqCountriesResult]:
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
        AsyncHttpResponse[OpenAqCountriesResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/countries/{encode_path_param(country_id)}",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "country": country,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqCountriesResult,
                    parse_obj_as(
                        type_=OpenAqCountriesResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
    ) -> AsyncHttpResponse[OpenAqResult]:
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
        AsyncHttpResponse[OpenAqResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/latest/{encode_path_param(location_id)}",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "has_geo": has_geo,
                "parameter_id": parameter_id,
                "parameter": parameter,
                "unit": unit,
                "coordinates": coordinates,
                "radius": radius,
                "country_id": country_id,
                "country": country,
                "city": city,
                "location": location,
                "order_by": order_by,
                "isMobile": is_mobile,
                "isAnalysis": is_analysis,
                "sourceName": source_name,
                "entity": entity,
                "sensorType": sensor_type,
                "modelName": model_name,
                "manufacturerName": manufacturer_name,
                "dumpRaw": dump_raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqResult,
                    parse_obj_as(
                        type_=OpenAqResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
    ) -> AsyncHttpResponse[OpenAqResult]:
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
        AsyncHttpResponse[OpenAqResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/{encode_path_param(location_id)}",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "has_geo": has_geo,
                "parameter_id": parameter_id,
                "parameter": parameter,
                "unit": unit,
                "coordinates": coordinates,
                "radius": radius,
                "country_id": country_id,
                "country": country,
                "city": city,
                "location": location,
                "order_by": order_by,
                "isMobile": is_mobile,
                "isAnalysis": is_analysis,
                "sourceName": source_name,
                "entity": entity,
                "sensorType": sensor_type,
                "modelName": model_name,
                "manufacturerName": manufacturer_name,
                "dumpRaw": dump_raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqResult,
                    parse_obj_as(
                        type_=OpenAqResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def mobilegentilejson(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TileJson]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TileJson]
            Return a tilejson
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/locations/tiles/mobile-generalized/tiles.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TileJson,
                    parse_obj_as(
                        type_=TileJson,
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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/tiles/mobile-generalized/{encode_path_param(z)}/{encode_path_param(x)}/{encode_path_param(y)}.pbf",
            method="GET",
            params={
                "parameter": parameter,
                "location": location,
                "lastUpdatedFrom": convert_and_respect_annotation_metadata(
                    object_=last_updated_from,
                    annotation=GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedFrom,
                    direction="write",
                ),
                "lastUpdatedTo": convert_and_respect_annotation_metadata(
                    object_=last_updated_to,
                    annotation=GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedTo,
                    direction="write",
                ),
                "isMobile": is_mobile,
                "project": project,
                "isAnalysis": is_analysis,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def mobiletilejson(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TileJson]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TileJson]
            Return a tilejson
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/locations/tiles/mobile/tiles.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TileJson,
                    parse_obj_as(
                        type_=TileJson,
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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/tiles/mobile/{encode_path_param(z)}/{encode_path_param(x)}/{encode_path_param(y)}.pbf",
            method="GET",
            params={
                "dateFrom": convert_and_respect_annotation_metadata(
                    object_=date_from,
                    annotation=GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateFrom,
                    direction="write",
                ),
                "dateTo": convert_and_respect_annotation_metadata(
                    object_=date_to,
                    annotation=GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateTo,
                    direction="write",
                ),
                "parameter": parameter,
                "location": location,
                "lastUpdatedFrom": convert_and_respect_annotation_metadata(
                    object_=last_updated_from,
                    annotation=GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedFrom,
                    direction="write",
                ),
                "lastUpdatedTo": convert_and_respect_annotation_metadata(
                    object_=last_updated_to,
                    annotation=GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedTo,
                    direction="write",
                ),
                "isMobile": is_mobile,
                "project": project,
                "isAnalysis": is_analysis,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def tilejson(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[TileJson]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TileJson]
            Return a tilejson
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/locations/tiles/tiles.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TileJson,
                    parse_obj_as(
                        type_=TileJson,
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

    async def demo(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/locations/tiles/viewer",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/locations/tiles/{encode_path_param(z)}/{encode_path_param(x)}/{encode_path_param(y)}.pbf",
            method="GET",
            params={
                "parameter": parameter,
                "location": location,
                "lastUpdatedFrom": convert_and_respect_annotation_metadata(
                    object_=last_updated_from,
                    annotation=GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedFrom,
                    direction="write",
                ),
                "lastUpdatedTo": convert_and_respect_annotation_metadata(
                    object_=last_updated_to,
                    annotation=GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedTo,
                    direction="write",
                ),
                "isMobile": is_mobile,
                "project": project,
                "isAnalysis": is_analysis,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def mfr_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OpenAqResult]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OpenAqResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/manufacturers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqResult,
                    parse_obj_as(
                        type_=OpenAqResult,
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
    ) -> AsyncHttpResponse[typing.Any]:
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
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/measurements",
            method="GET",
            params={
                "format": format,
                "date_from": convert_and_respect_annotation_metadata(
                    object_=date_from, annotation=MeasurementsGetV2MeasurementsGetRequestDateFrom, direction="write"
                ),
                "date_to": convert_and_respect_annotation_metadata(
                    object_=date_to, annotation=MeasurementsGetV2MeasurementsGetRequestDateTo, direction="write"
                ),
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "has_geo": has_geo,
                "parameter_id": parameter_id,
                "parameter": parameter,
                "unit": unit,
                "coordinates": coordinates,
                "radius": radius,
                "country_id": country_id,
                "country": country,
                "city": city,
                "location_id": location_id,
                "location": location,
                "order_by": order_by,
                "isMobile": is_mobile,
                "isAnalysis": is_analysis,
                "project": project,
                "entity": entity,
                "sensorType": sensor_type,
                "value_from": value_from,
                "value_to": value_to,
                "include_fields": include_fields,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def model_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OpenAqResult]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OpenAqResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/models",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqResult,
                    parse_obj_as(
                        type_=OpenAqResult,
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
    ) -> AsyncHttpResponse[OpenAqParametersResult]:
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
        AsyncHttpResponse[OpenAqParametersResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/parameters",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "sourceName": source_name,
                "sourceId": source_id,
                "sourceSlug": source_slug,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqParametersResult,
                    parse_obj_as(
                        type_=OpenAqParametersResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
    ) -> AsyncHttpResponse[OpenAqProjectsResult]:
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
        AsyncHttpResponse[OpenAqProjectsResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/projects/{encode_path_param(project_id)}",
            method="GET",
            params={
                "country_id": country_id,
                "country": country,
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "parameter_id": parameter_id,
                "parameter": parameter,
                "unit": unit,
                "project": project,
                "order_by": order_by,
                "isMobile": is_mobile,
                "isAnalysis": is_analysis,
                "entity": entity,
                "sensorType": sensor_type,
                "sourceName": source_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqProjectsResult,
                    parse_obj_as(
                        type_=OpenAqProjectsResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
    ) -> AsyncHttpResponse[OpenAqResult]:
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
        AsyncHttpResponse[OpenAqResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/sources",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "sourceName": source_name,
                "sourceId": source_id,
                "sourceSlug": source_slug,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqResult,
                    parse_obj_as(
                        type_=OpenAqResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def readme_get(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/sources/readme/{encode_path_param(slug)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def summary_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OpenAqResult]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OpenAqResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/summary",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OpenAqResult,
                    parse_obj_as(
                        type_=OpenAqResult,
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
