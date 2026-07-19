

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.block import Block
from .raw_client import AsyncRawInternalAgentsClient, RawInternalAgentsClient


OMIT = typing.cast(typing.Any, ...)


class InternalAgentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInternalAgentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInternalAgentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInternalAgentsClient
        """
        return self._raw_client

    def count_internal_agents(
        self, *, exclude_hidden: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Get the total number of agents for a user, with option to exclude hidden agents.

        Parameters
        ----------
        exclude_hidden : typing.Optional[bool]
            If True, excludes hidden agents from the count. If False, includes all agents.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.internal_agents.count_internal_agents()
        """
        _response = self._raw_client.count_internal_agents(
            exclude_hidden=exclude_hidden, request_options=request_options
        )
        return _response.data

    def modify_internal_core_memory_block(
        self,
        agent_id: str,
        block_label: str,
        *,
        value: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_name: typing.Optional[str] = OMIT,
        is_template: typing.Optional[bool] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        base_template_id: typing.Optional[str] = OMIT,
        deployment_id: typing.Optional[str] = OMIT,
        entity_id: typing.Optional[str] = OMIT,
        preserve_on_migration: typing.Optional[bool] = OMIT,
        label: typing.Optional[str] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Block:
        """
        Updates a core memory block of an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        block_label : str

        value : typing.Optional[str]
            Value of the block.

        limit : typing.Optional[int]
            Character limit of the block.

        project_id : typing.Optional[str]
            The associated project id.

        template_name : typing.Optional[str]
            Name of the block if it is a template.

        is_template : typing.Optional[bool]
            Whether the block is a template (e.g. saved human/persona options).

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

        label : typing.Optional[str]
            Label of the block (e.g. 'human', 'persona') in the context window.

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
        client.internal_agents.modify_internal_core_memory_block(
            agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
            block_label="block_label",
        )
        """
        _response = self._raw_client.modify_internal_core_memory_block(
            agent_id,
            block_label,
            value=value,
            limit=limit,
            project_id=project_id,
            template_name=template_name,
            is_template=is_template,
            template_id=template_id,
            base_template_id=base_template_id,
            deployment_id=deployment_id,
            entity_id=entity_id,
            preserve_on_migration=preserve_on_migration,
            label=label,
            read_only=read_only,
            description=description,
            metadata=metadata,
            hidden=hidden,
            tags=tags,
            request_options=request_options,
        )
        return _response.data


class AsyncInternalAgentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInternalAgentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInternalAgentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInternalAgentsClient
        """
        return self._raw_client

    async def count_internal_agents(
        self, *, exclude_hidden: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Get the total number of agents for a user, with option to exclude hidden agents.

        Parameters
        ----------
        exclude_hidden : typing.Optional[bool]
            If True, excludes hidden agents from the count. If False, includes all agents.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.internal_agents.count_internal_agents()


        asyncio.run(main())
        """
        _response = await self._raw_client.count_internal_agents(
            exclude_hidden=exclude_hidden, request_options=request_options
        )
        return _response.data

    async def modify_internal_core_memory_block(
        self,
        agent_id: str,
        block_label: str,
        *,
        value: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        project_id: typing.Optional[str] = OMIT,
        template_name: typing.Optional[str] = OMIT,
        is_template: typing.Optional[bool] = OMIT,
        template_id: typing.Optional[str] = OMIT,
        base_template_id: typing.Optional[str] = OMIT,
        deployment_id: typing.Optional[str] = OMIT,
        entity_id: typing.Optional[str] = OMIT,
        preserve_on_migration: typing.Optional[bool] = OMIT,
        label: typing.Optional[str] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        hidden: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Block:
        """
        Updates a core memory block of an agent.

        Parameters
        ----------
        agent_id : str
            The ID of the agent in the format 'agent-<uuid4>'

        block_label : str

        value : typing.Optional[str]
            Value of the block.

        limit : typing.Optional[int]
            Character limit of the block.

        project_id : typing.Optional[str]
            The associated project id.

        template_name : typing.Optional[str]
            Name of the block if it is a template.

        is_template : typing.Optional[bool]
            Whether the block is a template (e.g. saved human/persona options).

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

        label : typing.Optional[str]
            Label of the block (e.g. 'human', 'persona') in the context window.

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
            await client.internal_agents.modify_internal_core_memory_block(
                agent_id="agent-123e4567-e89b-42d3-8456-426614174000",
                block_label="block_label",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_internal_core_memory_block(
            agent_id,
            block_label,
            value=value,
            limit=limit,
            project_id=project_id,
            template_name=template_name,
            is_template=is_template,
            template_id=template_id,
            base_template_id=base_template_id,
            deployment_id=deployment_id,
            entity_id=entity_id,
            preserve_on_migration=preserve_on_migration,
            label=label,
            read_only=read_only,
            description=description,
            metadata=metadata,
            hidden=hidden,
            tags=tags,
            request_options=request_options,
        )
        return _response.data
