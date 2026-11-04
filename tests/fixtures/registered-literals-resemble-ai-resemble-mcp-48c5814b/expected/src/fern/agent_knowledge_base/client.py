

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAgentKnowledgeBaseClient, RawAgentKnowledgeBaseClient
from .types.attach_knowledge_item_to_agent_response import AttachKnowledgeItemToAgentResponse
from .types.create_knowledge_item_request_source_type import CreateKnowledgeItemRequestSourceType
from .types.create_knowledge_item_response import CreateKnowledgeItemResponse
from .types.delete_knowledge_item_response import DeleteKnowledgeItemResponse
from .types.detach_knowledge_item_from_agent_response import DetachKnowledgeItemFromAgentResponse
from .types.get_knowledge_item_response import GetKnowledgeItemResponse
from .types.list_agent_knowledge_items_response import ListAgentKnowledgeItemsResponse
from .types.list_knowledge_items_request_source_type import ListKnowledgeItemsRequestSourceType
from .types.list_knowledge_items_request_status import ListKnowledgeItemsRequestStatus
from .types.list_knowledge_items_response import ListKnowledgeItemsResponse
from .types.reingest_knowledge_item_response import ReingestKnowledgeItemResponse


OMIT = typing.cast(typing.Any, ...)


class AgentKnowledgeBaseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAgentKnowledgeBaseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAgentKnowledgeBaseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAgentKnowledgeBaseClient
        """
        return self._raw_client

    def list_knowledge_items(
        self,
        *,
        status: typing.Optional[ListKnowledgeItemsRequestStatus] = None,
        source_type: typing.Optional[ListKnowledgeItemsRequestSourceType] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListKnowledgeItemsResponse:
        """
        List all knowledge items belonging to the authenticated user's team

        Parameters
        ----------
        status : typing.Optional[ListKnowledgeItemsRequestStatus]
            Filter by status

        source_type : typing.Optional[ListKnowledgeItemsRequestSourceType]
            Filter by source type

        page : typing.Optional[int]
            Page number

        per_page : typing.Optional[int]
            Items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListKnowledgeItemsResponse
            List of knowledge items

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_knowledge_base.list_knowledge_items()
        """
        _response = self._raw_client.list_knowledge_items(
            status=status, source_type=source_type, page=page, per_page=per_page, request_options=request_options
        )
        return _response.data

    def create_knowledge_item(
        self,
        *,
        title: str,
        description: str,
        source_type: CreateKnowledgeItemRequestSourceType,
        url: typing.Optional[str] = OMIT,
        raw_text: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateKnowledgeItemResponse:
        """
        Creates a new knowledge item and queues it for ingestion processing

        Parameters
        ----------
        title : str
            Title of the knowledge item

        description : str
            Description of the knowledge item

        source_type : CreateKnowledgeItemRequestSourceType
            Type of knowledge source

        url : typing.Optional[str]
            Required when source_type is url

        raw_text : typing.Optional[str]
            Required when source_type is text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateKnowledgeItemResponse
            Knowledge item created successfully

        Examples
        --------
        from fern.agent_knowledge_base import CreateKnowledgeItemRequestSourceType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_knowledge_base.create_knowledge_item(
            title="title",
            description="description",
            source_type=CreateKnowledgeItemRequestSourceType.DOCUMENT,
        )
        """
        _response = self._raw_client.create_knowledge_item(
            title=title,
            description=description,
            source_type=source_type,
            url=url,
            raw_text=raw_text,
            request_options=request_options,
        )
        return _response.data

    def get_knowledge_item(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetKnowledgeItemResponse:
        """
        Retrieves a single knowledge item with detailed information including attached agents

        Parameters
        ----------
        uuid_ : str
            The UUID of the knowledge item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetKnowledgeItemResponse
            Knowledge item details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_knowledge_base.get_knowledge_item(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_knowledge_item(uuid_, request_options=request_options)
        return _response.data

    def delete_knowledge_item(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteKnowledgeItemResponse:
        """
        Deletes a knowledge item and cleans up associated data

        Parameters
        ----------
        uuid_ : str
            The UUID of the knowledge item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteKnowledgeItemResponse
            Knowledge item deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_knowledge_base.delete_knowledge_item(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.delete_knowledge_item(uuid_, request_options=request_options)
        return _response.data

    def reingest_knowledge_item(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReingestKnowledgeItemResponse:
        """
        Re-runs the ingestion pipeline for an existing knowledge item

        Parameters
        ----------
        uuid_ : str
            The UUID of the knowledge item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReingestKnowledgeItemResponse
            Re-ingestion queued successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_knowledge_base.reingest_knowledge_item(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.reingest_knowledge_item(uuid_, request_options=request_options)
        return _response.data

    def list_agent_knowledge_items(
        self, agent_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAgentKnowledgeItemsResponse:
        """
        Lists all knowledge items attached to a specific agent

        Parameters
        ----------
        agent_uuid : str
            The UUID of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAgentKnowledgeItemsResponse
            List of knowledge items attached to agent

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_knowledge_base.list_agent_knowledge_items(
            agent_uuid="agent_uuid",
        )
        """
        _response = self._raw_client.list_agent_knowledge_items(agent_uuid, request_options=request_options)
        return _response.data

    def attach_knowledge_item_to_agent(
        self, agent_uuid: str, *, knowledge_item_uuid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AttachKnowledgeItemToAgentResponse:
        """
        Attaches an existing knowledge item to an agent

        Parameters
        ----------
        agent_uuid : str
            The UUID of the agent

        knowledge_item_uuid : str
            The UUID of the knowledge item to attach

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachKnowledgeItemToAgentResponse
            Knowledge item attached successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_knowledge_base.attach_knowledge_item_to_agent(
            agent_uuid="agent_uuid",
            knowledge_item_uuid="knowledge_item_uuid",
        )
        """
        _response = self._raw_client.attach_knowledge_item_to_agent(
            agent_uuid, knowledge_item_uuid=knowledge_item_uuid, request_options=request_options
        )
        return _response.data

    def detach_knowledge_item_from_agent(
        self, agent_uuid: str, knowledge_item_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DetachKnowledgeItemFromAgentResponse:
        """
        Removes a knowledge item from an agent

        Parameters
        ----------
        agent_uuid : str
            The UUID of the agent

        knowledge_item_uuid : str
            The UUID of the knowledge item to detach

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DetachKnowledgeItemFromAgentResponse
            Knowledge item detached successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_knowledge_base.detach_knowledge_item_from_agent(
            agent_uuid="agent_uuid",
            knowledge_item_uuid="knowledge_item_uuid",
        )
        """
        _response = self._raw_client.detach_knowledge_item_from_agent(
            agent_uuid, knowledge_item_uuid, request_options=request_options
        )
        return _response.data


class AsyncAgentKnowledgeBaseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAgentKnowledgeBaseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAgentKnowledgeBaseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAgentKnowledgeBaseClient
        """
        return self._raw_client

    async def list_knowledge_items(
        self,
        *,
        status: typing.Optional[ListKnowledgeItemsRequestStatus] = None,
        source_type: typing.Optional[ListKnowledgeItemsRequestSourceType] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListKnowledgeItemsResponse:
        """
        List all knowledge items belonging to the authenticated user's team

        Parameters
        ----------
        status : typing.Optional[ListKnowledgeItemsRequestStatus]
            Filter by status

        source_type : typing.Optional[ListKnowledgeItemsRequestSourceType]
            Filter by source type

        page : typing.Optional[int]
            Page number

        per_page : typing.Optional[int]
            Items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListKnowledgeItemsResponse
            List of knowledge items

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_knowledge_base.list_knowledge_items()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_knowledge_items(
            status=status, source_type=source_type, page=page, per_page=per_page, request_options=request_options
        )
        return _response.data

    async def create_knowledge_item(
        self,
        *,
        title: str,
        description: str,
        source_type: CreateKnowledgeItemRequestSourceType,
        url: typing.Optional[str] = OMIT,
        raw_text: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateKnowledgeItemResponse:
        """
        Creates a new knowledge item and queues it for ingestion processing

        Parameters
        ----------
        title : str
            Title of the knowledge item

        description : str
            Description of the knowledge item

        source_type : CreateKnowledgeItemRequestSourceType
            Type of knowledge source

        url : typing.Optional[str]
            Required when source_type is url

        raw_text : typing.Optional[str]
            Required when source_type is text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateKnowledgeItemResponse
            Knowledge item created successfully

        Examples
        --------
        import asyncio

        from fern.agent_knowledge_base import CreateKnowledgeItemRequestSourceType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_knowledge_base.create_knowledge_item(
                title="title",
                description="description",
                source_type=CreateKnowledgeItemRequestSourceType.DOCUMENT,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_knowledge_item(
            title=title,
            description=description,
            source_type=source_type,
            url=url,
            raw_text=raw_text,
            request_options=request_options,
        )
        return _response.data

    async def get_knowledge_item(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetKnowledgeItemResponse:
        """
        Retrieves a single knowledge item with detailed information including attached agents

        Parameters
        ----------
        uuid_ : str
            The UUID of the knowledge item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetKnowledgeItemResponse
            Knowledge item details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_knowledge_base.get_knowledge_item(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_knowledge_item(uuid_, request_options=request_options)
        return _response.data

    async def delete_knowledge_item(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteKnowledgeItemResponse:
        """
        Deletes a knowledge item and cleans up associated data

        Parameters
        ----------
        uuid_ : str
            The UUID of the knowledge item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteKnowledgeItemResponse
            Knowledge item deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_knowledge_base.delete_knowledge_item(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_knowledge_item(uuid_, request_options=request_options)
        return _response.data

    async def reingest_knowledge_item(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReingestKnowledgeItemResponse:
        """
        Re-runs the ingestion pipeline for an existing knowledge item

        Parameters
        ----------
        uuid_ : str
            The UUID of the knowledge item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReingestKnowledgeItemResponse
            Re-ingestion queued successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_knowledge_base.reingest_knowledge_item(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reingest_knowledge_item(uuid_, request_options=request_options)
        return _response.data

    async def list_agent_knowledge_items(
        self, agent_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAgentKnowledgeItemsResponse:
        """
        Lists all knowledge items attached to a specific agent

        Parameters
        ----------
        agent_uuid : str
            The UUID of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAgentKnowledgeItemsResponse
            List of knowledge items attached to agent

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_knowledge_base.list_agent_knowledge_items(
                agent_uuid="agent_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_agent_knowledge_items(agent_uuid, request_options=request_options)
        return _response.data

    async def attach_knowledge_item_to_agent(
        self, agent_uuid: str, *, knowledge_item_uuid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AttachKnowledgeItemToAgentResponse:
        """
        Attaches an existing knowledge item to an agent

        Parameters
        ----------
        agent_uuid : str
            The UUID of the agent

        knowledge_item_uuid : str
            The UUID of the knowledge item to attach

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttachKnowledgeItemToAgentResponse
            Knowledge item attached successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_knowledge_base.attach_knowledge_item_to_agent(
                agent_uuid="agent_uuid",
                knowledge_item_uuid="knowledge_item_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.attach_knowledge_item_to_agent(
            agent_uuid, knowledge_item_uuid=knowledge_item_uuid, request_options=request_options
        )
        return _response.data

    async def detach_knowledge_item_from_agent(
        self, agent_uuid: str, knowledge_item_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DetachKnowledgeItemFromAgentResponse:
        """
        Removes a knowledge item from an agent

        Parameters
        ----------
        agent_uuid : str
            The UUID of the agent

        knowledge_item_uuid : str
            The UUID of the knowledge item to detach

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DetachKnowledgeItemFromAgentResponse
            Knowledge item detached successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_knowledge_base.detach_knowledge_item_from_agent(
                agent_uuid="agent_uuid",
                knowledge_item_uuid="knowledge_item_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.detach_knowledge_item_from_agent(
            agent_uuid, knowledge_item_uuid, request_options=request_options
        )
        return _response.data
