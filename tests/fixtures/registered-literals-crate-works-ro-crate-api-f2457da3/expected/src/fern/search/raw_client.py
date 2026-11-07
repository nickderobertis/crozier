

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.forbidden_error_body import ForbiddenErrorBody
from ..types.internal_server_error_body import InternalServerErrorBody
from ..types.order import Order
from ..types.rate_limit_error import RateLimitError
from ..types.unauthorized_error_body import UnauthorizedErrorBody
from ..types.validation_error import ValidationError as types_validation_error_ValidationError
from .types.search_entities_request_bounding_box import SearchEntitiesRequestBoundingBox
from .types.search_entities_request_filters_value import SearchEntitiesRequestFiltersValue
from .types.search_entities_request_search_type import SearchEntitiesRequestSearchType
from .types.search_entities_request_sort import SearchEntitiesRequestSort
from .types.search_entities_response import SearchEntitiesResponse
from pydantic import ValidationError as pydantic_ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def entities(
        self,
        *,
        query: str,
        search_type: typing.Optional[SearchEntitiesRequestSearchType] = OMIT,
        filters: typing.Optional[typing.Dict[str, SearchEntitiesRequestFiltersValue]] = OMIT,
        bounding_box: typing.Optional[SearchEntitiesRequestBoundingBox] = OMIT,
        geohash_precision: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        sort: typing.Optional[SearchEntitiesRequestSort] = OMIT,
        order: typing.Optional[Order] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchEntitiesResponse]:
        """
        Perform advanced or basic searches across the entire RO-Crate collection. This includes free text queries, as well as filters for specific fields such as `inLanguage` or `mediaType`. The search results can be paginated, sorted, and optionally returned alongside facet counts.

        Parameters
        ----------
        query : str
            The query string used in the search. Behavior depends on `searchType`. For `basic`, this can be free text. For `advanced`, Boolean operators can be used.

            When searchType is `basic` this is a free text field of text to search.

            When searchType is `advanced` this is a boolean search field.
            Examples:
              name: John
              name: John AND description: Engineer
              name: John AND (description: Engineer OR description: developer)

            NOTE: This API is implementation-agnostic. The examples above show basic boolean syntax that most search engines support.
            API implementors may support additional query syntax - refer to your implementation's documentation for details.

        search_type : typing.Optional[SearchEntitiesRequestSearchType]
            Specifies the search method to be used. `basic` searches across common fields, whereas `advanced` can handle Boolean queries or more complex logic.

        filters : typing.Optional[typing.Dict[str, SearchEntitiesRequestFiltersValue]]
            A set of key-value pairs representing additional filters. Keys MUST be filter fields the implementation declares in `/capabilities` under `search.filters`; a request using an undeclared key MUST be rejected with a 400 `ValidationError`.

            Each value is either an array of acceptable values (matched as exact terms, valid for any filter type), a single range object with inclusive `gte`/`lte` bounds, or a non-empty array of range objects matched as an OR of the ranges — an entity matches when any of the ranges matches. Ranges, single or in an array, are valid only for filters declared with type `date` or `number`; a range sent to a `string` or `boolean` filter MUST be rejected with a 400 `ValidationError`. An array MUST NOT mix exact terms and range objects; such a request MUST be rejected with a 400 `ValidationError`.

        bounding_box : typing.Optional[SearchEntitiesRequestBoundingBox]
            Will filter the results to entities that exist inside the bounding box.

        geohash_precision : typing.Optional[int]
            If supplied, returns a geohash grid with this precision. Must be between 1 (lowest precision) and 12 (highest precision).

        limit : typing.Optional[int]
            Maximum number of entities to return per page.

        offset : typing.Optional[int]
            Number of items to skip before returning the results, enabling paging.

        sort : typing.Optional[SearchEntitiesRequestSort]
            The field on which to sort results. Defaults to `relevance`, which orders
            results by search score (highest first). When set to `relevance`, the
            `order` parameter is ignored. Use `id`, `name`, `createdAt`, or
            `updatedAt` to sort by a specific field.

        order : typing.Optional[Order]
            Sort order:
            * `asc` - Ascending, from A to Z
            * `desc` - Descending, from Z to A

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchEntitiesResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "search",
            method="POST",
            json={
                "searchType": search_type,
                "query": query,
                "filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=typing.Dict[str, SearchEntitiesRequestFiltersValue], direction="write"
                ),
                "boundingBox": convert_and_respect_annotation_metadata(
                    object_=bounding_box, annotation=SearchEntitiesRequestBoundingBox, direction="write"
                ),
                "geohashPrecision": geohash_precision,
                "limit": limit,
                "offset": offset,
                "sort": sort,
                "order": order,
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
                    SearchEntitiesResponse,
                    parse_obj_as(
                        type_=SearchEntitiesResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_validation_error_ValidationError,
                        parse_obj_as(
                            type_=types_validation_error_ValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except pydantic_ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def entities(
        self,
        *,
        query: str,
        search_type: typing.Optional[SearchEntitiesRequestSearchType] = OMIT,
        filters: typing.Optional[typing.Dict[str, SearchEntitiesRequestFiltersValue]] = OMIT,
        bounding_box: typing.Optional[SearchEntitiesRequestBoundingBox] = OMIT,
        geohash_precision: typing.Optional[int] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        sort: typing.Optional[SearchEntitiesRequestSort] = OMIT,
        order: typing.Optional[Order] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchEntitiesResponse]:
        """
        Perform advanced or basic searches across the entire RO-Crate collection. This includes free text queries, as well as filters for specific fields such as `inLanguage` or `mediaType`. The search results can be paginated, sorted, and optionally returned alongside facet counts.

        Parameters
        ----------
        query : str
            The query string used in the search. Behavior depends on `searchType`. For `basic`, this can be free text. For `advanced`, Boolean operators can be used.

            When searchType is `basic` this is a free text field of text to search.

            When searchType is `advanced` this is a boolean search field.
            Examples:
              name: John
              name: John AND description: Engineer
              name: John AND (description: Engineer OR description: developer)

            NOTE: This API is implementation-agnostic. The examples above show basic boolean syntax that most search engines support.
            API implementors may support additional query syntax - refer to your implementation's documentation for details.

        search_type : typing.Optional[SearchEntitiesRequestSearchType]
            Specifies the search method to be used. `basic` searches across common fields, whereas `advanced` can handle Boolean queries or more complex logic.

        filters : typing.Optional[typing.Dict[str, SearchEntitiesRequestFiltersValue]]
            A set of key-value pairs representing additional filters. Keys MUST be filter fields the implementation declares in `/capabilities` under `search.filters`; a request using an undeclared key MUST be rejected with a 400 `ValidationError`.

            Each value is either an array of acceptable values (matched as exact terms, valid for any filter type), a single range object with inclusive `gte`/`lte` bounds, or a non-empty array of range objects matched as an OR of the ranges — an entity matches when any of the ranges matches. Ranges, single or in an array, are valid only for filters declared with type `date` or `number`; a range sent to a `string` or `boolean` filter MUST be rejected with a 400 `ValidationError`. An array MUST NOT mix exact terms and range objects; such a request MUST be rejected with a 400 `ValidationError`.

        bounding_box : typing.Optional[SearchEntitiesRequestBoundingBox]
            Will filter the results to entities that exist inside the bounding box.

        geohash_precision : typing.Optional[int]
            If supplied, returns a geohash grid with this precision. Must be between 1 (lowest precision) and 12 (highest precision).

        limit : typing.Optional[int]
            Maximum number of entities to return per page.

        offset : typing.Optional[int]
            Number of items to skip before returning the results, enabling paging.

        sort : typing.Optional[SearchEntitiesRequestSort]
            The field on which to sort results. Defaults to `relevance`, which orders
            results by search score (highest first). When set to `relevance`, the
            `order` parameter is ignored. Use `id`, `name`, `createdAt`, or
            `updatedAt` to sort by a specific field.

        order : typing.Optional[Order]
            Sort order:
            * `asc` - Ascending, from A to Z
            * `desc` - Descending, from Z to A

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchEntitiesResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "search",
            method="POST",
            json={
                "searchType": search_type,
                "query": query,
                "filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=typing.Dict[str, SearchEntitiesRequestFiltersValue], direction="write"
                ),
                "boundingBox": convert_and_respect_annotation_metadata(
                    object_=bounding_box, annotation=SearchEntitiesRequestBoundingBox, direction="write"
                ),
                "geohashPrecision": geohash_precision,
                "limit": limit,
                "offset": offset,
                "sort": sort,
                "order": order,
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
                    SearchEntitiesResponse,
                    parse_obj_as(
                        type_=SearchEntitiesResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_validation_error_ValidationError,
                        parse_obj_as(
                            type_=types_validation_error_ValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        RateLimitError,
                        parse_obj_as(
                            type_=RateLimitError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InternalServerErrorBody,
                        parse_obj_as(
                            type_=InternalServerErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except pydantic_ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
