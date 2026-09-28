

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..types.namespaces_get_response import NamespacesGetResponse
from ..types.resource_get_response import ResourceGetResponse
from ..types.resources_get_response import ResourcesGetResponse
from ..types.resources_kinds_get_response import ResourcesKindsGetResponse
from ..types.resources_search_get_response import ResourcesSearchGetResponse
from ..types.resources_sync_post_response import ResourcesSyncPostResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawResourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_resources_filtered_by_kind_and_optional_namespace(
        self,
        *,
        kind: str,
        api_version: str,
        namespace: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        offset: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResourcesGetResponse]:
        """
        List resources filtered by kind and optional namespace

        Parameters
        ----------
        kind : str
            Resource kind (e.g., Pod, Deployment)

        api_version : str
            API version (e.g., v1, apps/v1)

        namespace : typing.Optional[str]
            Filter by namespace

        limit : typing.Optional[float]
            Maximum results to return

        offset : typing.Optional[float]
            Offset for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResourcesGetResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/resources",
            method="GET",
            params={
                "kind": kind,
                "apiVersion": api_version,
                "namespace": namespace,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResourcesGetResponse,
                    parse_obj_as(
                        type_=ResourcesGetResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def list_all_resource_kinds_available_in_the_cluster_with_counts(
        self, *, namespace: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResourcesKindsGetResponse]:
        """
        List all resource kinds available in the cluster with counts

        Parameters
        ----------
        namespace : typing.Optional[str]
            Filter kinds by namespace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResourcesKindsGetResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/resources/kinds",
            method="GET",
            params={
                "namespace": namespace,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResourcesKindsGetResponse,
                    parse_obj_as(
                        type_=ResourcesKindsGetResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def search_for_resources_using_semantic_search(
        self, *, q: str, limit: float, offset: float, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResourcesSearchGetResponse]:
        """
        Search for resources using semantic search

        Parameters
        ----------
        q : str
            Search query

        limit : float
            Maximum results to return

        offset : float
            Offset for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResourcesSearchGetResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/resources/search",
            method="GET",
            params={
                "q": q,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResourcesSearchGetResponse,
                    parse_obj_as(
                        type_=ResourcesSearchGetResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def sync_resources_from_the_kubernetes_controller(
        self,
        *,
        upserts: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        deletes: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        is_resync: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResourcesSyncPostResponse]:
        """
        Sync resources from the Kubernetes controller

        Parameters
        ----------
        upserts : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Resources to upsert

        deletes : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Resources to delete (requires namespace, name, kind, apiVersion)

        is_resync : typing.Optional[bool]
            When true, performs full reconciliation - deletes resources not in upserts list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResourcesSyncPostResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/resources/sync",
            method="POST",
            json={
                "upserts": upserts,
                "deletes": deletes,
                "isResync": is_resync,
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
                    ResourcesSyncPostResponse,
                    parse_obj_as(
                        type_=ResourcesSyncPostResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_a_single_resource_with_full_details_including_live_status(
        self,
        *,
        kind: str,
        api_version: str,
        name: str,
        namespace: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResourceGetResponse]:
        """
        Get a single resource with full details including live status

        Parameters
        ----------
        kind : str
            Resource kind

        api_version : str
            API version

        name : str
            Resource name

        namespace : typing.Optional[str]
            Namespace (for namespaced resources)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResourceGetResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/resource",
            method="GET",
            params={
                "kind": kind,
                "apiVersion": api_version,
                "name": name,
                "namespace": namespace,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResourceGetResponse,
                    parse_obj_as(
                        type_=ResourceGetResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def list_all_namespaces_in_the_cluster(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NamespacesGetResponse]:
        """
        List all namespaces in the cluster

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NamespacesGetResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/namespaces",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamespacesGetResponse,
                    parse_obj_as(
                        type_=NamespacesGetResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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


class AsyncRawResourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_resources_filtered_by_kind_and_optional_namespace(
        self,
        *,
        kind: str,
        api_version: str,
        namespace: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        offset: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResourcesGetResponse]:
        """
        List resources filtered by kind and optional namespace

        Parameters
        ----------
        kind : str
            Resource kind (e.g., Pod, Deployment)

        api_version : str
            API version (e.g., v1, apps/v1)

        namespace : typing.Optional[str]
            Filter by namespace

        limit : typing.Optional[float]
            Maximum results to return

        offset : typing.Optional[float]
            Offset for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResourcesGetResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/resources",
            method="GET",
            params={
                "kind": kind,
                "apiVersion": api_version,
                "namespace": namespace,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResourcesGetResponse,
                    parse_obj_as(
                        type_=ResourcesGetResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def list_all_resource_kinds_available_in_the_cluster_with_counts(
        self, *, namespace: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResourcesKindsGetResponse]:
        """
        List all resource kinds available in the cluster with counts

        Parameters
        ----------
        namespace : typing.Optional[str]
            Filter kinds by namespace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResourcesKindsGetResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/resources/kinds",
            method="GET",
            params={
                "namespace": namespace,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResourcesKindsGetResponse,
                    parse_obj_as(
                        type_=ResourcesKindsGetResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def search_for_resources_using_semantic_search(
        self, *, q: str, limit: float, offset: float, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResourcesSearchGetResponse]:
        """
        Search for resources using semantic search

        Parameters
        ----------
        q : str
            Search query

        limit : float
            Maximum results to return

        offset : float
            Offset for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResourcesSearchGetResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/resources/search",
            method="GET",
            params={
                "q": q,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResourcesSearchGetResponse,
                    parse_obj_as(
                        type_=ResourcesSearchGetResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def sync_resources_from_the_kubernetes_controller(
        self,
        *,
        upserts: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        deletes: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        is_resync: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResourcesSyncPostResponse]:
        """
        Sync resources from the Kubernetes controller

        Parameters
        ----------
        upserts : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Resources to upsert

        deletes : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Resources to delete (requires namespace, name, kind, apiVersion)

        is_resync : typing.Optional[bool]
            When true, performs full reconciliation - deletes resources not in upserts list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResourcesSyncPostResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/resources/sync",
            method="POST",
            json={
                "upserts": upserts,
                "deletes": deletes,
                "isResync": is_resync,
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
                    ResourcesSyncPostResponse,
                    parse_obj_as(
                        type_=ResourcesSyncPostResponse,
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_a_single_resource_with_full_details_including_live_status(
        self,
        *,
        kind: str,
        api_version: str,
        name: str,
        namespace: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResourceGetResponse]:
        """
        Get a single resource with full details including live status

        Parameters
        ----------
        kind : str
            Resource kind

        api_version : str
            API version

        name : str
            Resource name

        namespace : typing.Optional[str]
            Namespace (for namespaced resources)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResourceGetResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/resource",
            method="GET",
            params={
                "kind": kind,
                "apiVersion": api_version,
                "name": name,
                "namespace": namespace,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResourceGetResponse,
                    parse_obj_as(
                        type_=ResourceGetResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def list_all_namespaces_in_the_cluster(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NamespacesGetResponse]:
        """
        List all namespaces in the cluster

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NamespacesGetResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/namespaces",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NamespacesGetResponse,
                    parse_obj_as(
                        type_=NamespacesGetResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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
