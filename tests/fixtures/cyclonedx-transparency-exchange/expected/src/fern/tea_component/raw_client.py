

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
from ..types.component import Component
from ..types.error_response import ErrorResponse
from ..types.identifier_type import IdentifierType
from ..types.paginated_component_release_response import PaginatedComponentReleaseResponse
from ..types.paginated_component_response import PaginatedComponentResponse
from ..types.uuid_ import Uuid
from .types.get_releases_by_component_id_request_sort_field import GetReleasesByComponentIdRequestSortField
from .types.get_releases_by_component_id_request_sort_order import GetReleasesByComponentIdRequestSortOrder
from .types.query_tea_components_request_sort_field import QueryTeaComponentsRequestSortField
from .types.query_tea_components_request_sort_order import QueryTeaComponentsRequestSortOrder
from pydantic import ValidationError


class RawTeaComponentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_tea_component_by_id(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Component]:
        """
        Get a TEA Component

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Component in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Component]
            Requested TEA Component found and returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"component/{encode_path_param(uuid_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Component,
                    parse_obj_as(
                        type_=Component,
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

    def get_releases_by_component_id(
        self,
        uuid_: Uuid,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_field: typing.Optional[GetReleasesByComponentIdRequestSortField] = None,
        sort_order: typing.Optional[GetReleasesByComponentIdRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedComponentReleaseResponse]:
        """
        Get releases of the component

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Component in the TEA server

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

        sort_field : typing.Optional[GetReleasesByComponentIdRequestSortField]
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

        sort_order : typing.Optional[GetReleasesByComponentIdRequestSortOrder]
            The direction of the sort.

            The selected sort order applies to both the primary `sortField` and the
            resource-specific deterministic secondary tie-breaker. For products, components,
            product releases, and component releases, the secondary key is `uuid`. For collections,
            the secondary key is `version` if additional tie-breaking is needed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedComponentReleaseResponse]
            A paginated response containing TEA Component Releases
        """
        _response = self._client_wrapper.httpx_client.request(
            f"component/{encode_path_param(uuid_)}/releases",
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
                    PaginatedComponentReleaseResponse,
                    parse_obj_as(
                        type_=PaginatedComponentReleaseResponse,
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

    def query_tea_components(
        self,
        *,
        id_type: typing.Optional[IdentifierType] = None,
        id_value: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_field: typing.Optional[QueryTeaComponentsRequestSortField] = None,
        sort_order: typing.Optional[QueryTeaComponentsRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedComponentResponse]:
        """
        Returns a list of TEA components. Note that multiple components may match.

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

        sort_field : typing.Optional[QueryTeaComponentsRequestSortField]
            The field by which to sort the results.

            Paginated results MUST be ordered first by the selected `sortField`, then by `uuid`
            as a deterministic secondary tie-breaker.

        sort_order : typing.Optional[QueryTeaComponentsRequestSortOrder]
            The direction of the sort.

            The selected sort order applies to both the primary `sortField` and the
            resource-specific deterministic secondary tie-breaker. For products, components,
            product releases, and component releases, the secondary key is `uuid`. For collections,
            the secondary key is `version` if additional tie-breaking is needed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedComponentResponse]
            A paginated response containing TEA Components
        """
        _response = self._client_wrapper.httpx_client.request(
            "components",
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
                    PaginatedComponentResponse,
                    parse_obj_as(
                        type_=PaginatedComponentResponse,
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


class AsyncRawTeaComponentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_tea_component_by_id(
        self, uuid_: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Component]:
        """
        Get a TEA Component

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Component in the TEA server

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Component]
            Requested TEA Component found and returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"component/{encode_path_param(uuid_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Component,
                    parse_obj_as(
                        type_=Component,
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

    async def get_releases_by_component_id(
        self,
        uuid_: Uuid,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_field: typing.Optional[GetReleasesByComponentIdRequestSortField] = None,
        sort_order: typing.Optional[GetReleasesByComponentIdRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedComponentReleaseResponse]:
        """
        Get releases of the component

        Parameters
        ----------
        uuid_ : Uuid
            UUID of TEA Component in the TEA server

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

        sort_field : typing.Optional[GetReleasesByComponentIdRequestSortField]
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

        sort_order : typing.Optional[GetReleasesByComponentIdRequestSortOrder]
            The direction of the sort.

            The selected sort order applies to both the primary `sortField` and the
            resource-specific deterministic secondary tie-breaker. For products, components,
            product releases, and component releases, the secondary key is `uuid`. For collections,
            the secondary key is `version` if additional tie-breaking is needed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedComponentReleaseResponse]
            A paginated response containing TEA Component Releases
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"component/{encode_path_param(uuid_)}/releases",
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
                    PaginatedComponentReleaseResponse,
                    parse_obj_as(
                        type_=PaginatedComponentReleaseResponse,
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

    async def query_tea_components(
        self,
        *,
        id_type: typing.Optional[IdentifierType] = None,
        id_value: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        sort_field: typing.Optional[QueryTeaComponentsRequestSortField] = None,
        sort_order: typing.Optional[QueryTeaComponentsRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedComponentResponse]:
        """
        Returns a list of TEA components. Note that multiple components may match.

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

        sort_field : typing.Optional[QueryTeaComponentsRequestSortField]
            The field by which to sort the results.

            Paginated results MUST be ordered first by the selected `sortField`, then by `uuid`
            as a deterministic secondary tie-breaker.

        sort_order : typing.Optional[QueryTeaComponentsRequestSortOrder]
            The direction of the sort.

            The selected sort order applies to both the primary `sortField` and the
            resource-specific deterministic secondary tie-breaker. For products, components,
            product releases, and component releases, the secondary key is `uuid`. For collections,
            the secondary key is `version` if additional tie-breaking is needed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedComponentResponse]
            A paginated response containing TEA Components
        """
        _response = await self._client_wrapper.httpx_client.request(
            "components",
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
                    PaginatedComponentResponse,
                    parse_obj_as(
                        type_=PaginatedComponentResponse,
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
