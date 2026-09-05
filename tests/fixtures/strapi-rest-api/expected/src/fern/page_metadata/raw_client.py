

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
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error_response import ErrorResponse
from ..types.get_page_metadata_request_populate import GetPageMetadataRequestPopulate
from ..types.list_page_metadata_request_populate import ListPageMetadataRequestPopulate
from ..types.page_metadata_attributes import PageMetadataAttributes
from ..types.page_metadata_list_response import PageMetadataListResponse
from ..types.page_metadata_single_response import PageMetadataSingleResponse
from .types.get_page_metadata_request_status import GetPageMetadataRequestStatus
from .types.list_page_metadata_request_status import ListPageMetadataRequestStatus
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPageMetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_page_metadata(
        self,
        *,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        populate: typing.Optional[ListPageMetadataRequestPopulate] = None,
        status: typing.Optional[ListPageMetadataRequestStatus] = None,
        locale: typing.Optional[str] = None,
        publication_filter: typing.Optional[str] = None,
        pagination_page: typing.Optional[int] = None,
        pagination_page_size: typing.Optional[int] = None,
        pagination_start: typing.Optional[int] = None,
        pagination_limit: typing.Optional[int] = None,
        pagination_with_count: typing.Optional[bool] = None,
        filters_page_path_eq: typing.Optional[str] = None,
        filters_robots_index_eq: typing.Optional[bool] = None,
        filters_robots_follow_eq: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageMetadataListResponse]:
        """
        List entries of the Jentic instance's `page-metadata` collection. This is the collection-type list endpoint (`GET /{pluralApiId}`) with `pluralApiId = page-metadatas`.

        Parameters
        ----------
        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sort the response. Single field `sort=field:asc`, or multiple via `sort[0]=field:asc&sort[1]=other:desc`. Direction is `:asc` (default) or `:desc`.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.

        populate : typing.Optional[ListPageMetadataRequestPopulate]
            Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.

        status : typing.Optional[ListPageMetadataRequestStatus]
            Select the Draft & Publish status on reads.

        locale : typing.Optional[str]
            Select a locale (i18n plugin).

        publication_filter : typing.Optional[str]
            Select documents by how their draft and published versions relate.

        pagination_page : typing.Optional[int]
            Page-based pagination: page number. Cannot be combined with start/limit.

        pagination_page_size : typing.Optional[int]
            Page-based pagination: entries per page.

        pagination_start : typing.Optional[int]
            Offset-based pagination: index of the first entry. Cannot be combined with page/pageSize.

        pagination_limit : typing.Optional[int]
            Offset-based pagination: number of entries to return. Maximum is configurable per instance.

        pagination_with_count : typing.Optional[bool]
            Include the total count / page count in the pagination metadata.

        filters_page_path_eq : typing.Optional[str]
            Filter by exact page path.

        filters_robots_index_eq : typing.Optional[bool]
            Filter by robotsIndex flag.

        filters_robots_follow_eq : typing.Optional[bool]
            Filter by robotsFollow flag.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageMetadataListResponse]
            Paginated list of page-metadata entries.
        """
        _response = self._client_wrapper.httpx_client.request(
            "page-metadatas",
            method="GET",
            params={
                "sort": sort,
                "fields": fields,
                "populate": convert_and_respect_annotation_metadata(
                    object_=populate, annotation=ListPageMetadataRequestPopulate, direction="write"
                ),
                "status": status,
                "locale": locale,
                "publicationFilter": publication_filter,
                "pagination[page]": pagination_page,
                "pagination[pageSize]": pagination_page_size,
                "pagination[start]": pagination_start,
                "pagination[limit]": pagination_limit,
                "pagination[withCount]": pagination_with_count,
                "filters[pagePath][$eq]": filters_page_path_eq,
                "filters[robotsIndex][$eq]": filters_robots_index_eq,
                "filters[robotsFollow][$eq]": filters_robots_follow_eq,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageMetadataListResponse,
                    parse_obj_as(
                        type_=PageMetadataListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def create_page_metadata(
        self, *, data: PageMetadataAttributes, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PageMetadataSingleResponse]:
        """
        Create a `page-metadata` entry (`POST /{pluralApiId}`). Note: over REST the created entry is published even when `status=draft` is supplied; verify `publishedAt` on the response.

        Parameters
        ----------
        data : PageMetadataAttributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageMetadataSingleResponse]
            Created entry.
        """
        _response = self._client_wrapper.httpx_client.request(
            "page-metadatas",
            method="POST",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=PageMetadataAttributes, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageMetadataSingleResponse,
                    parse_obj_as(
                        type_=PageMetadataSingleResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_page_metadata(
        self,
        document_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        populate: typing.Optional[GetPageMetadataRequestPopulate] = None,
        status: typing.Optional[GetPageMetadataRequestStatus] = None,
        locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageMetadataSingleResponse]:
        """
        Retrieve a single `page-metadata` entry by documentId (`GET /{pluralApiId}/{documentId}`).

        Parameters
        ----------
        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.

        populate : typing.Optional[GetPageMetadataRequestPopulate]
            Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.

        status : typing.Optional[GetPageMetadataRequestStatus]
            Select the Draft & Publish status on reads.

        locale : typing.Optional[str]
            Select a locale (i18n plugin).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageMetadataSingleResponse]
            The page-metadata entry.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"page-metadatas/{encode_path_param(document_id)}",
            method="GET",
            params={
                "fields": fields,
                "populate": convert_and_respect_annotation_metadata(
                    object_=populate, annotation=GetPageMetadataRequestPopulate, direction="write"
                ),
                "status": status,
                "locale": locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageMetadataSingleResponse,
                    parse_obj_as(
                        type_=PageMetadataSingleResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def update_page_metadata(
        self, document_id: str, *, data: PageMetadataAttributes, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PageMetadataSingleResponse]:
        """
        Partially update a `page-metadata` entry by documentId (`PUT /{pluralApiId}/{documentId}`). Used to flip `robotsIndex` / `robotsFollow`. Note: updating over REST publishes the entry; there is no REST route to unpublish. Verify `publishedAt` on the response.

        Parameters
        ----------
        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        data : PageMetadataAttributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageMetadataSingleResponse]
            Updated entry.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"page-metadatas/{encode_path_param(document_id)}",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=PageMetadataAttributes, direction="write"
                ),
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
                    PageMetadataSingleResponse,
                    parse_obj_as(
                        type_=PageMetadataSingleResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def delete_page_metadata(
        self, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a `page-metadata` entry by documentId (`DELETE /{pluralApiId}/{documentId}`).

        Parameters
        ----------
        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"page-metadatas/{encode_path_param(document_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawPageMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_page_metadata(
        self,
        *,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        populate: typing.Optional[ListPageMetadataRequestPopulate] = None,
        status: typing.Optional[ListPageMetadataRequestStatus] = None,
        locale: typing.Optional[str] = None,
        publication_filter: typing.Optional[str] = None,
        pagination_page: typing.Optional[int] = None,
        pagination_page_size: typing.Optional[int] = None,
        pagination_start: typing.Optional[int] = None,
        pagination_limit: typing.Optional[int] = None,
        pagination_with_count: typing.Optional[bool] = None,
        filters_page_path_eq: typing.Optional[str] = None,
        filters_robots_index_eq: typing.Optional[bool] = None,
        filters_robots_follow_eq: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageMetadataListResponse]:
        """
        List entries of the Jentic instance's `page-metadata` collection. This is the collection-type list endpoint (`GET /{pluralApiId}`) with `pluralApiId = page-metadatas`.

        Parameters
        ----------
        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sort the response. Single field `sort=field:asc`, or multiple via `sort[0]=field:asc&sort[1]=other:desc`. Direction is `:asc` (default) or `:desc`.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.

        populate : typing.Optional[ListPageMetadataRequestPopulate]
            Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.

        status : typing.Optional[ListPageMetadataRequestStatus]
            Select the Draft & Publish status on reads.

        locale : typing.Optional[str]
            Select a locale (i18n plugin).

        publication_filter : typing.Optional[str]
            Select documents by how their draft and published versions relate.

        pagination_page : typing.Optional[int]
            Page-based pagination: page number. Cannot be combined with start/limit.

        pagination_page_size : typing.Optional[int]
            Page-based pagination: entries per page.

        pagination_start : typing.Optional[int]
            Offset-based pagination: index of the first entry. Cannot be combined with page/pageSize.

        pagination_limit : typing.Optional[int]
            Offset-based pagination: number of entries to return. Maximum is configurable per instance.

        pagination_with_count : typing.Optional[bool]
            Include the total count / page count in the pagination metadata.

        filters_page_path_eq : typing.Optional[str]
            Filter by exact page path.

        filters_robots_index_eq : typing.Optional[bool]
            Filter by robotsIndex flag.

        filters_robots_follow_eq : typing.Optional[bool]
            Filter by robotsFollow flag.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageMetadataListResponse]
            Paginated list of page-metadata entries.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "page-metadatas",
            method="GET",
            params={
                "sort": sort,
                "fields": fields,
                "populate": convert_and_respect_annotation_metadata(
                    object_=populate, annotation=ListPageMetadataRequestPopulate, direction="write"
                ),
                "status": status,
                "locale": locale,
                "publicationFilter": publication_filter,
                "pagination[page]": pagination_page,
                "pagination[pageSize]": pagination_page_size,
                "pagination[start]": pagination_start,
                "pagination[limit]": pagination_limit,
                "pagination[withCount]": pagination_with_count,
                "filters[pagePath][$eq]": filters_page_path_eq,
                "filters[robotsIndex][$eq]": filters_robots_index_eq,
                "filters[robotsFollow][$eq]": filters_robots_follow_eq,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageMetadataListResponse,
                    parse_obj_as(
                        type_=PageMetadataListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def create_page_metadata(
        self, *, data: PageMetadataAttributes, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PageMetadataSingleResponse]:
        """
        Create a `page-metadata` entry (`POST /{pluralApiId}`). Note: over REST the created entry is published even when `status=draft` is supplied; verify `publishedAt` on the response.

        Parameters
        ----------
        data : PageMetadataAttributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageMetadataSingleResponse]
            Created entry.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "page-metadatas",
            method="POST",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=PageMetadataAttributes, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageMetadataSingleResponse,
                    parse_obj_as(
                        type_=PageMetadataSingleResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_page_metadata(
        self,
        document_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        populate: typing.Optional[GetPageMetadataRequestPopulate] = None,
        status: typing.Optional[GetPageMetadataRequestStatus] = None,
        locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageMetadataSingleResponse]:
        """
        Retrieve a single `page-metadata` entry by documentId (`GET /{pluralApiId}/{documentId}`).

        Parameters
        ----------
        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.

        populate : typing.Optional[GetPageMetadataRequestPopulate]
            Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.

        status : typing.Optional[GetPageMetadataRequestStatus]
            Select the Draft & Publish status on reads.

        locale : typing.Optional[str]
            Select a locale (i18n plugin).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageMetadataSingleResponse]
            The page-metadata entry.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"page-metadatas/{encode_path_param(document_id)}",
            method="GET",
            params={
                "fields": fields,
                "populate": convert_and_respect_annotation_metadata(
                    object_=populate, annotation=GetPageMetadataRequestPopulate, direction="write"
                ),
                "status": status,
                "locale": locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageMetadataSingleResponse,
                    parse_obj_as(
                        type_=PageMetadataSingleResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def update_page_metadata(
        self, document_id: str, *, data: PageMetadataAttributes, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PageMetadataSingleResponse]:
        """
        Partially update a `page-metadata` entry by documentId (`PUT /{pluralApiId}/{documentId}`). Used to flip `robotsIndex` / `robotsFollow`. Note: updating over REST publishes the entry; there is no REST route to unpublish. Verify `publishedAt` on the response.

        Parameters
        ----------
        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        data : PageMetadataAttributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageMetadataSingleResponse]
            Updated entry.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"page-metadatas/{encode_path_param(document_id)}",
            method="PUT",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=PageMetadataAttributes, direction="write"
                ),
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
                    PageMetadataSingleResponse,
                    parse_obj_as(
                        type_=PageMetadataSingleResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def delete_page_metadata(
        self, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a `page-metadata` entry by documentId (`DELETE /{pluralApiId}/{documentId}`).

        Parameters
        ----------
        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"page-metadatas/{encode_path_param(document_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
