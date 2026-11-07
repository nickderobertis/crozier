

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
from ..types.cities_order import CitiesOrder
from ..types.countries_order import CountriesOrder
from ..types.entity_types import EntityTypes
from ..types.http_validation_error import HttpValidationError
from ..types.locations_order import LocationsOrder
from ..types.meas_order import MeasOrder
from ..types.measurements_get_v1v1measurements_get_request_date_from import (
    MeasurementsGetV1V1MeasurementsGetRequestDateFrom,
)
from ..types.measurements_get_v1v1measurements_get_request_date_to import (
    MeasurementsGetV1V1MeasurementsGetRequestDateTo,
)
from ..types.open_aq_cities_result import OpenAqCitiesResult
from ..types.open_aq_countries_result import OpenAqCountriesResult
from ..types.open_aq_parameters_result import OpenAqParametersResult
from ..types.open_aq_result import OpenAqResult
from ..types.sensor_types import SensorTypes
from ..types.sort import Sort
from ..types.sources_v1order import SourcesV1Order
from .types.latest_v1get_v1latest_location_id_get_request_location_item import (
    LatestV1GetV1LatestLocationIdGetRequestLocationItem,
)
from .types.latest_v1get_v1latest_location_id_get_request_parameter_item import (
    LatestV1GetV1LatestLocationIdGetRequestParameterItem,
)
from .types.locationsv1get_v1locations_location_id_get_request_location_item import (
    Locationsv1GetV1LocationsLocationIdGetRequestLocationItem,
)
from .types.locationsv1get_v1locations_location_id_get_request_parameter_item import (
    Locationsv1GetV1LocationsLocationIdGetRequestParameterItem,
)
from .types.measurements_get_v1v1measurements_get_request_location_item import (
    MeasurementsGetV1V1MeasurementsGetRequestLocationItem,
)
from .types.measurements_get_v1v1measurements_get_request_parameter_item import (
    MeasurementsGetV1V1MeasurementsGetRequestParameterItem,
)
from pydantic import ValidationError


