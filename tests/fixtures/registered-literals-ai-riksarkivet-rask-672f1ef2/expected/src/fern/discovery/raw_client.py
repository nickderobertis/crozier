

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.datasets import Datasets
from ..types.estate_graph import EstateGraph
from ..types.http_validation_error import HttpValidationError
from ..types.jobs import Jobs
from ..types.namespaces import Namespaces
from ..types.search_results import SearchResults
from pydantic import ValidationError


class RawDiscoveryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_datasets(
        self,
        *,
        namespace: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Datasets]:
        """
        Browse every dataset the caller may see — the lineage catalog's landing list.

        Governed (a dataset is shown only if the caller ``can_get_metadata`` on it), optionally filtered by
        ``?namespace=`` / ``?tag=``, and paginated over the *visible* set. This is the entry point the graph
        reads (``/datasets/{name}/...``) needed but could not provide — you no longer must know a name first.

        Parameters
        ----------
        namespace : typing.Optional[str]

        tag : typing.Optional[str]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Datasets]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "datasets",
            method="GET",
            params={
                "namespace": namespace,
                "tag": tag,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Datasets,
                    parse_obj_as(
                        type_=Datasets,
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

    def estate_graph(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EstateGraph]:
        """
        The whole visible lineage graph in ONE response — the graph page's bulk read.

        Before this the UI recomposed the estate graph client-side from the per-``{name}`` reads —
        one ``/datasets/{name}/graph`` (plus ``/producers``) per dataset per refresh, a 2N+-request
        storm at N datasets. Governance is identical to ``/datasets``: a node the caller may not see
        is dropped, and an edge needs BOTH endpoints visible (the same transitive-disclosure
        guarantee as the per-dataset graph). Nodes are capped at ``limit`` deterministically (sorted
        by name) with ``total``/``capped`` reporting the truth.

        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EstateGraph]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "graph",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EstateGraph,
                    parse_obj_as(
                        type_=EstateGraph,
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

    def list_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Jobs]:
        """
        The jobs (compute identities) that have run — governed by the datasets each wrote.

        A job is shown only if the caller can see every dataset it wrote (a read-only / output-less job is
        hidden when auth is on, mirroring how ``/events`` drops a dataset-less row). Auth off → pass-through.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Jobs]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Jobs,
                    parse_obj_as(
                        type_=Jobs,
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

    def list_namespaces(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Namespaces]:
        """
        The namespaces containing at least one dataset the caller may see (for a namespace-tree browse).

        Derived from the governed dataset set, so a namespace the caller can see no dataset in never appears.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Namespaces]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "namespaces",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Namespaces,
                    parse_obj_as(
                        type_=Namespaces,
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
        self, *, q: str, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SearchResults]:
        """
        Governed search over the discovery estate (P1 Search tier 1, 2026-07-11).

        Case-insensitive substring over dataset NAMES, NAMESPACES, governance TAGS, and the CURRENT
        COLUMN inventory — each hit says WHY it matched (``name`` / ``namespace`` / ``tag:…`` /
        ``column:…``), so "which tables have an embedding column" and "what's in layer=gold" are one
        query. Governance is identical to ``/datasets``: the visibility filter runs over the FULL hit
        set BEFORE the limit, so search can never disclose (or even count) tables outside the caller's
        reach. 📌 Tier 2 (Lance FTS + FLAT vector content search, the rask pattern) stays decision-
        pinned in docs/DECISIONS.md §9 behind its measured recall gate — this tier is metadata-only
        by design.

        Parameters
        ----------
        q : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchResults]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "search",
            method="GET",
            params={
                "q": q,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchResults,
                    parse_obj_as(
                        type_=SearchResults,
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


class AsyncRawDiscoveryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_datasets(
        self,
        *,
        namespace: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Datasets]:
        """
        Browse every dataset the caller may see — the lineage catalog's landing list.

        Governed (a dataset is shown only if the caller ``can_get_metadata`` on it), optionally filtered by
        ``?namespace=`` / ``?tag=``, and paginated over the *visible* set. This is the entry point the graph
        reads (``/datasets/{name}/...``) needed but could not provide — you no longer must know a name first.

        Parameters
        ----------
        namespace : typing.Optional[str]

        tag : typing.Optional[str]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Datasets]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "datasets",
            method="GET",
            params={
                "namespace": namespace,
                "tag": tag,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Datasets,
                    parse_obj_as(
                        type_=Datasets,
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

    async def estate_graph(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EstateGraph]:
        """
        The whole visible lineage graph in ONE response — the graph page's bulk read.

        Before this the UI recomposed the estate graph client-side from the per-``{name}`` reads —
        one ``/datasets/{name}/graph`` (plus ``/producers``) per dataset per refresh, a 2N+-request
        storm at N datasets. Governance is identical to ``/datasets``: a node the caller may not see
        is dropped, and an edge needs BOTH endpoints visible (the same transitive-disclosure
        guarantee as the per-dataset graph). Nodes are capped at ``limit`` deterministically (sorted
        by name) with ``total``/``capped`` reporting the truth.

        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EstateGraph]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "graph",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EstateGraph,
                    parse_obj_as(
                        type_=EstateGraph,
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

    async def list_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[Jobs]:
        """
        The jobs (compute identities) that have run — governed by the datasets each wrote.

        A job is shown only if the caller can see every dataset it wrote (a read-only / output-less job is
        hidden when auth is on, mirroring how ``/events`` drops a dataset-less row). Auth off → pass-through.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Jobs]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Jobs,
                    parse_obj_as(
                        type_=Jobs,
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

    async def list_namespaces(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Namespaces]:
        """
        The namespaces containing at least one dataset the caller may see (for a namespace-tree browse).

        Derived from the governed dataset set, so a namespace the caller can see no dataset in never appears.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Namespaces]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "namespaces",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Namespaces,
                    parse_obj_as(
                        type_=Namespaces,
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
        self, *, q: str, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SearchResults]:
        """
        Governed search over the discovery estate (P1 Search tier 1, 2026-07-11).

        Case-insensitive substring over dataset NAMES, NAMESPACES, governance TAGS, and the CURRENT
        COLUMN inventory — each hit says WHY it matched (``name`` / ``namespace`` / ``tag:…`` /
        ``column:…``), so "which tables have an embedding column" and "what's in layer=gold" are one
        query. Governance is identical to ``/datasets``: the visibility filter runs over the FULL hit
        set BEFORE the limit, so search can never disclose (or even count) tables outside the caller's
        reach. 📌 Tier 2 (Lance FTS + FLAT vector content search, the rask pattern) stays decision-
        pinned in docs/DECISIONS.md §9 behind its measured recall gate — this tier is metadata-only
        by design.

        Parameters
        ----------
        q : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchResults]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "search",
            method="GET",
            params={
                "q": q,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchResults,
                    parse_obj_as(
                        type_=SearchResults,
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
