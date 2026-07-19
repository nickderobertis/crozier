

import contextlib
import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.get_full_text_search_response import GetFullTextSearchResponse
from .types.post_faceted_search_facet_class_facet_id_response import PostFacetedSearchFacetClassFacetIdResponse
from .types.post_faceted_search_result_class_count_response import PostFacetedSearchResultClassCountResponse
from .types.post_faceted_search_result_class_paginated_response import PostFacetedSearchResultClassPaginatedResponse
from .types.post_result_class_page_uri_response import PostResultClassPageUriResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def return_faceted_search_results_with_pagination(
        self,
        result_class: str,
        *,
        page: typing.Optional[int] = OMIT,
        pagesize: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[str] = OMIT,
        sort_direction: typing.Optional[str] = OMIT,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostFacetedSearchResultClassPaginatedResponse]:
        """
        Parameters
        ----------
        result_class : str
            The class of the results

        page : typing.Optional[int]

        pagesize : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[str]

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostFacetedSearchResultClassPaginatedResponse]
            Paginated search results
        """
        _response = self._client_wrapper.httpx_client.request(
            f"faceted-search/{encode_path_param(result_class)}/paginated",
            method="POST",
            json={
                "page": page,
                "pagesize": pagesize,
                "sortBy": sort_by,
                "sortDirection": sort_direction,
                "constraints": constraints,
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
                    PostFacetedSearchResultClassPaginatedResponse,
                    parse_obj_as(
                        type_=PostFacetedSearchResultClassPaginatedResponse,
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

    @contextlib.contextmanager
    def return_all_search_results_as_a_csv_file(
        self,
        result_class: str,
        *,
        facet_class: str,
        result_format: str,
        constraints: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        result_class : str
            The class of the results

        facet_class : str
            The class for facet configs

        result_format : str
            Result format, only support for CSV for now.

        constraints : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            All search results as a CSV file
        """
        with self._client_wrapper.httpx_client.stream(
            f"faceted-search/{encode_path_param(result_class)}/all",
            method="GET",
            params={
                "facetClass": facet_class,
                "constraints": constraints,
                "resultFormat": result_format,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def return_all_search_results(
        self,
        result_class: str,
        *,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        result_class : str
            The class of the results

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            All search results
        """
        _response = self._client_wrapper.httpx_client.request(
            f"faceted-search/{encode_path_param(result_class)}/all",
            method="POST",
            json={
                "constraints": constraints,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    def return_the_total_count_of_the_faceted_search_results(
        self,
        result_class: str,
        *,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostFacetedSearchResultClassCountResponse]:
        """
        Parameters
        ----------
        result_class : str
            The class of the results

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostFacetedSearchResultClassCountResponse]
            The total count of the faceted search results
        """
        _response = self._client_wrapper.httpx_client.request(
            f"faceted-search/{encode_path_param(result_class)}/count",
            method="POST",
            json={
                "constraints": constraints,
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
                    PostFacetedSearchResultClassCountResponse,
                    parse_obj_as(
                        type_=PostFacetedSearchResultClassCountResponse,
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

    def return_values_for_a_single_facet(
        self,
        facet_class: str,
        id: str,
        *,
        sort_by: typing.Optional[str] = OMIT,
        sort_direction: typing.Optional[str] = OMIT,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        constrain_self: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostFacetedSearchFacetClassFacetIdResponse]:
        """
        Parameters
        ----------
        facet_class : str
            The class of the facet

        id : str
            The id of the facet

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[str]

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        constrain_self : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostFacetedSearchFacetClassFacetIdResponse]
            Facet values
        """
        _response = self._client_wrapper.httpx_client.request(
            f"faceted-search/{encode_path_param(facet_class)}/facet/{encode_path_param(id)}",
            method="POST",
            json={
                "sortBy": sort_by,
                "sortDirection": sort_direction,
                "constraints": constraints,
                "constrainSelf": constrain_self,
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
                    PostFacetedSearchFacetClassFacetIdResponse,
                    parse_obj_as(
                        type_=PostFacetedSearchFacetClassFacetIdResponse,
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

    def return_information_about_a_single_resource_optionally_applying_facet_filters(
        self,
        result_class: str,
        uri: str,
        *,
        facet_class: typing.Optional[str] = OMIT,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostResultClassPageUriResponse]:
        """
        Parameters
        ----------
        result_class : str
            The class of the resource

        uri : str
            The URI of the resource

        facet_class : typing.Optional[str]

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostResultClassPageUriResponse]
            Information about a single resource
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(result_class)}/page/{encode_path_param(uri)}",
            method="POST",
            json={
                "facetClass": facet_class,
                "constraints": constraints,
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
                    PostResultClassPageUriResponse,
                    parse_obj_as(
                        type_=PostResultClassPageUriResponse,
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

    def full_text_search(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetFullTextSearchResponse]:
        """
        Parameters
        ----------
        q : str
            The query string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetFullTextSearchResponse]
            Full text search results
        """
        _response = self._client_wrapper.httpx_client.request(
            "full-text-search",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFullTextSearchResponse,
                    parse_obj_as(
                        type_=GetFullTextSearchResponse,
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

    def federated_search_can_be_used_for_retrieving_the_initial_result_set_from_multiple_sparql_endpoints_for_client_side_faceted_search(
        self,
        *,
        perspective_id: str,
        dataset: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        q: typing.Optional[str] = None,
        lat_min: typing.Optional[float] = None,
        long_min: typing.Optional[float] = None,
        lat_max: typing.Optional[float] = None,
        long_max: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[typing.Dict[str, typing.Any]]]:
        """
        Parameters
        ----------
        perspective_id : str

        dataset : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        q : typing.Optional[str]
            The query string

        lat_min : typing.Optional[float]

        long_min : typing.Optional[float]

        lat_max : typing.Optional[float]

        long_max : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[typing.Dict[str, typing.Any]]]
            Federated search results
        """
        _response = self._client_wrapper.httpx_client.request(
            "federated-search",
            method="GET",
            params={
                "perspectiveID": perspective_id,
                "dataset": dataset,
                "q": q,
                "latMin": lat_min,
                "longMin": long_min,
                "latMax": lat_max,
                "longMax": long_max,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Dict[str, typing.Any]],
                    parse_obj_as(
                        type_=typing.List[typing.Dict[str, typing.Any]],
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

    def make_preconfigured_web_feature_service_wfs_api_calls_via_the_backend(
        self,
        *,
        layer_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[typing.Any]]:
        """
        Parameters
        ----------
        layer_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[typing.Any]]
            An array of GeoJSON layers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "wfs",
            method="GET",
            params={
                "layerID": layer_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Any],
                    parse_obj_as(
                        type_=typing.List[typing.Any],
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

    @contextlib.contextmanager
    def route_for_password_protected_wms_layers(
        self,
        *,
        service: str,
        request: str,
        layers: str,
        styles: str,
        format: str,
        transparent: bool,
        version: str,
        width: float,
        height: float,
        crs: str,
        bbox: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        service : str

        request : str

        layers : str

        styles : str

        format : str

        transparent : bool

        version : str

        width : float

        height : float

        crs : str

        bbox : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Image
        """
        with self._client_wrapper.httpx_client.stream(
            "fha-wms",
            method="GET",
            params={
                "service": service,
                "request": request,
                "layers": layers,
                "styles": styles,
                "format": format,
                "transparent": transparent,
                "version": version,
                "width": width,
                "height": height,
                "crs": crs,
                "bbox": bbox,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def route_for_nls_wmts_api_only_for_contract_customers(
        self, *, layer_id: str, x: str, y: str, z: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[typing.Any]]:
        """
        Parameters
        ----------
        layer_id : str

        x : str

        y : str

        z : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[typing.Any]]
            An array of GeoJSON layers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "nls-wmts",
            method="GET",
            params={
                "layerID": layer_id,
                "x": x,
                "y": y,
                "z": z,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Any],
                    parse_obj_as(
                        type_=typing.List[typing.Any],
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

    def route_for_nls_wmts_api_free_but_requires_an_api_key(
        self, *, layer_id: str, x: str, y: str, z: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[typing.Any]]:
        """
        Parameters
        ----------
        layer_id : str

        x : str

        y : str

        z : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[typing.Any]]
            An array of GeoJSON layers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "nls-wmts-open",
            method="GET",
            params={
                "layerID": layer_id,
                "x": x,
                "y": y,
                "z": z,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Any],
                    parse_obj_as(
                        type_=typing.List[typing.Any],
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

    def route_for_nls_vectortiles_api_free_but_requires_an_api_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Styles for vector tiles as JSON
        """
        _response = self._client_wrapper.httpx_client.request(
            "nls-vectortiles-open",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    def retrieve_a_vo_id_description(
        self, perspective_id: str, result_class: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        perspective_id : str

        result_class : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            VoID description as JSON.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"void/{encode_path_param(perspective_id)}/{encode_path_param(result_class)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def return_faceted_search_results_with_pagination(
        self,
        result_class: str,
        *,
        page: typing.Optional[int] = OMIT,
        pagesize: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[str] = OMIT,
        sort_direction: typing.Optional[str] = OMIT,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostFacetedSearchResultClassPaginatedResponse]:
        """
        Parameters
        ----------
        result_class : str
            The class of the results

        page : typing.Optional[int]

        pagesize : typing.Optional[int]

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[str]

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostFacetedSearchResultClassPaginatedResponse]
            Paginated search results
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"faceted-search/{encode_path_param(result_class)}/paginated",
            method="POST",
            json={
                "page": page,
                "pagesize": pagesize,
                "sortBy": sort_by,
                "sortDirection": sort_direction,
                "constraints": constraints,
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
                    PostFacetedSearchResultClassPaginatedResponse,
                    parse_obj_as(
                        type_=PostFacetedSearchResultClassPaginatedResponse,
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

    @contextlib.asynccontextmanager
    async def return_all_search_results_as_a_csv_file(
        self,
        result_class: str,
        *,
        facet_class: str,
        result_format: str,
        constraints: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        result_class : str
            The class of the results

        facet_class : str
            The class for facet configs

        result_format : str
            Result format, only support for CSV for now.

        constraints : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            All search results as a CSV file
        """
        async with self._client_wrapper.httpx_client.stream(
            f"faceted-search/{encode_path_param(result_class)}/all",
            method="GET",
            params={
                "facetClass": facet_class,
                "constraints": constraints,
                "resultFormat": result_format,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def return_all_search_results(
        self,
        result_class: str,
        *,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        result_class : str
            The class of the results

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            All search results
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"faceted-search/{encode_path_param(result_class)}/all",
            method="POST",
            json={
                "constraints": constraints,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    async def return_the_total_count_of_the_faceted_search_results(
        self,
        result_class: str,
        *,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostFacetedSearchResultClassCountResponse]:
        """
        Parameters
        ----------
        result_class : str
            The class of the results

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostFacetedSearchResultClassCountResponse]
            The total count of the faceted search results
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"faceted-search/{encode_path_param(result_class)}/count",
            method="POST",
            json={
                "constraints": constraints,
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
                    PostFacetedSearchResultClassCountResponse,
                    parse_obj_as(
                        type_=PostFacetedSearchResultClassCountResponse,
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

    async def return_values_for_a_single_facet(
        self,
        facet_class: str,
        id: str,
        *,
        sort_by: typing.Optional[str] = OMIT,
        sort_direction: typing.Optional[str] = OMIT,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        constrain_self: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostFacetedSearchFacetClassFacetIdResponse]:
        """
        Parameters
        ----------
        facet_class : str
            The class of the facet

        id : str
            The id of the facet

        sort_by : typing.Optional[str]

        sort_direction : typing.Optional[str]

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        constrain_self : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostFacetedSearchFacetClassFacetIdResponse]
            Facet values
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"faceted-search/{encode_path_param(facet_class)}/facet/{encode_path_param(id)}",
            method="POST",
            json={
                "sortBy": sort_by,
                "sortDirection": sort_direction,
                "constraints": constraints,
                "constrainSelf": constrain_self,
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
                    PostFacetedSearchFacetClassFacetIdResponse,
                    parse_obj_as(
                        type_=PostFacetedSearchFacetClassFacetIdResponse,
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

    async def return_information_about_a_single_resource_optionally_applying_facet_filters(
        self,
        result_class: str,
        uri: str,
        *,
        facet_class: typing.Optional[str] = OMIT,
        constraints: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostResultClassPageUriResponse]:
        """
        Parameters
        ----------
        result_class : str
            The class of the resource

        uri : str
            The URI of the resource

        facet_class : typing.Optional[str]

        constraints : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostResultClassPageUriResponse]
            Information about a single resource
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(result_class)}/page/{encode_path_param(uri)}",
            method="POST",
            json={
                "facetClass": facet_class,
                "constraints": constraints,
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
                    PostResultClassPageUriResponse,
                    parse_obj_as(
                        type_=PostResultClassPageUriResponse,
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

    async def full_text_search(
        self, *, q: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetFullTextSearchResponse]:
        """
        Parameters
        ----------
        q : str
            The query string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetFullTextSearchResponse]
            Full text search results
        """
        _response = await self._client_wrapper.httpx_client.request(
            "full-text-search",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFullTextSearchResponse,
                    parse_obj_as(
                        type_=GetFullTextSearchResponse,
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

    async def federated_search_can_be_used_for_retrieving_the_initial_result_set_from_multiple_sparql_endpoints_for_client_side_faceted_search(
        self,
        *,
        perspective_id: str,
        dataset: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        q: typing.Optional[str] = None,
        lat_min: typing.Optional[float] = None,
        long_min: typing.Optional[float] = None,
        lat_max: typing.Optional[float] = None,
        long_max: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[typing.Dict[str, typing.Any]]]:
        """
        Parameters
        ----------
        perspective_id : str

        dataset : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        q : typing.Optional[str]
            The query string

        lat_min : typing.Optional[float]

        long_min : typing.Optional[float]

        lat_max : typing.Optional[float]

        long_max : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[typing.Dict[str, typing.Any]]]
            Federated search results
        """
        _response = await self._client_wrapper.httpx_client.request(
            "federated-search",
            method="GET",
            params={
                "perspectiveID": perspective_id,
                "dataset": dataset,
                "q": q,
                "latMin": lat_min,
                "longMin": long_min,
                "latMax": lat_max,
                "longMax": long_max,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Dict[str, typing.Any]],
                    parse_obj_as(
                        type_=typing.List[typing.Dict[str, typing.Any]],
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

    async def make_preconfigured_web_feature_service_wfs_api_calls_via_the_backend(
        self,
        *,
        layer_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[typing.Any]]:
        """
        Parameters
        ----------
        layer_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[typing.Any]]
            An array of GeoJSON layers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "wfs",
            method="GET",
            params={
                "layerID": layer_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Any],
                    parse_obj_as(
                        type_=typing.List[typing.Any],
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

    @contextlib.asynccontextmanager
    async def route_for_password_protected_wms_layers(
        self,
        *,
        service: str,
        request: str,
        layers: str,
        styles: str,
        format: str,
        transparent: bool,
        version: str,
        width: float,
        height: float,
        crs: str,
        bbox: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        service : str

        request : str

        layers : str

        styles : str

        format : str

        transparent : bool

        version : str

        width : float

        height : float

        crs : str

        bbox : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Image
        """
        async with self._client_wrapper.httpx_client.stream(
            "fha-wms",
            method="GET",
            params={
                "service": service,
                "request": request,
                "layers": layers,
                "styles": styles,
                "format": format,
                "transparent": transparent,
                "version": version,
                "width": width,
                "height": height,
                "crs": crs,
                "bbox": bbox,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def route_for_nls_wmts_api_only_for_contract_customers(
        self, *, layer_id: str, x: str, y: str, z: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[typing.Any]]:
        """
        Parameters
        ----------
        layer_id : str

        x : str

        y : str

        z : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[typing.Any]]
            An array of GeoJSON layers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "nls-wmts",
            method="GET",
            params={
                "layerID": layer_id,
                "x": x,
                "y": y,
                "z": z,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Any],
                    parse_obj_as(
                        type_=typing.List[typing.Any],
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

    async def route_for_nls_wmts_api_free_but_requires_an_api_key(
        self, *, layer_id: str, x: str, y: str, z: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[typing.Any]]:
        """
        Parameters
        ----------
        layer_id : str

        x : str

        y : str

        z : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[typing.Any]]
            An array of GeoJSON layers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "nls-wmts-open",
            method="GET",
            params={
                "layerID": layer_id,
                "x": x,
                "y": y,
                "z": z,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Any],
                    parse_obj_as(
                        type_=typing.List[typing.Any],
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

    async def route_for_nls_vectortiles_api_free_but_requires_an_api_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Styles for vector tiles as JSON
        """
        _response = await self._client_wrapper.httpx_client.request(
            "nls-vectortiles-open",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    async def retrieve_a_vo_id_description(
        self, perspective_id: str, result_class: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        perspective_id : str

        result_class : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            VoID description as JSON.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"void/{encode_path_param(perspective_id)}/{encode_path_param(result_class)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