class RawV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def cities_getv1(
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
            "v1/cities",
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

    def countries_getv1(
        self,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        country_id: typing.Optional[str] = None,
        country: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[CountriesOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OpenAqCountriesResult]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

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


        order_by : typing.Optional[CountriesOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OpenAqCountriesResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/countries",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "country_id": country_id,
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
            f"v1/countries/{encode_path_param(country_id)}",
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

    def latest_v1get(
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
                LatestV1GetV1LatestLocationIdGetRequestParameterItem,
                typing.Sequence[LatestV1GetV1LatestLocationIdGetRequestParameterItem],
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
                LatestV1GetV1LatestLocationIdGetRequestLocationItem,
                typing.Sequence[LatestV1GetV1LatestLocationIdGetRequestLocationItem],
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

        parameter : typing.Optional[typing.Union[LatestV1GetV1LatestLocationIdGetRequestParameterItem, typing.Sequence[LatestV1GetV1LatestLocationIdGetRequestParameterItem]]]

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


        location : typing.Optional[typing.Union[LatestV1GetV1LatestLocationIdGetRequestLocationItem, typing.Sequence[LatestV1GetV1LatestLocationIdGetRequestLocationItem]]]

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
            f"v1/latest/{encode_path_param(location_id)}",
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

    def locationsv1get(
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
                Locationsv1GetV1LocationsLocationIdGetRequestParameterItem,
                typing.Sequence[Locationsv1GetV1LocationsLocationIdGetRequestParameterItem],
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
                Locationsv1GetV1LocationsLocationIdGetRequestLocationItem,
                typing.Sequence[Locationsv1GetV1LocationsLocationIdGetRequestLocationItem],
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

        parameter : typing.Optional[typing.Union[Locationsv1GetV1LocationsLocationIdGetRequestParameterItem, typing.Sequence[Locationsv1GetV1LocationsLocationIdGetRequestParameterItem]]]

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


        location : typing.Optional[typing.Union[Locationsv1GetV1LocationsLocationIdGetRequestLocationItem, typing.Sequence[Locationsv1GetV1LocationsLocationIdGetRequestLocationItem]]]

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
            f"v1/locations/{encode_path_param(location_id)}",
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

    def measurements_get_v1(
        self,
        *,
        format: typing.Optional[str] = None,
        date_from: typing.Optional[MeasurementsGetV1V1MeasurementsGetRequestDateFrom] = None,
        date_to: typing.Optional[MeasurementsGetV1V1MeasurementsGetRequestDateTo] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        has_geo: typing.Optional[bool] = None,
        parameter_id: typing.Optional[int] = None,
        parameter: typing.Optional[
            typing.Union[
                MeasurementsGetV1V1MeasurementsGetRequestParameterItem,
                typing.Sequence[MeasurementsGetV1V1MeasurementsGetRequestParameterItem],
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
                MeasurementsGetV1V1MeasurementsGetRequestLocationItem,
                typing.Sequence[MeasurementsGetV1V1MeasurementsGetRequestLocationItem],
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

        date_from : typing.Optional[MeasurementsGetV1V1MeasurementsGetRequestDateFrom]

        date_to : typing.Optional[MeasurementsGetV1V1MeasurementsGetRequestDateTo]

        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]

        has_geo : typing.Optional[bool]

        parameter_id : typing.Optional[int]

        parameter : typing.Optional[typing.Union[MeasurementsGetV1V1MeasurementsGetRequestParameterItem, typing.Sequence[MeasurementsGetV1V1MeasurementsGetRequestParameterItem]]]

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

        location : typing.Optional[typing.Union[MeasurementsGetV1V1MeasurementsGetRequestLocationItem, typing.Sequence[MeasurementsGetV1V1MeasurementsGetRequestLocationItem]]]

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
            "v1/measurements",
            method="GET",
            params={
                "format": format,
                "date_from": convert_and_respect_annotation_metadata(
                    object_=date_from, annotation=MeasurementsGetV1V1MeasurementsGetRequestDateFrom, direction="write"
                ),
                "date_to": convert_and_respect_annotation_metadata(
                    object_=date_to, annotation=MeasurementsGetV1V1MeasurementsGetRequestDateTo, direction="write"
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

    def parameters_getv1(
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
            "v1/parameters",
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

    def sources_v1get(
        self,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        name: typing.Optional[str] = None,
        order_by: typing.Optional[SourcesV1Order] = None,
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

        name : typing.Optional[str]

        order_by : typing.Optional[SourcesV1Order]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OpenAqResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sources",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "name": name,
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


class AsyncRawV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def cities_getv1(
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
            "v1/cities",
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

    async def countries_getv1(
        self,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        country_id: typing.Optional[str] = None,
        country: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        order_by: typing.Optional[CountriesOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OpenAqCountriesResult]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

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


        order_by : typing.Optional[CountriesOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OpenAqCountriesResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/countries",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "country_id": country_id,
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
            f"v1/countries/{encode_path_param(country_id)}",
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

    async def latest_v1get(
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
                LatestV1GetV1LatestLocationIdGetRequestParameterItem,
                typing.Sequence[LatestV1GetV1LatestLocationIdGetRequestParameterItem],
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
                LatestV1GetV1LatestLocationIdGetRequestLocationItem,
                typing.Sequence[LatestV1GetV1LatestLocationIdGetRequestLocationItem],
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

        parameter : typing.Optional[typing.Union[LatestV1GetV1LatestLocationIdGetRequestParameterItem, typing.Sequence[LatestV1GetV1LatestLocationIdGetRequestParameterItem]]]

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


        location : typing.Optional[typing.Union[LatestV1GetV1LatestLocationIdGetRequestLocationItem, typing.Sequence[LatestV1GetV1LatestLocationIdGetRequestLocationItem]]]

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
            f"v1/latest/{encode_path_param(location_id)}",
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

    async def locationsv1get(
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
                Locationsv1GetV1LocationsLocationIdGetRequestParameterItem,
                typing.Sequence[Locationsv1GetV1LocationsLocationIdGetRequestParameterItem],
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
                Locationsv1GetV1LocationsLocationIdGetRequestLocationItem,
                typing.Sequence[Locationsv1GetV1LocationsLocationIdGetRequestLocationItem],
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

        parameter : typing.Optional[typing.Union[Locationsv1GetV1LocationsLocationIdGetRequestParameterItem, typing.Sequence[Locationsv1GetV1LocationsLocationIdGetRequestParameterItem]]]

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


        location : typing.Optional[typing.Union[Locationsv1GetV1LocationsLocationIdGetRequestLocationItem, typing.Sequence[Locationsv1GetV1LocationsLocationIdGetRequestLocationItem]]]

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
            f"v1/locations/{encode_path_param(location_id)}",
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

    async def measurements_get_v1(
        self,
        *,
        format: typing.Optional[str] = None,
        date_from: typing.Optional[MeasurementsGetV1V1MeasurementsGetRequestDateFrom] = None,
        date_to: typing.Optional[MeasurementsGetV1V1MeasurementsGetRequestDateTo] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        has_geo: typing.Optional[bool] = None,
        parameter_id: typing.Optional[int] = None,
        parameter: typing.Optional[
            typing.Union[
                MeasurementsGetV1V1MeasurementsGetRequestParameterItem,
                typing.Sequence[MeasurementsGetV1V1MeasurementsGetRequestParameterItem],
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
                MeasurementsGetV1V1MeasurementsGetRequestLocationItem,
                typing.Sequence[MeasurementsGetV1V1MeasurementsGetRequestLocationItem],
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

        date_from : typing.Optional[MeasurementsGetV1V1MeasurementsGetRequestDateFrom]

        date_to : typing.Optional[MeasurementsGetV1V1MeasurementsGetRequestDateTo]

        limit : typing.Optional[int]
            Change the number of results returned.

        page : typing.Optional[int]
            Paginate through results.

        offset : typing.Optional[int]

        sort : typing.Optional[Sort]

        has_geo : typing.Optional[bool]

        parameter_id : typing.Optional[int]

        parameter : typing.Optional[typing.Union[MeasurementsGetV1V1MeasurementsGetRequestParameterItem, typing.Sequence[MeasurementsGetV1V1MeasurementsGetRequestParameterItem]]]

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

        location : typing.Optional[typing.Union[MeasurementsGetV1V1MeasurementsGetRequestLocationItem, typing.Sequence[MeasurementsGetV1V1MeasurementsGetRequestLocationItem]]]

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
            "v1/measurements",
            method="GET",
            params={
                "format": format,
                "date_from": convert_and_respect_annotation_metadata(
                    object_=date_from, annotation=MeasurementsGetV1V1MeasurementsGetRequestDateFrom, direction="write"
                ),
                "date_to": convert_and_respect_annotation_metadata(
                    object_=date_to, annotation=MeasurementsGetV1V1MeasurementsGetRequestDateTo, direction="write"
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

    async def parameters_getv1(
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
            "v1/parameters",
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

    async def sources_v1get(
        self,
        *,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[Sort] = None,
        name: typing.Optional[str] = None,
        order_by: typing.Optional[SourcesV1Order] = None,
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

        name : typing.Optional[str]

        order_by : typing.Optional[SourcesV1Order]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OpenAqResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sources",
            method="GET",
            params={
                "limit": limit,
                "page": page,
                "offset": offset,
                "sort": sort,
                "name": name,
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
