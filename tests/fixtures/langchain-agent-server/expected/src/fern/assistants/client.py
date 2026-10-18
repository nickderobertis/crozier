

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.assistant import Assistant
from ..types.get_assistant_graph_assistants_assistant_id_graph_get_request_xray import (
    GetAssistantGraphAssistantsAssistantIdGraphGetRequestXray,
)
from ..types.graph_schema import GraphSchema
from ..types.subgraphs import Subgraphs
from .raw_client import AsyncRawAssistantsClient, RawAssistantsClient
from .types.assistant_create_if_exists import AssistantCreateIfExists
from .types.assistant_search_request_select_item import AssistantSearchRequestSelectItem
from .types.assistant_search_request_sort_by import AssistantSearchRequestSortBy
from .types.assistant_search_request_sort_order import AssistantSearchRequestSortOrder


OMIT = typing.cast(typing.Any, ...)


class AssistantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssistantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssistantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssistantsClient
        """
        return self._raw_client

    def create_assistant(
        self,
        *,
        graph_id: str,
        assistant_id: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        if_exists: typing.Optional[AssistantCreateIfExists] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Assistant:
        """
        Create an assistant.

        An initial version of the assistant will be created and the assistant is set to that version. To change versions, use the `POST /assistants/{assistant_id}/latest` endpoint.

        Parameters
        ----------
        graph_id : str
            The ID of the graph the assistant should use. The graph ID is normally set in your langgraph.json configuration.

        assistant_id : typing.Optional[str]
            The ID of the assistant. If not provided, a random UUID will be generated.

        config : typing.Optional[typing.Dict[str, typing.Any]]
            Configuration to use for the graph. Useful when graph is configurable and you want to create different assistants based on different configurations.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to add to assistant.

        if_exists : typing.Optional[AssistantCreateIfExists]
            How to handle duplicate creation. Must be either 'raise' (raise error if duplicate), or 'do_nothing' (return existing assistant).

        name : typing.Optional[str]
            The name of the assistant. Defaults to 'Untitled'.

        description : typing.Optional[str]
            The description of the assistant. Defaults to null.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Assistant
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.assistants.create_assistant(
            graph_id="graph_id",
        )
        """
        _response = self._raw_client.create_assistant(
            graph_id=graph_id,
            assistant_id=assistant_id,
            config=config,
            context=context,
            metadata=metadata,
            if_exists=if_exists,
            name=name,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def search_assistants(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        graph_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[AssistantSearchRequestSortBy] = OMIT,
        sort_order: typing.Optional[AssistantSearchRequestSortOrder] = OMIT,
        select: typing.Optional[typing.Sequence[AssistantSearchRequestSelectItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Assistant]:
        """
        Search for assistants.

        This endpoint also functions as the endpoint to list all assistants.

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to filter by. Exact match filter for each KV pair.

        graph_id : typing.Optional[str]
            The ID of the graph to filter by. The graph ID is normally set in your langgraph.json configuration.

        name : typing.Optional[str]
            Name of the assistant to filter by. The filtering logic will match (case insensitive) assistants where 'name' is a substring of the assistant name.

        limit : typing.Optional[int]
            The maximum number of results to return.

        offset : typing.Optional[int]
            The number of results to skip.

        sort_by : typing.Optional[AssistantSearchRequestSortBy]
            The field to sort by.

        sort_order : typing.Optional[AssistantSearchRequestSortOrder]
            The order to sort by.

        select : typing.Optional[typing.Sequence[AssistantSearchRequestSelectItem]]
            Specify which fields to return. If not provided, all fields are returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Assistant]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.assistants.search_assistants()
        """
        _response = self._raw_client.search_assistants(
            metadata=metadata,
            graph_id=graph_id,
            name=name,
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            sort_order=sort_order,
            select=select,
            request_options=request_options,
        )
        return _response.data

    def count_assistants(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        graph_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Get the count of assistants matching the specified criteria.

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to filter by. Exact match filter for each KV pair.

        graph_id : typing.Optional[str]
            The ID of the graph to filter by. The graph ID is normally set in your langgraph.json configuration.

        name : typing.Optional[str]
            Name of the assistant to filter by. The filtering logic will match (case insensitive) assistants where 'name' is a substring of the assistant name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.assistants.count_assistants()
        """
        _response = self._raw_client.count_assistants(
            metadata=metadata, graph_id=graph_id, name=name, request_options=request_options
        )
        return _response.data

    def get_assistant(self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Assistant:
        """
        Get an assistant by ID.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Assistant
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.assistants.get_assistant(
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.get_assistant(assistant_id, request_options=request_options)
        return _response.data

    def delete_assistant(
        self,
        assistant_id: str,
        *,
        delete_threads: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Delete an assistant by ID.

        All versions of the assistant will be deleted as well.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        delete_threads : typing.Optional[bool]
            If true, delete all threads with metadata.assistant_id matching this assistant, along with runs and checkpoints belonging to those threads. Auth filters are applied, so threads not visible to the user will not be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.assistants.delete_assistant(
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.delete_assistant(
            assistant_id, delete_threads=delete_threads, request_options=request_options
        )
        return _response.data

    def patch_assistant(
        self,
        assistant_id: str,
        *,
        graph_id: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Assistant:
        """
        Update an assistant.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        graph_id : typing.Optional[str]
            The ID of the graph the assistant should use. The graph ID is normally set in your langgraph.json configuration. If not provided, assistant will keep pointing to same graph.

        config : typing.Optional[typing.Dict[str, typing.Any]]
            Configuration to use for the graph. Useful when graph is configurable and you want to update the assistant's configuration.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to merge with existing assistant metadata.

        name : typing.Optional[str]
            The new name for the assistant. If not provided, assistant will keep its current name.

        description : typing.Optional[str]
            The new description for the assistant. If not provided, assistant will keep its current description.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Assistant
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.assistants.patch_assistant(
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.patch_assistant(
            assistant_id,
            graph_id=graph_id,
            config=config,
            context=context,
            metadata=metadata,
            name=name,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def get_assistant_graph(
        self,
        assistant_id: str,
        *,
        xray: typing.Optional[GetAssistantGraphAssistantsAssistantIdGraphGetRequestXray] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]:
        """
        Get an assistant by ID.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        xray : typing.Optional[GetAssistantGraphAssistantsAssistantIdGraphGetRequestXray]
            Include graph representation of subgraphs. If an integer value is provided, only subgraphs with a depth less than or equal to the value will be included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.assistants.get_assistant_graph(
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.get_assistant_graph(assistant_id, xray=xray, request_options=request_options)
        return _response.data

    def get_assistant_subgraphs(
        self,
        assistant_id: str,
        namespace: str,
        *,
        recurse: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Subgraphs:
        """
        Get an assistant's subgraphs filtered by namespace.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        namespace : str
            Namespace of the subgraph to filter by.

        recurse : typing.Optional[bool]
            Recursively retrieve subgraphs of subgraphs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Subgraphs
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.assistants.get_assistant_subgraphs(
            assistant_id="assistant_id",
            namespace="namespace",
        )
        """
        _response = self._raw_client.get_assistant_subgraphs(
            assistant_id, namespace, recurse=recurse, request_options=request_options
        )
        return _response.data

    def get_assistant_schemas(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GraphSchema:
        """
        Get an assistant by ID.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GraphSchema
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.assistants.get_assistant_schemas(
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.get_assistant_schemas(assistant_id, request_options=request_options)
        return _response.data

    def get_assistant_versions_assistants_assistant_id_versions_get(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Assistant]:
        """
        Get all versions of an assistant.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Assistant]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.assistants.get_assistant_versions_assistants_assistant_id_versions_get(
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.get_assistant_versions_assistants_assistant_id_versions_get(
            assistant_id, request_options=request_options
        )
        return _response.data

    def set_latest_assistant_version_assistants_assistant_id_versions_post(
        self, assistant_id: str, *, version: int, request_options: typing.Optional[RequestOptions] = None
    ) -> Assistant:
        """
        Set the latest version for an assistant.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        version : int
            The version to change to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Assistant
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.assistants.set_latest_assistant_version_assistants_assistant_id_versions_post(
            assistant_id="assistant_id",
            version=1,
        )
        """
        _response = self._raw_client.set_latest_assistant_version_assistants_assistant_id_versions_post(
            assistant_id, version=version, request_options=request_options
        )
        return _response.data


class AsyncAssistantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssistantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssistantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssistantsClient
        """
        return self._raw_client

    async def create_assistant(
        self,
        *,
        graph_id: str,
        assistant_id: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        if_exists: typing.Optional[AssistantCreateIfExists] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Assistant:
        """
        Create an assistant.

        An initial version of the assistant will be created and the assistant is set to that version. To change versions, use the `POST /assistants/{assistant_id}/latest` endpoint.

        Parameters
        ----------
        graph_id : str
            The ID of the graph the assistant should use. The graph ID is normally set in your langgraph.json configuration.

        assistant_id : typing.Optional[str]
            The ID of the assistant. If not provided, a random UUID will be generated.

        config : typing.Optional[typing.Dict[str, typing.Any]]
            Configuration to use for the graph. Useful when graph is configurable and you want to create different assistants based on different configurations.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to add to assistant.

        if_exists : typing.Optional[AssistantCreateIfExists]
            How to handle duplicate creation. Must be either 'raise' (raise error if duplicate), or 'do_nothing' (return existing assistant).

        name : typing.Optional[str]
            The name of the assistant. Defaults to 'Untitled'.

        description : typing.Optional[str]
            The description of the assistant. Defaults to null.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Assistant
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assistants.create_assistant(
                graph_id="graph_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_assistant(
            graph_id=graph_id,
            assistant_id=assistant_id,
            config=config,
            context=context,
            metadata=metadata,
            if_exists=if_exists,
            name=name,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def search_assistants(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        graph_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        sort_by: typing.Optional[AssistantSearchRequestSortBy] = OMIT,
        sort_order: typing.Optional[AssistantSearchRequestSortOrder] = OMIT,
        select: typing.Optional[typing.Sequence[AssistantSearchRequestSelectItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Assistant]:
        """
        Search for assistants.

        This endpoint also functions as the endpoint to list all assistants.

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to filter by. Exact match filter for each KV pair.

        graph_id : typing.Optional[str]
            The ID of the graph to filter by. The graph ID is normally set in your langgraph.json configuration.

        name : typing.Optional[str]
            Name of the assistant to filter by. The filtering logic will match (case insensitive) assistants where 'name' is a substring of the assistant name.

        limit : typing.Optional[int]
            The maximum number of results to return.

        offset : typing.Optional[int]
            The number of results to skip.

        sort_by : typing.Optional[AssistantSearchRequestSortBy]
            The field to sort by.

        sort_order : typing.Optional[AssistantSearchRequestSortOrder]
            The order to sort by.

        select : typing.Optional[typing.Sequence[AssistantSearchRequestSelectItem]]
            Specify which fields to return. If not provided, all fields are returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Assistant]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assistants.search_assistants()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_assistants(
            metadata=metadata,
            graph_id=graph_id,
            name=name,
            limit=limit,
            offset=offset,
            sort_by=sort_by,
            sort_order=sort_order,
            select=select,
            request_options=request_options,
        )
        return _response.data

    async def count_assistants(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        graph_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Get the count of assistants matching the specified criteria.

        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to filter by. Exact match filter for each KV pair.

        graph_id : typing.Optional[str]
            The ID of the graph to filter by. The graph ID is normally set in your langgraph.json configuration.

        name : typing.Optional[str]
            Name of the assistant to filter by. The filtering logic will match (case insensitive) assistants where 'name' is a substring of the assistant name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assistants.count_assistants()


        asyncio.run(main())
        """
        _response = await self._raw_client.count_assistants(
            metadata=metadata, graph_id=graph_id, name=name, request_options=request_options
        )
        return _response.data

    async def get_assistant(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Assistant:
        """
        Get an assistant by ID.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Assistant
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assistants.get_assistant(
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_assistant(assistant_id, request_options=request_options)
        return _response.data

    async def delete_assistant(
        self,
        assistant_id: str,
        *,
        delete_threads: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Delete an assistant by ID.

        All versions of the assistant will be deleted as well.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        delete_threads : typing.Optional[bool]
            If true, delete all threads with metadata.assistant_id matching this assistant, along with runs and checkpoints belonging to those threads. Auth filters are applied, so threads not visible to the user will not be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assistants.delete_assistant(
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_assistant(
            assistant_id, delete_threads=delete_threads, request_options=request_options
        )
        return _response.data

    async def patch_assistant(
        self,
        assistant_id: str,
        *,
        graph_id: typing.Optional[str] = OMIT,
        config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Assistant:
        """
        Update an assistant.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        graph_id : typing.Optional[str]
            The ID of the graph the assistant should use. The graph ID is normally set in your langgraph.json configuration. If not provided, assistant will keep pointing to same graph.

        config : typing.Optional[typing.Dict[str, typing.Any]]
            Configuration to use for the graph. Useful when graph is configurable and you want to update the assistant's configuration.

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Static context added to the assistant.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata to merge with existing assistant metadata.

        name : typing.Optional[str]
            The new name for the assistant. If not provided, assistant will keep its current name.

        description : typing.Optional[str]
            The new description for the assistant. If not provided, assistant will keep its current description.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Assistant
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assistants.patch_assistant(
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_assistant(
            assistant_id,
            graph_id=graph_id,
            config=config,
            context=context,
            metadata=metadata,
            name=name,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def get_assistant_graph(
        self,
        assistant_id: str,
        *,
        xray: typing.Optional[GetAssistantGraphAssistantsAssistantIdGraphGetRequestXray] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]:
        """
        Get an assistant by ID.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        xray : typing.Optional[GetAssistantGraphAssistantsAssistantIdGraphGetRequestXray]
            Include graph representation of subgraphs. If an integer value is provided, only subgraphs with a depth less than or equal to the value will be included.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assistants.get_assistant_graph(
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_assistant_graph(assistant_id, xray=xray, request_options=request_options)
        return _response.data

    async def get_assistant_subgraphs(
        self,
        assistant_id: str,
        namespace: str,
        *,
        recurse: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Subgraphs:
        """
        Get an assistant's subgraphs filtered by namespace.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        namespace : str
            Namespace of the subgraph to filter by.

        recurse : typing.Optional[bool]
            Recursively retrieve subgraphs of subgraphs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Subgraphs
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assistants.get_assistant_subgraphs(
                assistant_id="assistant_id",
                namespace="namespace",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_assistant_subgraphs(
            assistant_id, namespace, recurse=recurse, request_options=request_options
        )
        return _response.data

    async def get_assistant_schemas(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GraphSchema:
        """
        Get an assistant by ID.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GraphSchema
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assistants.get_assistant_schemas(
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_assistant_schemas(assistant_id, request_options=request_options)
        return _response.data

    async def get_assistant_versions_assistants_assistant_id_versions_get(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Assistant]:
        """
        Get all versions of an assistant.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Assistant]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assistants.get_assistant_versions_assistants_assistant_id_versions_get(
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_assistant_versions_assistants_assistant_id_versions_get(
            assistant_id, request_options=request_options
        )
        return _response.data

    async def set_latest_assistant_version_assistants_assistant_id_versions_post(
        self, assistant_id: str, *, version: int, request_options: typing.Optional[RequestOptions] = None
    ) -> Assistant:
        """
        Set the latest version for an assistant.

        Parameters
        ----------
        assistant_id : str
            The ID of the assistant.

        version : int
            The version to change to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Assistant
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assistants.set_latest_assistant_version_assistants_assistant_id_versions_post(
                assistant_id="assistant_id",
                version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_latest_assistant_version_assistants_assistant_id_versions_post(
            assistant_id, version=version, request_options=request_options
        )
        return _response.data
