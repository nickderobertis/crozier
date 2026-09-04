

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
from ..errors.not_found_error import NotFoundError
from ..types.collection import Collection
from ..types.error_response import ErrorResponse
from ..types.identifier_type import IdentifierType
from ..types.paginated_collection_response import PaginatedCollectionResponse
from ..types.paginated_product_release_response import PaginatedProductReleaseResponse
from ..types.product_release import ProductRelease
from ..types.uuid_ import Uuid
from .types.get_collections_by_product_release_id_request_sort_field import (
    GetCollectionsByProductReleaseIdRequestSortField,
)
from .types.get_collections_by_product_release_id_request_sort_order import (
    GetCollectionsByProductReleaseIdRequestSortOrder,
)
from .types.get_releases_by_product_id_request_sort_field import GetReleasesByProductIdRequestSortField
from .types.get_releases_by_product_id_request_sort_order import GetReleasesByProductIdRequestSortOrder
from .types.query_tea_product_releases_request_sort_field import QueryTeaProductReleasesRequestSortField
from .types.query_tea_product_releases_request_sort_order import QueryTeaProductReleasesRequestSortOrder
from pydantic import ValidationError


class RawTeaProductReleaseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_releases_by_product_id(
        self,
        uuid_: Uuid,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_field: typing.Optional[GetReleasesByProductIdRequestSortField] = None,
        sort_order: typing.Optional[GetReleasesByProductIdRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedProductReleaseResponse]:
        """
        Get releases of the product

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Product in the TEA server

        page_size : typing.Optional[int]
            The maximum number of results to return.

        page_token : typing.Optional[str]
            An opaque continuation token produced by a previous response.
            This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
            Clients MUST NOT parse, construct, or modify this token.

            The token represents continuation state for the original query, including
            `sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
            and path parameters such as parent `uuid`.
            When `pageToken` is supplied, clients MUST NOT change those result-affecting query
            parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
            parameters conflict with the token state. To change any result-affecting parameter,
            clients MUST start a new pagination sequence without `pageToken`.

            A `pageToken` is only valid with the same request path and same path parameter values
            used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
            resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
            when a `pageToken` is used with a different path or different path parameter values.

            Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
            `pageToken` values.

        sort_field : typing.Optional[GetReleasesByProductIdRequestSortField]
            The field by which to sort the results.

            Paginated results MUST be ordered first by the selected `sortField`, then by `uuid`
            as a deterministic secondary tie-breaker.

            When `version` is selected, ordering is by the stored version string according to
            the server's documented string collation; semantic-version precedence is not implied.
            Servers MUST apply a stable and deterministic string collation for version sorting,
            and the same collation MUST be used consistently across pages for a pagination sequence.

            When `releaseDate` is selected, releases without a `releaseDate` MUST be ordered
            consistently. Missing `releaseDate` values sort after populated `releaseDate` values
            for ascending order and before populated `releaseDate` values for descending order.

        sort_order : typing.Optional[GetReleasesByProductIdRequestSortOrder]
            The direction of the sort.

            The selected sort order applies to both the primary `sortField` and the
            resource-specific deterministic secondary tie-breaker. For products, components,
            product releases, and component releases, the secondary key is `uuid`. For collections,
            the secondary key is `version` if additional tie-breaking is needed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedProductReleaseResponse]
            A paginated response containing TEA Product Releases
        """
        _response = self._client_wrapper.httpx_client.request(
            f"product/{encode_path_param(uuid_)}/releases",
            method="GET",
            params={
                "pageSize": page_size,
                "pageToken": page_token,
                "sortField": sort_field,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedProductReleaseResponse,
                    parse_obj_as(
                        type_=PaginatedProductReleaseResponse,
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

    def get_tea_product_release_by_uuid(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProductRelease]:
        """
        Get a TEA Product Release

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Product Release in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProductRelease]
            Requested TEA Product Release found and returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"productRelease/{encode_path_param(uuid_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProductRelease,
                    parse_obj_as(
                        type_=ProductRelease,
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

    def query_tea_product_releases(
        self,
        *,
        id_type: typing.Optional[IdentifierType] = None,
        id_value: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_field: typing.Optional[QueryTeaProductReleasesRequestSortField] = None,
        sort_order: typing.Optional[QueryTeaProductReleasesRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedProductReleaseResponse]:
        """
        Returns a list of TEA product releases. Note that multiple product releases may match.

        Parameters
        ----------
        id_type : typing.Optional[IdentifierType]
            Type of identifier specified in the `idValue` parameter

        id_value : typing.Optional[str]
            If present, only the objects with the given identifier value will be returned.

        page_size : typing.Optional[int]
            The maximum number of results to return.

        page_token : typing.Optional[str]
            An opaque continuation token produced by a previous response.
            This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
            Clients MUST NOT parse, construct, or modify this token.

            The token represents continuation state for the original query, including
            `sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
            and path parameters such as parent `uuid`.
            When `pageToken` is supplied, clients MUST NOT change those result-affecting query
            parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
            parameters conflict with the token state. To change any result-affecting parameter,
            clients MUST start a new pagination sequence without `pageToken`.

            A `pageToken` is only valid with the same request path and same path parameter values
            used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
            resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
            when a `pageToken` is used with a different path or different path parameter values.

            Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
            `pageToken` values.

        sort_field : typing.Optional[QueryTeaProductReleasesRequestSortField]
            The field by which to sort the results.

            Paginated results MUST be ordered first by the selected `sortField`, then by `uuid`
            as a deterministic secondary tie-breaker.

            When `version` is selected, ordering is by the stored version string according to
            the server's documented string collation; semantic-version precedence is not implied.
            Servers MUST apply a stable and deterministic string collation for version sorting,
            and the same collation MUST be used consistently across pages for a pagination sequence.

            When `releaseDate` is selected, releases without a `releaseDate` MUST be ordered
            consistently. Missing `releaseDate` values sort after populated `releaseDate` values
            for ascending order and before populated `releaseDate` values for descending order.

        sort_order : typing.Optional[QueryTeaProductReleasesRequestSortOrder]
            The direction of the sort.

            The selected sort order applies to both the primary `sortField` and the
            resource-specific deterministic secondary tie-breaker. For products, components,
            product releases, and component releases, the secondary key is `uuid`. For collections,
            the secondary key is `version` if additional tie-breaking is needed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedProductReleaseResponse]
            A paginated response containing TEA Product Releases
        """
        _response = self._client_wrapper.httpx_client.request(
            "productReleases",
            method="GET",
            params={
                "idType": id_type,
                "idValue": id_value,
                "pageSize": page_size,
                "pageToken": page_token,
                "sortField": sort_field,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedProductReleaseResponse,
                    parse_obj_as(
                        type_=PaginatedProductReleaseResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_latest_collection_for_product_release(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Collection]:
        """
        Get the latest TEA Collection belonging to the TEA Product Release

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Product Release in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Collection]
            Requested TEA Collection found and returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"productRelease/{encode_path_param(uuid_)}/collection/latest",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collection,
                    parse_obj_as(
                        type_=Collection,
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

    def get_collections_by_product_release_id(
        self,
        uuid_: Uuid,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_field: typing.Optional[GetCollectionsByProductReleaseIdRequestSortField] = None,
        sort_order: typing.Optional[GetCollectionsByProductReleaseIdRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedCollectionResponse]:
        """
        Get the TEA Collections belonging to the TEA Product Release

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Product Release in the TEA server

        page_size : typing.Optional[int]
            The maximum number of results to return.

        page_token : typing.Optional[str]
            An opaque continuation token produced by a previous response.
            This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
            Clients MUST NOT parse, construct, or modify this token.

            The token represents continuation state for the original query, including
            `sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
            and path parameters such as parent `uuid`.
            When `pageToken` is supplied, clients MUST NOT change those result-affecting query
            parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
            parameters conflict with the token state. To change any result-affecting parameter,
            clients MUST start a new pagination sequence without `pageToken`.

            A `pageToken` is only valid with the same request path and same path parameter values
            used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
            resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
            when a `pageToken` is used with a different path or different path parameter values.

            Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
            `pageToken` values.

        sort_field : typing.Optional[GetCollectionsByProductReleaseIdRequestSortField]
            The field by which to sort the results.

            Paginated collection results MUST be ordered first by the selected `sortField`,
            then by `version` as the deterministic secondary key if additional tie-breaking
            is needed. Collection UUIDs are not used as tie-breakers because collection UUIDs
            match the associated release UUID and can be shared across collection revisions.

            The only currently supported collection `sortField` is `version`, so the secondary
            `version` key is redundant unless additional collection sort fields are added later.

        sort_order : typing.Optional[GetCollectionsByProductReleaseIdRequestSortOrder]
            The direction of the sort.

            The selected sort order applies to both the primary `sortField` and the
            resource-specific deterministic secondary tie-breaker. For products, components,
            product releases, and component releases, the secondary key is `uuid`. For collections,
            the secondary key is `version` if additional tie-breaking is needed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedCollectionResponse]
            A paginated response containing TEA Collections
        """
        _response = self._client_wrapper.httpx_client.request(
            f"productRelease/{encode_path_param(uuid_)}/collections",
            method="GET",
            params={
                "pageSize": page_size,
                "pageToken": page_token,
                "sortField": sort_field,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedCollectionResponse,
                    parse_obj_as(
                        type_=PaginatedCollectionResponse,
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

    def get_collection_for_product_release(
        self, uuid_: Uuid, collection_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Collection]:
        """
        Get a specific Collection (by version) for a TEA Product Release by its UUID

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Product Release in the TEA server

        collection_version : int
            Version of TEA Collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Collection]
            Requested TEA Collection Version found and returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"productRelease/{encode_path_param(uuid_)}/collection/{encode_path_param(collection_version)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collection,
                    parse_obj_as(
                        type_=Collection,
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


class AsyncRawTeaProductReleaseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_releases_by_product_id(
        self,
        uuid_: Uuid,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_field: typing.Optional[GetReleasesByProductIdRequestSortField] = None,
        sort_order: typing.Optional[GetReleasesByProductIdRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedProductReleaseResponse]:
        """
        Get releases of the product

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Product in the TEA server

        page_size : typing.Optional[int]
            The maximum number of results to return.

        page_token : typing.Optional[str]
            An opaque continuation token produced by a previous response.
            This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
            Clients MUST NOT parse, construct, or modify this token.

            The token represents continuation state for the original query, including
            `sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
            and path parameters such as parent `uuid`.
            When `pageToken` is supplied, clients MUST NOT change those result-affecting query
            parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
            parameters conflict with the token state. To change any result-affecting parameter,
            clients MUST start a new pagination sequence without `pageToken`.

            A `pageToken` is only valid with the same request path and same path parameter values
            used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
            resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
            when a `pageToken` is used with a different path or different path parameter values.

            Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
            `pageToken` values.

        sort_field : typing.Optional[GetReleasesByProductIdRequestSortField]
            The field by which to sort the results.

            Paginated results MUST be ordered first by the selected `sortField`, then by `uuid`
            as a deterministic secondary tie-breaker.

            When `version` is selected, ordering is by the stored version string according to
            the server's documented string collation; semantic-version precedence is not implied.
            Servers MUST apply a stable and deterministic string collation for version sorting,
            and the same collation MUST be used consistently across pages for a pagination sequence.

            When `releaseDate` is selected, releases without a `releaseDate` MUST be ordered
            consistently. Missing `releaseDate` values sort after populated `releaseDate` values
            for ascending order and before populated `releaseDate` values for descending order.

        sort_order : typing.Optional[GetReleasesByProductIdRequestSortOrder]
            The direction of the sort.

            The selected sort order applies to both the primary `sortField` and the
            resource-specific deterministic secondary tie-breaker. For products, components,
            product releases, and component releases, the secondary key is `uuid`. For collections,
            the secondary key is `version` if additional tie-breaking is needed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedProductReleaseResponse]
            A paginated response containing TEA Product Releases
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"product/{encode_path_param(uuid_)}/releases",
            method="GET",
            params={
                "pageSize": page_size,
                "pageToken": page_token,
                "sortField": sort_field,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedProductReleaseResponse,
                    parse_obj_as(
                        type_=PaginatedProductReleaseResponse,
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

    async def get_tea_product_release_by_uuid(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProductRelease]:
        """
        Get a TEA Product Release

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Product Release in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProductRelease]
            Requested TEA Product Release found and returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"productRelease/{encode_path_param(uuid_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProductRelease,
                    parse_obj_as(
                        type_=ProductRelease,
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

    async def query_tea_product_releases(
        self,
        *,
        id_type: typing.Optional[IdentifierType] = None,
        id_value: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_field: typing.Optional[QueryTeaProductReleasesRequestSortField] = None,
        sort_order: typing.Optional[QueryTeaProductReleasesRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedProductReleaseResponse]:
        """
        Returns a list of TEA product releases. Note that multiple product releases may match.

        Parameters
        ----------
        id_type : typing.Optional[IdentifierType]
            Type of identifier specified in the `idValue` parameter

        id_value : typing.Optional[str]
            If present, only the objects with the given identifier value will be returned.

        page_size : typing.Optional[int]
            The maximum number of results to return.

        page_token : typing.Optional[str]
            An opaque continuation token produced by a previous response.
            This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
            Clients MUST NOT parse, construct, or modify this token.

            The token represents continuation state for the original query, including
            `sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
            and path parameters such as parent `uuid`.
            When `pageToken` is supplied, clients MUST NOT change those result-affecting query
            parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
            parameters conflict with the token state. To change any result-affecting parameter,
            clients MUST start a new pagination sequence without `pageToken`.

            A `pageToken` is only valid with the same request path and same path parameter values
            used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
            resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
            when a `pageToken` is used with a different path or different path parameter values.

            Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
            `pageToken` values.

        sort_field : typing.Optional[QueryTeaProductReleasesRequestSortField]
            The field by which to sort the results.

            Paginated results MUST be ordered first by the selected `sortField`, then by `uuid`
            as a deterministic secondary tie-breaker.

            When `version` is selected, ordering is by the stored version string according to
            the server's documented string collation; semantic-version precedence is not implied.
            Servers MUST apply a stable and deterministic string collation for version sorting,
            and the same collation MUST be used consistently across pages for a pagination sequence.

            When `releaseDate` is selected, releases without a `releaseDate` MUST be ordered
            consistently. Missing `releaseDate` values sort after populated `releaseDate` values
            for ascending order and before populated `releaseDate` values for descending order.

        sort_order : typing.Optional[QueryTeaProductReleasesRequestSortOrder]
            The direction of the sort.

            The selected sort order applies to both the primary `sortField` and the
            resource-specific deterministic secondary tie-breaker. For products, components,
            product releases, and component releases, the secondary key is `uuid`. For collections,
            the secondary key is `version` if additional tie-breaking is needed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedProductReleaseResponse]
            A paginated response containing TEA Product Releases
        """
        _response = await self._client_wrapper.httpx_client.request(
            "productReleases",
            method="GET",
            params={
                "idType": id_type,
                "idValue": id_value,
                "pageSize": page_size,
                "pageToken": page_token,
                "sortField": sort_field,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedProductReleaseResponse,
                    parse_obj_as(
                        type_=PaginatedProductReleaseResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_latest_collection_for_product_release(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Collection]:
        """
        Get the latest TEA Collection belonging to the TEA Product Release

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Product Release in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Collection]
            Requested TEA Collection found and returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"productRelease/{encode_path_param(uuid_)}/collection/latest",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collection,
                    parse_obj_as(
                        type_=Collection,
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

    async def get_collections_by_product_release_id(
        self,
        uuid_: Uuid,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_field: typing.Optional[GetCollectionsByProductReleaseIdRequestSortField] = None,
        sort_order: typing.Optional[GetCollectionsByProductReleaseIdRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedCollectionResponse]:
        """
        Get the TEA Collections belonging to the TEA Product Release

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Product Release in the TEA server

        page_size : typing.Optional[int]
            The maximum number of results to return.

        page_token : typing.Optional[str]
            An opaque continuation token produced by a previous response.
            This token MUST be copied verbatim from the `nextPageToken` value returned by the previous response.
            Clients MUST NOT parse, construct, or modify this token.

            The token represents continuation state for the original query, including
            `sortField`, `sortOrder`, result-affecting filters such as `idType` and `idValue`,
            and path parameters such as parent `uuid`.
            When `pageToken` is supplied, clients MUST NOT change those result-affecting query
            parameters. Servers MUST return `400 Bad Request` if supplied result-affecting query
            parameters conflict with the token state. To change any result-affecting parameter,
            clients MUST start a new pagination sequence without `pageToken`.

            A `pageToken` is only valid with the same request path and same path parameter values
            used to obtain it. Clients MUST NOT reuse a `pageToken` across different parent
            resource paths or different path `uuid` values. Servers MUST return `400 Bad Request`
            when a `pageToken` is used with a different path or different path parameter values.

            Servers MUST return `400 Bad Request` for malformed, invalid, expired, or conflicting
            `pageToken` values.

        sort_field : typing.Optional[GetCollectionsByProductReleaseIdRequestSortField]
            The field by which to sort the results.

            Paginated collection results MUST be ordered first by the selected `sortField`,
            then by `version` as the deterministic secondary key if additional tie-breaking
            is needed. Collection UUIDs are not used as tie-breakers because collection UUIDs
            match the associated release UUID and can be shared across collection revisions.

            The only currently supported collection `sortField` is `version`, so the secondary
            `version` key is redundant unless additional collection sort fields are added later.

        sort_order : typing.Optional[GetCollectionsByProductReleaseIdRequestSortOrder]
            The direction of the sort.

            The selected sort order applies to both the primary `sortField` and the
            resource-specific deterministic secondary tie-breaker. For products, components,
            product releases, and component releases, the secondary key is `uuid`. For collections,
            the secondary key is `version` if additional tie-breaking is needed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedCollectionResponse]
            A paginated response containing TEA Collections
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"productRelease/{encode_path_param(uuid_)}/collections",
            method="GET",
            params={
                "pageSize": page_size,
                "pageToken": page_token,
                "sortField": sort_field,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedCollectionResponse,
                    parse_obj_as(
                        type_=PaginatedCollectionResponse,
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

    async def get_collection_for_product_release(
        self, uuid_: Uuid, collection_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Collection]:
        """
        Get a specific Collection (by version) for a TEA Product Release by its UUID

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Product Release in the TEA server

        collection_version : int
            Version of TEA Collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Collection]
            Requested TEA Collection Version found and returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"productRelease/{encode_path_param(uuid_)}/collection/{encode_path_param(collection_version)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Collection,
                    parse_obj_as(
                        type_=Collection,
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
