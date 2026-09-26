

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawKnowledgeGraphsClient, RawKnowledgeGraphsClient


OMIT = typing.cast(typing.Any, ...)


class KnowledgeGraphsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKnowledgeGraphsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKnowledgeGraphsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKnowledgeGraphsClient
        """
        return self._raw_client

    def list_public_knowledge_graphs(
        self, *, term: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        List all public BAGs

        Parameters
        ----------
        term : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.knowledge_graphs.list_public_knowledge_graphs()
        """
        _response = self._raw_client.list_public_knowledge_graphs(term=term, request_options=request_options)
        return _response.data

    def backend_list_project_kgs(
        self,
        proj_key: str,
        *,
        term: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        List all bags in the project, backend-aware

        Parameters
        ----------
        proj_key : str

        term : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.knowledge_graphs.backend_list_project_kgs(
            proj_key="proj_key",
        )
        """
        _response = self._raw_client.backend_list_project_kgs(proj_key, term=term, request_options=request_options)
        return _response.data

    def create_project_knowledge_graph(
        self,
        proj_key: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Create new BAG, backend-aware

        Parameters
        ----------
        proj_key : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.knowledge_graphs.create_project_knowledge_graph(
            proj_key="proj_key",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_project_knowledge_graph(
            proj_key, request=request, request_options=request_options
        )
        return _response.data

    def update_project_knowledge_graph_metadata(
        self,
        proj_key: str,
        bag_key: typing.Any,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update the metadata of a Knowledge graph

        Parameters
        ----------
        proj_key : str

        bag_key : typing.Any

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.knowledge_graphs.update_project_knowledge_graph_metadata(
            proj_key="proj_key",
            bag_key="bag_key",
            request={"string": {"key": "value"}},
        )
        """
        _response = self._raw_client.update_project_knowledge_graph_metadata(
            proj_key, bag_key, request=request, request_options=request_options
        )
        return _response.data


class AsyncKnowledgeGraphsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKnowledgeGraphsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKnowledgeGraphsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKnowledgeGraphsClient
        """
        return self._raw_client

    async def list_public_knowledge_graphs(
        self, *, term: typing.Optional[typing.Any] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        List all public BAGs

        Parameters
        ----------
        term : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.knowledge_graphs.list_public_knowledge_graphs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_public_knowledge_graphs(term=term, request_options=request_options)
        return _response.data

    async def backend_list_project_kgs(
        self,
        proj_key: str,
        *,
        term: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        List all bags in the project, backend-aware

        Parameters
        ----------
        proj_key : str

        term : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.knowledge_graphs.backend_list_project_kgs(
                proj_key="proj_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.backend_list_project_kgs(
            proj_key, term=term, request_options=request_options
        )
        return _response.data

    async def create_project_knowledge_graph(
        self,
        proj_key: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Create new BAG, backend-aware

        Parameters
        ----------
        proj_key : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.knowledge_graphs.create_project_knowledge_graph(
                proj_key="proj_key",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_project_knowledge_graph(
            proj_key, request=request, request_options=request_options
        )
        return _response.data

    async def update_project_knowledge_graph_metadata(
        self,
        proj_key: str,
        bag_key: typing.Any,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update the metadata of a Knowledge graph

        Parameters
        ----------
        proj_key : str

        bag_key : typing.Any

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.knowledge_graphs.update_project_knowledge_graph_metadata(
                proj_key="proj_key",
                bag_key="bag_key",
                request={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_project_knowledge_graph_metadata(
            proj_key, bag_key, request=request, request_options=request_options
        )
        return _response.data
