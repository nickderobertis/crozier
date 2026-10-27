

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
from ..types.collections import Collections
from ..types.conformance import Conformance
from ..types.http_validation_error import HttpValidationError
from ..types.item_collection_output import ItemCollectionOutput
from ..types.landing_page import LandingPage
from ..types.post_fields_extension import PostFieldsExtension
from ..types.search_post_request_filter_lang import SearchPostRequestFilterLang
from ..types.search_post_request_intersects import SearchPostRequestIntersects
from ..types.sort_extension import SortExtension
from ..types.stac_pydantic_api_collection_collection import StacPydanticApiCollectionCollection
from ..types.stac_pydantic_api_item_item import StacPydanticApiItemItem
from .types.get_collections_catalog_collections_get_request_filter_lang import (
    GetCollectionsCatalogCollectionsGetRequestFilterLang,
)
from .types.get_item_collection_catalog_collections_collection_id_items_get_request_filter_lang import (
    GetItemCollectionCatalogCollectionsCollectionIdItemsGetRequestFilterLang,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCatalogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def landing_page(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[LandingPage]:
        """
        Endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LandingPage]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "catalog/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LandingPage,
                    parse_obj_as(
                        type_=LandingPage,
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

    def conformance_classes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Conformance]:
        """
        Endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Conformance]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "catalog/conformance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Conformance,
                    parse_obj_as(
                        type_=Conformance,
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

    def get_item(
        self, collection_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StacPydanticApiItemItem]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        item_id : str
            Item ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StacPydanticApiItemItem]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}/items/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticApiItemItem,
                    parse_obj_as(
                        type_=StacPydanticApiItemItem,
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

    def search(
        self,
        *,
        collections: typing.Optional[typing.Sequence[str]] = OMIT,
        ids: typing.Optional[typing.Sequence[str]] = OMIT,
        bbox: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        intersects: typing.Optional[SearchPostRequestIntersects] = OMIT,
        datetime: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        conf: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        query: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        sortby: typing.Optional[typing.Sequence[SortExtension]] = OMIT,
        fields: typing.Optional[PostFieldsExtension] = OMIT,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        filter_crs: typing.Optional[str] = OMIT,
        filter_lang: typing.Optional[SearchPostRequestFilterLang] = OMIT,
        token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ItemCollectionOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collections : typing.Optional[typing.Sequence[str]]

        ids : typing.Optional[typing.Sequence[str]]

        bbox : typing.Optional[typing.Sequence[typing.Any]]

        intersects : typing.Optional[SearchPostRequestIntersects]

        datetime : typing.Optional[str]

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response (capped to 10_000).

        conf : typing.Optional[typing.Dict[str, typing.Any]]

        query : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]

        sortby : typing.Optional[typing.Sequence[SortExtension]]
            An array of property (field) names, and direction in form of '{'field': '<property_name>', 'direction':'<direction>'}'

        fields : typing.Optional[PostFieldsExtension]
            Include or exclude fields from items body.

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            A CQL filter expression for filtering items.

        filter_crs : typing.Optional[str]
            The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`

        filter_lang : typing.Optional[SearchPostRequestFilterLang]
            The CQL filter encoding that the 'filter' value uses.

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ItemCollectionOutput]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "catalog/search",
            method="POST",
            json={
                "collections": collections,
                "ids": ids,
                "bbox": bbox,
                "intersects": convert_and_respect_annotation_metadata(
                    object_=intersects, annotation=typing.Optional[SearchPostRequestIntersects], direction="write"
                ),
                "datetime": datetime,
                "limit": limit,
                "conf": conf,
                "query": query,
                "sortby": convert_and_respect_annotation_metadata(
                    object_=sortby, annotation=typing.Optional[typing.Sequence[SortExtension]], direction="write"
                ),
                "fields": convert_and_respect_annotation_metadata(
                    object_=fields, annotation=typing.Optional[PostFieldsExtension], direction="write"
                ),
                "filter": filter,
                "filter-crs": filter_crs,
                "filter-lang": filter_lang,
                "token": token,
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
                    ItemCollectionOutput,
                    parse_obj_as(
                        type_=ItemCollectionOutput,
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

    def get_collections(
        self,
        *,
        bbox: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        sortby: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_crs: typing.Optional[str] = None,
        filter_lang: typing.Optional[GetCollectionsCatalogCollectionsGetRequestFilterLang] = None,
        q: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Collections]:
        """
        Endpoint.

        Parameters
        ----------
        bbox : typing.Optional[str]
            Only return items intersecting this bounding box. Mutually exclusive with **intersects**.

        datetime : typing.Optional[str]
            Only return items that have a temporal property that intersects this value.

            Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response.

        query : typing.Optional[str]
            Allows additional filtering based on the properties of Item objects

        sortby : typing.Optional[str]
            An array of property names, prefixed by either '+' for ascending or '-' for descending. If no prefix is provided, '+' is assumed.

        fields : typing.Optional[str]
            Include or exclude fields from items body.

        filter : typing.Optional[str]
            A CQL2 filter expression for filtering items.

            Supports `CQL2-JSON` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.htmln
            Remember to URL encode the CQL2-JSON if using GET

        filter_crs : typing.Optional[str]
            The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`

        filter_lang : typing.Optional[GetCollectionsCatalogCollectionsGetRequestFilterLang]
            The CQL filter encoding that the 'filter' value uses.

        q : typing.Optional[str]
            Parameter to perform free-text queries against STAC metadata

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Collections]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "catalog/collections",
            method="GET",
            params={
                "bbox": bbox,
                "datetime": datetime,
                "limit": limit,
                "query": query,
                "sortby": sortby,
                "fields": fields,
                "filter": filter,
                "filter-crs": filter_crs,
                "filter-lang": filter_lang,
                "q": q,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collections,
                    parse_obj_as(
                        type_=Collections,
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

    def get_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StacPydanticApiCollectionCollection]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StacPydanticApiCollectionCollection]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticApiCollectionCollection,
                    parse_obj_as(
                        type_=StacPydanticApiCollectionCollection,
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

    def get_item_collection(
        self,
        collection_id: str,
        *,
        limit: typing.Optional[int] = None,
        bbox: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        sortby: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_crs: typing.Optional[str] = None,
        filter_lang: typing.Optional[GetItemCollectionCatalogCollectionsCollectionIdItemsGetRequestFilterLang] = None,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ItemCollectionOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response (capped to 10_000).

        bbox : typing.Optional[str]
            Only return items intersecting this bounding box. Mutually exclusive with **intersects**.

        datetime : typing.Optional[str]
            Only return items that have a temporal property that intersects this value.

            Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.

        query : typing.Optional[str]
            Allows additional filtering based on the properties of Item objects

        sortby : typing.Optional[str]
            An array of property names, prefixed by either '+' for ascending or '-' for descending. If no prefix is provided, '+' is assumed.

        fields : typing.Optional[str]
            Include or exclude fields from items body.

        filter : typing.Optional[str]
            A CQL2 filter expression for filtering items.

            Supports `CQL2-JSON` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.htmln
            Remember to URL encode the CQL2-JSON if using GET

        filter_crs : typing.Optional[str]
            The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`

        filter_lang : typing.Optional[GetItemCollectionCatalogCollectionsCollectionIdItemsGetRequestFilterLang]
            The CQL filter encoding that the 'filter' value uses.

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ItemCollectionOutput]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}/items",
            method="GET",
            params={
                "limit": limit,
                "bbox": bbox,
                "datetime": datetime,
                "query": query,
                "sortby": sortby,
                "fields": fields,
                "filter": filter,
                "filter-crs": filter_crs,
                "filter-lang": filter_lang,
                "token": token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ItemCollectionOutput,
                    parse_obj_as(
                        type_=ItemCollectionOutput,
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


class AsyncRawCatalogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def landing_page(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LandingPage]:
        """
        Endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LandingPage]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "catalog/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LandingPage,
                    parse_obj_as(
                        type_=LandingPage,
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

    async def conformance_classes(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Conformance]:
        """
        Endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Conformance]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "catalog/conformance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Conformance,
                    parse_obj_as(
                        type_=Conformance,
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

    async def get_item(
        self, collection_id: str, item_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StacPydanticApiItemItem]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        item_id : str
            Item ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StacPydanticApiItemItem]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}/items/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticApiItemItem,
                    parse_obj_as(
                        type_=StacPydanticApiItemItem,
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

    async def search(
        self,
        *,
        collections: typing.Optional[typing.Sequence[str]] = OMIT,
        ids: typing.Optional[typing.Sequence[str]] = OMIT,
        bbox: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        intersects: typing.Optional[SearchPostRequestIntersects] = OMIT,
        datetime: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        conf: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        query: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        sortby: typing.Optional[typing.Sequence[SortExtension]] = OMIT,
        fields: typing.Optional[PostFieldsExtension] = OMIT,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        filter_crs: typing.Optional[str] = OMIT,
        filter_lang: typing.Optional[SearchPostRequestFilterLang] = OMIT,
        token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ItemCollectionOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collections : typing.Optional[typing.Sequence[str]]

        ids : typing.Optional[typing.Sequence[str]]

        bbox : typing.Optional[typing.Sequence[typing.Any]]

        intersects : typing.Optional[SearchPostRequestIntersects]

        datetime : typing.Optional[str]

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response (capped to 10_000).

        conf : typing.Optional[typing.Dict[str, typing.Any]]

        query : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]

        sortby : typing.Optional[typing.Sequence[SortExtension]]
            An array of property (field) names, and direction in form of '{'field': '<property_name>', 'direction':'<direction>'}'

        fields : typing.Optional[PostFieldsExtension]
            Include or exclude fields from items body.

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            A CQL filter expression for filtering items.

        filter_crs : typing.Optional[str]
            The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`

        filter_lang : typing.Optional[SearchPostRequestFilterLang]
            The CQL filter encoding that the 'filter' value uses.

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ItemCollectionOutput]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "catalog/search",
            method="POST",
            json={
                "collections": collections,
                "ids": ids,
                "bbox": bbox,
                "intersects": convert_and_respect_annotation_metadata(
                    object_=intersects, annotation=typing.Optional[SearchPostRequestIntersects], direction="write"
                ),
                "datetime": datetime,
                "limit": limit,
                "conf": conf,
                "query": query,
                "sortby": convert_and_respect_annotation_metadata(
                    object_=sortby, annotation=typing.Optional[typing.Sequence[SortExtension]], direction="write"
                ),
                "fields": convert_and_respect_annotation_metadata(
                    object_=fields, annotation=typing.Optional[PostFieldsExtension], direction="write"
                ),
                "filter": filter,
                "filter-crs": filter_crs,
                "filter-lang": filter_lang,
                "token": token,
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
                    ItemCollectionOutput,
                    parse_obj_as(
                        type_=ItemCollectionOutput,
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

    async def get_collections(
        self,
        *,
        bbox: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        sortby: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_crs: typing.Optional[str] = None,
        filter_lang: typing.Optional[GetCollectionsCatalogCollectionsGetRequestFilterLang] = None,
        q: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Collections]:
        """
        Endpoint.

        Parameters
        ----------
        bbox : typing.Optional[str]
            Only return items intersecting this bounding box. Mutually exclusive with **intersects**.

        datetime : typing.Optional[str]
            Only return items that have a temporal property that intersects this value.

            Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response.

        query : typing.Optional[str]
            Allows additional filtering based on the properties of Item objects

        sortby : typing.Optional[str]
            An array of property names, prefixed by either '+' for ascending or '-' for descending. If no prefix is provided, '+' is assumed.

        fields : typing.Optional[str]
            Include or exclude fields from items body.

        filter : typing.Optional[str]
            A CQL2 filter expression for filtering items.

            Supports `CQL2-JSON` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.htmln
            Remember to URL encode the CQL2-JSON if using GET

        filter_crs : typing.Optional[str]
            The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`

        filter_lang : typing.Optional[GetCollectionsCatalogCollectionsGetRequestFilterLang]
            The CQL filter encoding that the 'filter' value uses.

        q : typing.Optional[str]
            Parameter to perform free-text queries against STAC metadata

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Collections]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "catalog/collections",
            method="GET",
            params={
                "bbox": bbox,
                "datetime": datetime,
                "limit": limit,
                "query": query,
                "sortby": sortby,
                "fields": fields,
                "filter": filter,
                "filter-crs": filter_crs,
                "filter-lang": filter_lang,
                "q": q,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collections,
                    parse_obj_as(
                        type_=Collections,
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

    async def get_collection(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StacPydanticApiCollectionCollection]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StacPydanticApiCollectionCollection]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StacPydanticApiCollectionCollection,
                    parse_obj_as(
                        type_=StacPydanticApiCollectionCollection,
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

    async def get_item_collection(
        self,
        collection_id: str,
        *,
        limit: typing.Optional[int] = None,
        bbox: typing.Optional[str] = None,
        datetime: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        sortby: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        filter_crs: typing.Optional[str] = None,
        filter_lang: typing.Optional[GetItemCollectionCatalogCollectionsCollectionIdItemsGetRequestFilterLang] = None,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ItemCollectionOutput]:
        """
        Endpoint.

        Parameters
        ----------
        collection_id : str
            Collection ID

        limit : typing.Optional[int]
            Limits the number of results that are included in each page of the response (capped to 10_000).

        bbox : typing.Optional[str]
            Only return items intersecting this bounding box. Mutually exclusive with **intersects**.

        datetime : typing.Optional[str]
            Only return items that have a temporal property that intersects this value.

            Either a date-time or an interval, open or closed. Date and time expressions adhere to RFC 3339. Open intervals are expressed using double-dots.

        query : typing.Optional[str]
            Allows additional filtering based on the properties of Item objects

        sortby : typing.Optional[str]
            An array of property names, prefixed by either '+' for ascending or '-' for descending. If no prefix is provided, '+' is assumed.

        fields : typing.Optional[str]
            Include or exclude fields from items body.

        filter : typing.Optional[str]
            A CQL2 filter expression for filtering items.

            Supports `CQL2-JSON` as defined in https://docs.ogc.org/is/21-065r2/21-065r2.htmln
            Remember to URL encode the CQL2-JSON if using GET

        filter_crs : typing.Optional[str]
            The coordinate reference system (CRS) used by spatial literals in the 'filter' value. Default is `http://www.opengis.net/def/crs/OGC/1.3/CRS84`

        filter_lang : typing.Optional[GetItemCollectionCatalogCollectionsCollectionIdItemsGetRequestFilterLang]
            The CQL filter encoding that the 'filter' value uses.

        token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ItemCollectionOutput]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"catalog/collections/{encode_path_param(collection_id)}/items",
            method="GET",
            params={
                "limit": limit,
                "bbox": bbox,
                "datetime": datetime,
                "query": query,
                "sortby": sortby,
                "fields": fields,
                "filter": filter,
                "filter-crs": filter_crs,
                "filter-lang": filter_lang,
                "token": token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ItemCollectionOutput,
                    parse_obj_as(
                        type_=ItemCollectionOutput,
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
