

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agent_state import AgentState
from ..types.block import Block
from .raw_client import AsyncRawInternalBlocksClient, RawInternalBlocksClient
from .types.list_agents_for_internal_block_request_order import ListAgentsForInternalBlockRequestOrder
from .types.list_agents_for_internal_block_request_order_by import ListAgentsForInternalBlockRequestOrderBy
from .types.list_internal_blocks_request_order import ListInternalBlocksRequestOrder
from .types.list_internal_blocks_request_order_by import ListInternalBlocksRequestOrderBy


OMIT = typing.cast(typing.Any, ...)


class InternalBlocksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInternalBlocksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInternalBlocksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInternalBlocksClient
        """
        return self._raw_client

    def list_internal_blocks(
        self,
        *,
        label: typing.Optional[str] = None,
        templates_only: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        identity_id: typing.Optional[str] = None,
        identifier_keys: typing.Optional[typing.Sequence[str]] = None,
        project_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        order: typing.Optional[ListInternalBlocksRequestOrder] = None,
        order_by: typing.Optional[ListInternalBlocksRequestOrderBy] = None,
        label_search: typing.Optional[str] = None,
        description_search: typing.Optional[str] = None,
        value_search: typing.Optional[str] = None,
        connected_to_agents_count_gt: typing.Optional[int] = None,
        connected_to_agents_count_lt: typing.Optional[int] = None,
        connected_to_agents_count_eq: typing.Optional[typing.Sequence[int]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Block]:
        """
        Parameters
        ----------
        label : typing.Optional[str]
            Label to include (alphanumeric, hyphens, underscores, forward slashes)

        templates_only : typing.Optional[bool]
            Whether to include only templates

        name : typing.Optional[str]
            Name filter (alphanumeric, spaces, hyphens, underscores)

        identity_id : typing.Optional[str]
            The ID of the identity in the format 'identity-<uuid4>'

        identifier_keys : typing.Optional[typing.Sequence[str]]
            Search agents by identifier keys

        project_id : typing.Optional[str]
            Search blocks by project id

        limit : typing.Optional[int]
            Number of blocks to return

        before : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come before this block ID in the specified sort order

        after : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come after this block ID in the specified sort order

        order : typing.Optional[ListInternalBlocksRequestOrder]
            Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListInternalBlocksRequestOrderBy]
            Field to sort by

        label_search : typing.Optional[str]
            Search blocks by label. If provided, returns blocks whose label matches the search query. This is a full-text search on block labels.

        description_search : typing.Optional[str]
            Search blocks by description. If provided, returns blocks whose description matches the search query. This is a full-text search on block descriptions.

        value_search : typing.Optional[str]
            Search blocks by value. If provided, returns blocks whose value matches the search query. This is a full-text search on block values.

        connected_to_agents_count_gt : typing.Optional[int]
            Filter blocks by the number of connected agents. If provided, returns blocks that have more than this number of connected agents.

        connected_to_agents_count_lt : typing.Optional[int]
            Filter blocks by the number of connected agents. If provided, returns blocks that have less than this number of connected agents.

        connected_to_agents_count_eq : typing.Optional[typing.Sequence[int]]
            Filter blocks by the exact number of connected agents. If provided, returns blocks that have exactly this number of connected agents.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Block]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.internal_blocks.list_internal_blocks()
        """
        _response = self._raw_client.list_internal_blocks(
            label=label,
            templates_only=templates_only,
            name=name,
            identity_id=identity_id,
            identifier_keys=identifier_keys,
            project_id=project_id,
            limit=limit,
            before=before,
            after=after,
            order=order,
            order_by=order_by,
            label_search=label_search,
            description_search=description_search,
            value_search=value_search,
            connected_to_agents_count_gt=connected_to_agents_count_gt,
            connected_to_agents_count_lt=connected_to_agents_count_lt,
            connected_to_agents_count_eq=connected_to_agents_count_eq,
            request_options=request_options,
        )
        return _response.data

    def create_internal_block(
        self,
        *,
        value: str,
        label: str,
        limit: typing.Optional[int] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_name: typing.Optional[str] = OMIT,
        is_template: typing.Optional[bool] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        base_template_id: typing.Optional[str] = OMIT,
        deployment_id: typing.Optional[str] = OMIT,
        entity_id: typing.Optional[str] = OMIT,
        preserve_on_migration: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Block:
        """
        Parameters
        ----------
        value : str
            Value of the block.

        label : str
            Label of the block.

        limit : typing.Optional[int]
            Character limit of the block.

        project_id : typing.Optional[str]
            The associated project id.

        template_name : typing.Optional[str]
            Name of the block if it is a template.

        is_template : typing.Optional[bool]

        template_id : typing.Optional[str]
            The id of the template.

        base_template_id : typing.Optional[str]
            The base template id of the block.

        deployment_id : typing.Optional[str]
            The id of the deployment.

        entity_id : typing.Optional[str]
            The id of the entity within the template.

        preserve_on_migration : typing.Optional[bool]
            Preserve the block on template migration.

        read_only : typing.Optional[bool]
            Whether the agent has read-only access to the block.

        description : typing.Optional[str]
            Description of the block.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata of the block.

        hidden : typing.Optional[bool]
            If set to True, the block will be hidden.

        tags : typing.Optional[typing.Sequence[str]]
            The tags to associate with the block.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.internal_blocks.create_internal_block(
            value="value",
            label="label",
        )
        """
        _response = self._raw_client.create_internal_block(
            value=value,
            label=label,
            limit=limit,
            project_id=project_id,
            template_name=template_name,
            is_template=is_template,
            template_id=template_id,
            base_template_id=base_template_id,
            deployment_id=deployment_id,
            entity_id=entity_id,
            preserve_on_migration=preserve_on_migration,
            read_only=read_only,
            description=description,
            metadata=metadata,
            hidden=hidden,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    def delete_internal_block(
        self, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.internal_blocks.delete_internal_block(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.delete_internal_block(block_id, request_options=request_options)
        return _response.data

    def list_agents_for_internal_block(
        self,
        block_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentsForInternalBlockRequestOrder] = None,
        order_by: typing.Optional[ListAgentsForInternalBlockRequestOrderBy] = None,
        include_relationships: typing.Optional[typing.Sequence[str]] = None,
        include: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AgentState]:
        """
        Retrieves all agents associated with the specified block.
        Raises a 404 if the block does not exist.

        Parameters
        ----------
        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        before : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order

        after : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of agents to return

        order : typing.Optional[ListAgentsForInternalBlockRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListAgentsForInternalBlockRequestOrderBy]
            Field to sort by

        include_relationships : typing.Optional[typing.Sequence[str]]
            Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include in the response. If not provided, all relationships are loaded by default. Using this can optimize performance by reducing unnecessary joins.This is a legacy parameter, and no longer supported after 1.0.0 SDK versions.

        include : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Specify which relational fields to include in the response. No relationships are included by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AgentState]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.internal_blocks.list_agents_for_internal_block(
            block_id="block-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.list_agents_for_internal_block(
            block_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            include_relationships=include_relationships,
            include=include,
            request_options=request_options,
        )
        return _response.data


class AsyncInternalBlocksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInternalBlocksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInternalBlocksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInternalBlocksClient
        """
        return self._raw_client

    async def list_internal_blocks(
        self,
        *,
        label: typing.Optional[str] = None,
        templates_only: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        identity_id: typing.Optional[str] = None,
        identifier_keys: typing.Optional[typing.Sequence[str]] = None,
        project_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        order: typing.Optional[ListInternalBlocksRequestOrder] = None,
        order_by: typing.Optional[ListInternalBlocksRequestOrderBy] = None,
        label_search: typing.Optional[str] = None,
        description_search: typing.Optional[str] = None,
        value_search: typing.Optional[str] = None,
        connected_to_agents_count_gt: typing.Optional[int] = None,
        connected_to_agents_count_lt: typing.Optional[int] = None,
        connected_to_agents_count_eq: typing.Optional[typing.Sequence[int]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Block]:
        """
        Parameters
        ----------
        label : typing.Optional[str]
            Label to include (alphanumeric, hyphens, underscores, forward slashes)

        templates_only : typing.Optional[bool]
            Whether to include only templates

        name : typing.Optional[str]
            Name filter (alphanumeric, spaces, hyphens, underscores)

        identity_id : typing.Optional[str]
            The ID of the identity in the format 'identity-<uuid4>'

        identifier_keys : typing.Optional[typing.Sequence[str]]
            Search agents by identifier keys

        project_id : typing.Optional[str]
            Search blocks by project id

        limit : typing.Optional[int]
            Number of blocks to return

        before : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come before this block ID in the specified sort order

        after : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come after this block ID in the specified sort order

        order : typing.Optional[ListInternalBlocksRequestOrder]
            Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListInternalBlocksRequestOrderBy]
            Field to sort by

        label_search : typing.Optional[str]
            Search blocks by label. If provided, returns blocks whose label matches the search query. This is a full-text search on block labels.

        description_search : typing.Optional[str]
            Search blocks by description. If provided, returns blocks whose description matches the search query. This is a full-text search on block descriptions.

        value_search : typing.Optional[str]
            Search blocks by value. If provided, returns blocks whose value matches the search query. This is a full-text search on block values.

        connected_to_agents_count_gt : typing.Optional[int]
            Filter blocks by the number of connected agents. If provided, returns blocks that have more than this number of connected agents.

        connected_to_agents_count_lt : typing.Optional[int]
            Filter blocks by the number of connected agents. If provided, returns blocks that have less than this number of connected agents.

        connected_to_agents_count_eq : typing.Optional[typing.Sequence[int]]
            Filter blocks by the exact number of connected agents. If provided, returns blocks that have exactly this number of connected agents.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Block]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.internal_blocks.list_internal_blocks()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_internal_blocks(
            label=label,
            templates_only=templates_only,
            name=name,
            identity_id=identity_id,
            identifier_keys=identifier_keys,
            project_id=project_id,
            limit=limit,
            before=before,
            after=after,
            order=order,
            order_by=order_by,
            label_search=label_search,
            description_search=description_search,
            value_search=value_search,
            connected_to_agents_count_gt=connected_to_agents_count_gt,
            connected_to_agents_count_lt=connected_to_agents_count_lt,
            connected_to_agents_count_eq=connected_to_agents_count_eq,
            request_options=request_options,
        )
        return _response.data

    async def create_internal_block(
        self,
        *,
        value: str,
        label: str,
        limit: typing.Optional[int] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_name: typing.Optional[str] = OMIT,
        is_template: typing.Optional[bool] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        base_template_id: typing.Optional[str] = OMIT,
        deployment_id: typing.Optional[str] = OMIT,
        entity_id: typing.Optional[str] = OMIT,
        preserve_on_migration: typing.Optional[bool] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Block:
        """
        Parameters
        ----------
        value : str
            Value of the block.

        label : str
            Label of the block.

        limit : typing.Optional[int]
            Character limit of the block.

        project_id : typing.Optional[str]
            The associated project id.

        template_name : typing.Optional[str]
            Name of the block if it is a template.

        is_template : typing.Optional[bool]

        template_id : typing.Optional[str]
            The id of the template.

        base_template_id : typing.Optional[str]
            The base template id of the block.

        deployment_id : typing.Optional[str]
            The id of the deployment.

        entity_id : typing.Optional[str]
            The id of the entity within the template.

        preserve_on_migration : typing.Optional[bool]
            Preserve the block on template migration.

        read_only : typing.Optional[bool]
            Whether the agent has read-only access to the block.

        description : typing.Optional[str]
            Description of the block.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Metadata of the block.

        hidden : typing.Optional[bool]
            If set to True, the block will be hidden.

        tags : typing.Optional[typing.Sequence[str]]
            The tags to associate with the block.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Block
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.internal_blocks.create_internal_block(
                value="value",
                label="label",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_internal_block(
            value=value,
            label=label,
            limit=limit,
            project_id=project_id,
            template_name=template_name,
            is_template=is_template,
            template_id=template_id,
            base_template_id=base_template_id,
            deployment_id=deployment_id,
            entity_id=entity_id,
            preserve_on_migration=preserve_on_migration,
            read_only=read_only,
            description=description,
            metadata=metadata,
            hidden=hidden,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    async def delete_internal_block(
        self, block_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.internal_blocks.delete_internal_block(
                block_id="block-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_internal_block(block_id, request_options=request_options)
        return _response.data

    async def list_agents_for_internal_block(
        self,
        block_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentsForInternalBlockRequestOrder] = None,
        order_by: typing.Optional[ListAgentsForInternalBlockRequestOrderBy] = None,
        include_relationships: typing.Optional[typing.Sequence[str]] = None,
        include: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AgentState]:
        """
        Retrieves all agents associated with the specified block.
        Raises a 404 if the block does not exist.

        Parameters
        ----------
        block_id : str
            The ID of the block in the format 'block-<uuid4>'

        before : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order

        after : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of agents to return

        order : typing.Optional[ListAgentsForInternalBlockRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListAgentsForInternalBlockRequestOrderBy]
            Field to sort by

        include_relationships : typing.Optional[typing.Sequence[str]]
            Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include in the response. If not provided, all relationships are loaded by default. Using this can optimize performance by reducing unnecessary joins.This is a legacy parameter, and no longer supported after 1.0.0 SDK versions.

        include : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Specify which relational fields to include in the response. No relationships are included by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AgentState]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.internal_blocks.list_agents_for_internal_block(
                block_id="block-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_agents_for_internal_block(
            block_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            include_relationships=include_relationships,
            include=include,
            request_options=request_options,
        )
        return _response.data
