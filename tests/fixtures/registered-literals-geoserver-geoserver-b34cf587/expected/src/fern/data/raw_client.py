

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
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.bbox import Bbox
from ..types.bbox_crs import BboxCrs
from ..types.crs import Crs
from ..types.datetime import Datetime
from ..types.exception import Exception
from ..types.feature_collection_geo_json import FeatureCollectionGeoJson
from ..types.feature_geo_json import FeatureGeoJson
from ..types.filter import Filter
from ..types.filter_crs import FilterCrs
from ..types.filter_lang import FilterLang
from ..types.ids import Ids
from ..types.limit import Limit
from ..types.sort_by import SortBy
from .types.get_features_request_filter_lang import GetFeaturesRequestFilterLang
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_features(
        self,
        collection_id: str,
        *,
        limit: typing.Optional[int] = None,
        bbox: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        datetime: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_lang: typing.Optional[GetFeaturesRequestFilterLang] = None,
        filter_crs: typing.Optional[str] = None,
        sortby: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        crs: typing.Optional[str] = None,
        bbox_crs: typing.Optional[str] = None,
        properties: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_properties: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        other_parameters: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeatureCollectionGeoJson]:
        """
        Fetch features of the feature collection with id `collectionId`.

        Every feature in a dataset belongs to a collection. A dataset may
        consist of multiple feature collections. A feature collection is often a
        collection of features of a similar type, based on a common schema.

        Use content negotiation to request HTML or GeoJSON.

        Parameters
        ----------
        collection_id : str
            local identifier of a collection

        limit : typing.Optional[int]
            The optional limit parameter limits the number of items that are presented in the response document.

            Only items are counted that are on the first level of the collection in the response document.
            Nested objects contained within the explicitly requested items shall not be counted.

            Minimum = 1. Maximum = 10000. Default = 10.

        bbox : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            Only features that have a geometry that intersects the bounding box are selected.
            The bounding box is provided as four or six numbers, depending on whether the
            coordinate reference system includes a vertical axis (height or depth):

            * Lower left corner, coordinate axis 1
            * Lower left corner, coordinate axis 2
            * Minimum value, coordinate axis 3 (optional)
            * Upper right corner, coordinate axis 1
            * Upper right corner, coordinate axis 2
            * Maximum value, coordinate axis 3 (optional)

            The coordinate reference system of the values is WGS 84 longitude/latitude
            (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate
            reference system is specified in the parameter `bbox-crs`.

            For WGS 84 longitude/latitude the values are in most cases the sequence of
            minimum longitude, minimum latitude, maximum longitude and maximum latitude.
            However, in cases where the box spans the antimeridian the first value
            (west-most box edge) is larger than the third value (east-most box edge).

            If the vertical axis is included, the third and the sixth number are
            the bottom and the top of the 3-dimensional bounding box.

            If a feature has multiple spatial geometry properties, it is the decision of the
            server whether only a single spatial geometry property is used to determine
            the extent or all relevant geometries.

        datetime : typing.Optional[str]
            Either a date-time or an interval, open or closed. Date and time expressions
            adhere to RFC 3339. Open intervals are expressed using double-dots.

            Examples:

            * A date-time: "2018-02-12T23:20:50Z"
            * A closed interval: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z"
            * Open intervals: "2018-02-12T00:00:00Z/.." or "../2018-03-18T12:31:12Z"

            Only features that have a temporal property that intersects the value of
            `datetime` are selected.

            If a feature has multiple temporal properties, it is the decision of the
            server whether only a single temporal property is used to determine
            the extent or all relevant temporal properties.

        filter : typing.Optional[str]
            Defines a filter that will be applied on items, only items matching the filter will be returned

        filter_lang : typing.Optional[GetFeaturesRequestFilterLang]
            Filter encoding used in the filter parameter

        filter_crs : typing.Optional[str]
            Filter CRS which is being used to encode geometries in the filter parameter

        sortby : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Defines how features in a response should be ordered for presentation.

        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Query multiple items by ID.

            WARNING:

            The parameter is part of the draft proposal "Query by IDs". The syntax and semantic of the
            parameter is subject to change in a future release. Its usage should be carefully considered.

        crs : typing.Optional[str]

        bbox_crs : typing.Optional[str]

        properties : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        exclude_properties : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        other_parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Allows unrecognized parameters to be added in the query string without getting a 400 back (e.g., cache busters)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeatureCollectionGeoJson]
            The response is a document consisting of features in the collection.
            The features included in the response are determined by the server
            based on the query parameters of the request. To support access to
            larger collections without overloading the client, the API supports
            paged access with links to the next page, if more features are selected
            that the page size.

            The `bbox` and `datetime` parameter can be used to select only a
            subset of the features in the collection (the features that are in the
            bounding box or time interval). The `bbox` parameter matches all features
            in the collection that are not associated with a location, too. The
            `datetime` parameter matches all features in the collection that are
            not associated with a time stamp or interval, too.

            The `limit` parameter may be used to control the subset of the
            selected features that should be returned in the response, the page size.
            Each page may include information about the number of selected and
            returned features (`numberMatched` and `numberReturned`) as well as
            links to support paging (link relation `next`).
        """
        _response = self._client_wrapper.httpx_client.request(
            f"collections/{encode_path_param(collection_id)}/items",
            method="GET",
            params={
                "limit": limit,
                "bbox": ",".join(map(str, bbox)) if isinstance(bbox, (list, tuple, set)) else bbox,
                "datetime": datetime,
                "filter": filter,
                "filter-lang": filter_lang,
                "filter-crs": filter_crs,
                "sortby": ",".join(map(str, sortby)) if isinstance(sortby, (list, tuple, set)) else sortby,
                "ids": ",".join(map(str, ids)) if isinstance(ids, (list, tuple, set)) else ids,
                "crs": crs,
                "bbox-crs": bbox_crs,
                "properties": ",".join(map(str, properties))
                if isinstance(properties, (list, tuple, set))
                else properties,
                "exclude-properties": ",".join(map(str, exclude_properties))
                if isinstance(exclude_properties, (list, tuple, set))
                else exclude_properties,
                "otherParameters": other_parameters,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeatureCollectionGeoJson,
                    parse_obj_as(
                        type_=FeatureCollectionGeoJson,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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

    def search_features(
        self,
        collection_id: str,
        *,
        limit: typing.Optional[Limit] = OMIT,
        bbox: typing.Optional[Bbox] = OMIT,
        bbox_crs: typing.Optional[BboxCrs] = OMIT,
        crs: typing.Optional[Crs] = OMIT,
        datetime: typing.Optional[Datetime] = OMIT,
        ids: typing.Optional[Ids] = OMIT,
        sort_by: typing.Optional[SortBy] = OMIT,
        filter: typing.Optional[Filter] = OMIT,
        filter_crs: typing.Optional[FilterCrs] = OMIT,
        filter_lang: typing.Optional[FilterLang] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeatureCollectionGeoJson]:
        """
        Retrieve items matching filters using POST.

        WARNING:

        This endpoint is part of the draft proposal "OGC API - Features - Part 5". The syntax and
        semantic of the endpoint is subject to change in a future release. Its usage should be
        carefully considered.

        Parameters
        ----------
        collection_id : str

        limit : typing.Optional[Limit]

        bbox : typing.Optional[Bbox]

        bbox_crs : typing.Optional[BboxCrs]

        crs : typing.Optional[Crs]

        datetime : typing.Optional[Datetime]

        ids : typing.Optional[Ids]

        sort_by : typing.Optional[SortBy]

        filter : typing.Optional[Filter]

        filter_crs : typing.Optional[FilterCrs]

        filter_lang : typing.Optional[FilterLang]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeatureCollectionGeoJson]
            The response is a document consisting of features in the collection.
            The features included in the response are determined by the server
            based on the query parameters of the request. To support access to
            larger collections without overloading the client, the API supports
            paged access with links to the next page, if more features are selected
            that the page size.

            The `bbox` and `datetime` parameter can be used to select only a
            subset of the features in the collection (the features that are in the
            bounding box or time interval). The `bbox` parameter matches all features
            in the collection that are not associated with a location, too. The
            `datetime` parameter matches all features in the collection that are
            not associated with a time stamp or interval, too.

            The `limit` parameter may be used to control the subset of the
            selected features that should be returned in the response, the page size.
            Each page may include information about the number of selected and
            returned features (`numberMatched` and `numberReturned`) as well as
            links to support paging (link relation `next`).
        """
        _response = self._client_wrapper.httpx_client.request(
            f"collections/{encode_path_param(collection_id)}/search",
            method="POST",
            json={
                "limit": limit,
                "bbox": bbox,
                "bboxCrs": bbox_crs,
                "crs": crs,
                "datetime": datetime,
                "ids": ids,
                "sortBy": sort_by,
                "filter": filter,
                "filterCrs": filter_crs,
                "filterLang": filter_lang,
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
                    FeatureCollectionGeoJson,
                    parse_obj_as(
                        type_=FeatureCollectionGeoJson,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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

    def get_feature(
        self,
        collection_id: str,
        feature_id: str,
        *,
        crs: typing.Optional[str] = None,
        properties: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_properties: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        other_parameters: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeatureGeoJson]:
        """
        Fetch the feature with id `featureId` in the feature collection
        with id `collectionId`.

        Use content negotiation to request HTML or GeoJSON.

        Parameters
        ----------
        collection_id : str
            local identifier of a collection

        feature_id : str
            local identifier of a feature

        crs : typing.Optional[str]

        properties : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        exclude_properties : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        other_parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Allows unrecognized parameters to be added in the query string without getting a 400 back (e.g., cache busters)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeatureGeoJson]
            fetch the feature with id `featureId` in the feature collection
            with id `collectionId`
        """
        _response = self._client_wrapper.httpx_client.request(
            f"collections/{encode_path_param(collection_id)}/items/{encode_path_param(feature_id)}",
            method="GET",
            params={
                "crs": crs,
                "properties": ",".join(map(str, properties))
                if isinstance(properties, (list, tuple, set))
                else properties,
                "exclude-properties": ",".join(map(str, exclude_properties))
                if isinstance(exclude_properties, (list, tuple, set))
                else exclude_properties,
                "otherParameters": other_parameters,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeatureGeoJson,
                    parse_obj_as(
                        type_=FeatureGeoJson,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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


class AsyncRawDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_features(
        self,
        collection_id: str,
        *,
        limit: typing.Optional[int] = None,
        bbox: typing.Optional[typing.Union[float, typing.Sequence[float]]] = None,
        datetime: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_lang: typing.Optional[GetFeaturesRequestFilterLang] = None,
        filter_crs: typing.Optional[str] = None,
        sortby: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        crs: typing.Optional[str] = None,
        bbox_crs: typing.Optional[str] = None,
        properties: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_properties: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        other_parameters: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeatureCollectionGeoJson]:
        """
        Fetch features of the feature collection with id `collectionId`.

        Every feature in a dataset belongs to a collection. A dataset may
        consist of multiple feature collections. A feature collection is often a
        collection of features of a similar type, based on a common schema.

        Use content negotiation to request HTML or GeoJSON.

        Parameters
        ----------
        collection_id : str
            local identifier of a collection

        limit : typing.Optional[int]
            The optional limit parameter limits the number of items that are presented in the response document.

            Only items are counted that are on the first level of the collection in the response document.
            Nested objects contained within the explicitly requested items shall not be counted.

            Minimum = 1. Maximum = 10000. Default = 10.

        bbox : typing.Optional[typing.Union[float, typing.Sequence[float]]]
            Only features that have a geometry that intersects the bounding box are selected.
            The bounding box is provided as four or six numbers, depending on whether the
            coordinate reference system includes a vertical axis (height or depth):

            * Lower left corner, coordinate axis 1
            * Lower left corner, coordinate axis 2
            * Minimum value, coordinate axis 3 (optional)
            * Upper right corner, coordinate axis 1
            * Upper right corner, coordinate axis 2
            * Maximum value, coordinate axis 3 (optional)

            The coordinate reference system of the values is WGS 84 longitude/latitude
            (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate
            reference system is specified in the parameter `bbox-crs`.

            For WGS 84 longitude/latitude the values are in most cases the sequence of
            minimum longitude, minimum latitude, maximum longitude and maximum latitude.
            However, in cases where the box spans the antimeridian the first value
            (west-most box edge) is larger than the third value (east-most box edge).

            If the vertical axis is included, the third and the sixth number are
            the bottom and the top of the 3-dimensional bounding box.

            If a feature has multiple spatial geometry properties, it is the decision of the
            server whether only a single spatial geometry property is used to determine
            the extent or all relevant geometries.

        datetime : typing.Optional[str]
            Either a date-time or an interval, open or closed. Date and time expressions
            adhere to RFC 3339. Open intervals are expressed using double-dots.

            Examples:

            * A date-time: "2018-02-12T23:20:50Z"
            * A closed interval: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z"
            * Open intervals: "2018-02-12T00:00:00Z/.." or "../2018-03-18T12:31:12Z"

            Only features that have a temporal property that intersects the value of
            `datetime` are selected.

            If a feature has multiple temporal properties, it is the decision of the
            server whether only a single temporal property is used to determine
            the extent or all relevant temporal properties.

        filter : typing.Optional[str]
            Defines a filter that will be applied on items, only items matching the filter will be returned

        filter_lang : typing.Optional[GetFeaturesRequestFilterLang]
            Filter encoding used in the filter parameter

        filter_crs : typing.Optional[str]
            Filter CRS which is being used to encode geometries in the filter parameter

        sortby : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Defines how features in a response should be ordered for presentation.

        ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Query multiple items by ID.

            WARNING:

            The parameter is part of the draft proposal "Query by IDs". The syntax and semantic of the
            parameter is subject to change in a future release. Its usage should be carefully considered.

        crs : typing.Optional[str]

        bbox_crs : typing.Optional[str]

        properties : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        exclude_properties : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        other_parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Allows unrecognized parameters to be added in the query string without getting a 400 back (e.g., cache busters)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeatureCollectionGeoJson]
            The response is a document consisting of features in the collection.
            The features included in the response are determined by the server
            based on the query parameters of the request. To support access to
            larger collections without overloading the client, the API supports
            paged access with links to the next page, if more features are selected
            that the page size.

            The `bbox` and `datetime` parameter can be used to select only a
            subset of the features in the collection (the features that are in the
            bounding box or time interval). The `bbox` parameter matches all features
            in the collection that are not associated with a location, too. The
            `datetime` parameter matches all features in the collection that are
            not associated with a time stamp or interval, too.

            The `limit` parameter may be used to control the subset of the
            selected features that should be returned in the response, the page size.
            Each page may include information about the number of selected and
            returned features (`numberMatched` and `numberReturned`) as well as
            links to support paging (link relation `next`).
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"collections/{encode_path_param(collection_id)}/items",
            method="GET",
            params={
                "limit": limit,
                "bbox": ",".join(map(str, bbox)) if isinstance(bbox, (list, tuple, set)) else bbox,
                "datetime": datetime,
                "filter": filter,
                "filter-lang": filter_lang,
                "filter-crs": filter_crs,
                "sortby": ",".join(map(str, sortby)) if isinstance(sortby, (list, tuple, set)) else sortby,
                "ids": ",".join(map(str, ids)) if isinstance(ids, (list, tuple, set)) else ids,
                "crs": crs,
                "bbox-crs": bbox_crs,
                "properties": ",".join(map(str, properties))
                if isinstance(properties, (list, tuple, set))
                else properties,
                "exclude-properties": ",".join(map(str, exclude_properties))
                if isinstance(exclude_properties, (list, tuple, set))
                else exclude_properties,
                "otherParameters": other_parameters,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeatureCollectionGeoJson,
                    parse_obj_as(
                        type_=FeatureCollectionGeoJson,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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

    async def search_features(
        self,
        collection_id: str,
        *,
        limit: typing.Optional[Limit] = OMIT,
        bbox: typing.Optional[Bbox] = OMIT,
        bbox_crs: typing.Optional[BboxCrs] = OMIT,
        crs: typing.Optional[Crs] = OMIT,
        datetime: typing.Optional[Datetime] = OMIT,
        ids: typing.Optional[Ids] = OMIT,
        sort_by: typing.Optional[SortBy] = OMIT,
        filter: typing.Optional[Filter] = OMIT,
        filter_crs: typing.Optional[FilterCrs] = OMIT,
        filter_lang: typing.Optional[FilterLang] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeatureCollectionGeoJson]:
        """
        Retrieve items matching filters using POST.

        WARNING:

        This endpoint is part of the draft proposal "OGC API - Features - Part 5". The syntax and
        semantic of the endpoint is subject to change in a future release. Its usage should be
        carefully considered.

        Parameters
        ----------
        collection_id : str

        limit : typing.Optional[Limit]

        bbox : typing.Optional[Bbox]

        bbox_crs : typing.Optional[BboxCrs]

        crs : typing.Optional[Crs]

        datetime : typing.Optional[Datetime]

        ids : typing.Optional[Ids]

        sort_by : typing.Optional[SortBy]

        filter : typing.Optional[Filter]

        filter_crs : typing.Optional[FilterCrs]

        filter_lang : typing.Optional[FilterLang]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeatureCollectionGeoJson]
            The response is a document consisting of features in the collection.
            The features included in the response are determined by the server
            based on the query parameters of the request. To support access to
            larger collections without overloading the client, the API supports
            paged access with links to the next page, if more features are selected
            that the page size.

            The `bbox` and `datetime` parameter can be used to select only a
            subset of the features in the collection (the features that are in the
            bounding box or time interval). The `bbox` parameter matches all features
            in the collection that are not associated with a location, too. The
            `datetime` parameter matches all features in the collection that are
            not associated with a time stamp or interval, too.

            The `limit` parameter may be used to control the subset of the
            selected features that should be returned in the response, the page size.
            Each page may include information about the number of selected and
            returned features (`numberMatched` and `numberReturned`) as well as
            links to support paging (link relation `next`).
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"collections/{encode_path_param(collection_id)}/search",
            method="POST",
            json={
                "limit": limit,
                "bbox": bbox,
                "bboxCrs": bbox_crs,
                "crs": crs,
                "datetime": datetime,
                "ids": ids,
                "sortBy": sort_by,
                "filter": filter,
                "filterCrs": filter_crs,
                "filterLang": filter_lang,
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
                    FeatureCollectionGeoJson,
                    parse_obj_as(
                        type_=FeatureCollectionGeoJson,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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

    async def get_feature(
        self,
        collection_id: str,
        feature_id: str,
        *,
        crs: typing.Optional[str] = None,
        properties: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_properties: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        other_parameters: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeatureGeoJson]:
        """
        Fetch the feature with id `featureId` in the feature collection
        with id `collectionId`.

        Use content negotiation to request HTML or GeoJSON.

        Parameters
        ----------
        collection_id : str
            local identifier of a collection

        feature_id : str
            local identifier of a feature

        crs : typing.Optional[str]

        properties : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        exclude_properties : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        other_parameters : typing.Optional[typing.Dict[str, typing.Any]]
            Allows unrecognized parameters to be added in the query string without getting a 400 back (e.g., cache busters)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeatureGeoJson]
            fetch the feature with id `featureId` in the feature collection
            with id `collectionId`
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"collections/{encode_path_param(collection_id)}/items/{encode_path_param(feature_id)}",
            method="GET",
            params={
                "crs": crs,
                "properties": ",".join(map(str, properties))
                if isinstance(properties, (list, tuple, set))
                else properties,
                "exclude-properties": ",".join(map(str, exclude_properties))
                if isinstance(exclude_properties, (list, tuple, set))
                else exclude_properties,
                "otherParameters": other_parameters,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeatureGeoJson,
                    parse_obj_as(
                        type_=FeatureGeoJson,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Exception,
                        parse_obj_as(
                            type_=Exception,
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
