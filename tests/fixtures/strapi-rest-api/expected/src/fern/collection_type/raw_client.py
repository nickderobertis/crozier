

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
from ..types.entry_list_response import EntryListResponse
from ..types.entry_single_response import EntrySingleResponse
from ..types.error_response import ErrorResponse
from ..types.get_entry_request_populate import GetEntryRequestPopulate
from ..types.list_entries_request_populate import ListEntriesRequestPopulate
from .types.get_entry_request_status import GetEntryRequestStatus
from .types.list_entries_request_status import ListEntriesRequestStatus
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCollectionTypeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_entries(
        self,
        api_id: str,
        *,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        populate: typing.Optional[ListEntriesRequestPopulate] = None,
        status: typing.Optional[ListEntriesRequestStatus] = None,
        locale: typing.Optional[str] = None,
        publication_filter: typing.Optional[str] = None,
        pagination_page: typing.Optional[int] = None,
        pagination_page_size: typing.Optional[int] = None,
        pagination_start: typing.Optional[int] = None,
        pagination_limit: typing.Optional[int] = None,
        pagination_with_count: typing.Optional[bool] = None,
        filters: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntryListResponse]:
        """
        For a collection type (`apiId` = plural API ID, e.g. `articles`, `page-metadatas`) this lists entries with filtering, sorting, field selection, population, pagination, and status. For a single type (`apiId` = singular API ID, e.g. `homepage`) this returns the one global entry; the list query parameters do not apply. Collection and single types share this path position, so they are described by one templated path.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sort the response. Single field `sort=field:asc`, or multiple via `sort[0]=field:asc&sort[1]=other:desc`. Direction is `:asc` (default) or `:desc`.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.

        populate : typing.Optional[ListEntriesRequestPopulate]
            Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.

        status : typing.Optional[ListEntriesRequestStatus]
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

        filters : typing.Optional[typing.Dict[str, typing.Any]]
            Filter the response. Use bracket syntax `filters[field][$operator]=value`. Operators: $eq, $eqi, $ne, $nei, $lt, $lte, $gt, $gte, $in, $notIn, $contains, $notContains, $containsi, $notContainsi, $startsWith, $startsWithi, $endsWith, $endsWithi, $null, $notNull, $between, $or, $and, $not.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntryListResponse]
            Paginated list of entries.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(api_id)}",
            method="GET",
            params={
                "sort": sort,
                "fields": fields,
                "populate": convert_and_respect_annotation_metadata(
                    object_=populate, annotation=ListEntriesRequestPopulate, direction="write"
                ),
                "status": status,
                "locale": locale,
                "publicationFilter": publication_filter,
                "pagination[page]": pagination_page,
                "pagination[pageSize]": pagination_page_size,
                "pagination[start]": pagination_start,
                "pagination[limit]": pagination_limit,
                "pagination[withCount]": pagination_with_count,
                "filters": filters,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntryListResponse,
                    parse_obj_as(
                        type_=EntryListResponse,
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

    def create_entry(
        self,
        api_id: str,
        *,
        data: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntrySingleResponse]:
        """
        Create an entry of a collection type. The request body wraps attributes under a `data` key. Not applicable to single types (use PUT). Note: over REST the entry is auto-published even with `status=draft`; verify `publishedAt` on the response.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        data : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntrySingleResponse]
            Created entry.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(api_id)}",
            method="POST",
            json={
                "data": data,
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
                    EntrySingleResponse,
                    parse_obj_as(
                        type_=EntrySingleResponse,
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

    def get_entry(
        self,
        api_id: str,
        document_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        populate: typing.Optional[GetEntryRequestPopulate] = None,
        status: typing.Optional[GetEntryRequestStatus] = None,
        locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntrySingleResponse]:
        """
        Retrieve a single collection-type entry by its `documentId`.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.

        populate : typing.Optional[GetEntryRequestPopulate]
            Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.

        status : typing.Optional[GetEntryRequestStatus]
            Select the Draft & Publish status on reads.

        locale : typing.Optional[str]
            Select a locale (i18n plugin).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntrySingleResponse]
            The entry.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(api_id)}/{encode_path_param(document_id)}",
            method="GET",
            params={
                "fields": fields,
                "populate": convert_and_respect_annotation_metadata(
                    object_=populate, annotation=GetEntryRequestPopulate, direction="write"
                ),
                "status": status,
                "locale": locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntrySingleResponse,
                    parse_obj_as(
                        type_=EntrySingleResponse,
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

    def update_entry(
        self,
        api_id: str,
        document_id: str,
        *,
        data: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntrySingleResponse]:
        """
        Partially update a collection-type entry by `documentId`. Note: updating over REST publishes the entry; there is no REST route to unpublish.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        data : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntrySingleResponse]
            Updated entry.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(api_id)}/{encode_path_param(document_id)}",
            method="PUT",
            json={
                "data": data,
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
                    EntrySingleResponse,
                    parse_obj_as(
                        type_=EntrySingleResponse,
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

    def delete_entry(
        self, api_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a collection-type entry by `documentId`.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(api_id)}/{encode_path_param(document_id)}",
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


class AsyncRawCollectionTypeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_entries(
        self,
        api_id: str,
        *,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        populate: typing.Optional[ListEntriesRequestPopulate] = None,
        status: typing.Optional[ListEntriesRequestStatus] = None,
        locale: typing.Optional[str] = None,
        publication_filter: typing.Optional[str] = None,
        pagination_page: typing.Optional[int] = None,
        pagination_page_size: typing.Optional[int] = None,
        pagination_start: typing.Optional[int] = None,
        pagination_limit: typing.Optional[int] = None,
        pagination_with_count: typing.Optional[bool] = None,
        filters: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntryListResponse]:
        """
        For a collection type (`apiId` = plural API ID, e.g. `articles`, `page-metadatas`) this lists entries with filtering, sorting, field selection, population, pagination, and status. For a single type (`apiId` = singular API ID, e.g. `homepage`) this returns the one global entry; the list query parameters do not apply. Collection and single types share this path position, so they are described by one templated path.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sort the response. Single field `sort=field:asc`, or multiple via `sort[0]=field:asc&sort[1]=other:desc`. Direction is `:asc` (default) or `:desc`.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.

        populate : typing.Optional[ListEntriesRequestPopulate]
            Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.

        status : typing.Optional[ListEntriesRequestStatus]
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

        filters : typing.Optional[typing.Dict[str, typing.Any]]
            Filter the response. Use bracket syntax `filters[field][$operator]=value`. Operators: $eq, $eqi, $ne, $nei, $lt, $lte, $gt, $gte, $in, $notIn, $contains, $notContains, $containsi, $notContainsi, $startsWith, $startsWithi, $endsWith, $endsWithi, $null, $notNull, $between, $or, $and, $not.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntryListResponse]
            Paginated list of entries.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(api_id)}",
            method="GET",
            params={
                "sort": sort,
                "fields": fields,
                "populate": convert_and_respect_annotation_metadata(
                    object_=populate, annotation=ListEntriesRequestPopulate, direction="write"
                ),
                "status": status,
                "locale": locale,
                "publicationFilter": publication_filter,
                "pagination[page]": pagination_page,
                "pagination[pageSize]": pagination_page_size,
                "pagination[start]": pagination_start,
                "pagination[limit]": pagination_limit,
                "pagination[withCount]": pagination_with_count,
                "filters": filters,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntryListResponse,
                    parse_obj_as(
                        type_=EntryListResponse,
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

    async def create_entry(
        self,
        api_id: str,
        *,
        data: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntrySingleResponse]:
        """
        Create an entry of a collection type. The request body wraps attributes under a `data` key. Not applicable to single types (use PUT). Note: over REST the entry is auto-published even with `status=draft`; verify `publishedAt` on the response.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        data : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntrySingleResponse]
            Created entry.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(api_id)}",
            method="POST",
            json={
                "data": data,
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
                    EntrySingleResponse,
                    parse_obj_as(
                        type_=EntrySingleResponse,
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

    async def get_entry(
        self,
        api_id: str,
        document_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        populate: typing.Optional[GetEntryRequestPopulate] = None,
        status: typing.Optional[GetEntryRequestStatus] = None,
        locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntrySingleResponse]:
        """
        Retrieve a single collection-type entry by its `documentId`.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Select only specific fields to return, e.g. `fields[0]=title&fields[1]=description`. Does not apply to relational/media/component/dynamic-zone fields.

        populate : typing.Optional[GetEntryRequestPopulate]
            Populate relations, media, components, and dynamic zones (excluded by default). `populate=*` for all one level deep, or bracket syntax for specific/nested relations.

        status : typing.Optional[GetEntryRequestStatus]
            Select the Draft & Publish status on reads.

        locale : typing.Optional[str]
            Select a locale (i18n plugin).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntrySingleResponse]
            The entry.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(api_id)}/{encode_path_param(document_id)}",
            method="GET",
            params={
                "fields": fields,
                "populate": convert_and_respect_annotation_metadata(
                    object_=populate, annotation=GetEntryRequestPopulate, direction="write"
                ),
                "status": status,
                "locale": locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntrySingleResponse,
                    parse_obj_as(
                        type_=EntrySingleResponse,
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

    async def update_entry(
        self,
        api_id: str,
        document_id: str,
        *,
        data: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntrySingleResponse]:
        """
        Partially update a collection-type entry by `documentId`. Note: updating over REST publishes the entry; there is no REST route to unpublish.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        data : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntrySingleResponse]
            Updated entry.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(api_id)}/{encode_path_param(document_id)}",
            method="PUT",
            json={
                "data": data,
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
                    EntrySingleResponse,
                    parse_obj_as(
                        type_=EntrySingleResponse,
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

    async def delete_entry(
        self, api_id: str, document_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a collection-type entry by `documentId`.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        document_id : str
            Strapi 5 document identifier (string), stable across locales and draft/published versions.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(api_id)}/{encode_path_param(document_id)}",
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
