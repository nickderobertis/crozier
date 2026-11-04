

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cities_order import CitiesOrder
from ..types.countries_order import CountriesOrder
from ..types.entity_types import EntityTypes
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
from .raw_client import AsyncRawV1Client, RawV1Client
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


class V1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawV1Client
        """
        return self._raw_client

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
        client.v1.cities_getv1()
        """
        _response = self._raw_client.cities_getv1(
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
    ) -> OpenAqCountriesResult:
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
        OpenAqCountriesResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v1.countries_getv1()
        """
        _response = self._raw_client.countries_getv1(
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            country_id=country_id,
            country=country,
            order_by=order_by,
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
        client.v1.countries_get(
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
        OpenAqResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v1.latest_v1get(
            location_id=1,
        )
        """
        _response = self._raw_client.latest_v1get(
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
        OpenAqResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v1.locationsv1get(
            location_id=1,
        )
        """
        _response = self._raw_client.locationsv1get(
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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.v1.measurements_get_v1()
        """
        _response = self._raw_client.measurements_get_v1(
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
        client.v1.parameters_getv1()
        """
        _response = self._raw_client.parameters_getv1(
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

        name : typing.Optional[str]

        order_by : typing.Optional[SourcesV1Order]

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
        client.v1.sources_v1get()
        """
        _response = self._raw_client.sources_v1get(
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            name=name,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data


class AsyncV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawV1Client
        """
        return self._raw_client

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
            await client.v1.cities_getv1()


        asyncio.run(main())
        """
        _response = await self._raw_client.cities_getv1(
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
    ) -> OpenAqCountriesResult:
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
        OpenAqCountriesResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v1.countries_getv1()


        asyncio.run(main())
        """
        _response = await self._raw_client.countries_getv1(
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            country_id=country_id,
            country=country,
            order_by=order_by,
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
            await client.v1.countries_get(
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
        OpenAqResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v1.latest_v1get(
                location_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.latest_v1get(
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
        OpenAqResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v1.locationsv1get(
                location_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.locationsv1get(
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
    ) -> typing.Any:
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
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.v1.measurements_get_v1()


        asyncio.run(main())
        """
        _response = await self._raw_client.measurements_get_v1(
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
            await client.v1.parameters_getv1()


        asyncio.run(main())
        """
        _response = await self._raw_client.parameters_getv1(
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

        name : typing.Optional[str]

        order_by : typing.Optional[SourcesV1Order]

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
            await client.v1.sources_v1get()


        asyncio.run(main())
        """
        _response = await self._raw_client.sources_v1get(
            limit=limit,
            page=page,
            offset=offset,
            sort=sort,
            name=name,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data
