

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.datasets import Datasets
from ..types.estate_graph import EstateGraph
from ..types.jobs import Jobs
from ..types.namespaces import Namespaces
from ..types.search_results import SearchResults
from .raw_client import AsyncRawDiscoveryClient, RawDiscoveryClient


class DiscoveryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDiscoveryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDiscoveryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDiscoveryClient
        """
        return self._raw_client

    def list_datasets(
        self,
        *,
        namespace: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Datasets:
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
        Datasets
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.discovery.list_datasets()
        """
        _response = self._raw_client.list_datasets(
            namespace=namespace, tag=tag, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def estate_graph(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> EstateGraph:
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
        EstateGraph
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.discovery.estate_graph()
        """
        _response = self._raw_client.estate_graph(limit=limit, request_options=request_options)
        return _response.data

    def list_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> Jobs:
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
        Jobs
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.discovery.list_jobs()
        """
        _response = self._raw_client.list_jobs(request_options=request_options)
        return _response.data

    def list_namespaces(self, *, request_options: typing.Optional[RequestOptions] = None) -> Namespaces:
        """
        The namespaces containing at least one dataset the caller may see (for a namespace-tree browse).

        Derived from the governed dataset set, so a namespace the caller can see no dataset in never appears.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Namespaces
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.discovery.list_namespaces()
        """
        _response = self._raw_client.list_namespaces(request_options=request_options)
        return _response.data

    def search(
        self, *, q: str, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> SearchResults:
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
        SearchResults
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.discovery.search(
            q="q",
        )
        """
        _response = self._raw_client.search(q=q, limit=limit, request_options=request_options)
        return _response.data


class AsyncDiscoveryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDiscoveryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDiscoveryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDiscoveryClient
        """
        return self._raw_client

    async def list_datasets(
        self,
        *,
        namespace: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Datasets:
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
        Datasets
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.discovery.list_datasets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_datasets(
            namespace=namespace, tag=tag, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def estate_graph(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> EstateGraph:
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
        EstateGraph
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.discovery.estate_graph()


        asyncio.run(main())
        """
        _response = await self._raw_client.estate_graph(limit=limit, request_options=request_options)
        return _response.data

    async def list_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> Jobs:
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
        Jobs
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.discovery.list_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_jobs(request_options=request_options)
        return _response.data

    async def list_namespaces(self, *, request_options: typing.Optional[RequestOptions] = None) -> Namespaces:
        """
        The namespaces containing at least one dataset the caller may see (for a namespace-tree browse).

        Derived from the governed dataset set, so a namespace the caller can see no dataset in never appears.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Namespaces
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.discovery.list_namespaces()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_namespaces(request_options=request_options)
        return _response.data

    async def search(
        self, *, q: str, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> SearchResults:
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
        SearchResults
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dapr_api_token="YOUR_DAPR_API_TOKEN",
            lance_service_identity="YOUR_LANCE_SERVICE_IDENTITY",
            dapr_caller_app_id="YOUR_DAPR_CALLER_APP_ID",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.discovery.search(
                q="q",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search(q=q, limit=limit, request_options=request_options)
        return _response.data
