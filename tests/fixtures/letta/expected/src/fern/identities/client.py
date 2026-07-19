

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agent_state import AgentState
from ..types.block_response import BlockResponse
from ..types.identity import Identity
from ..types.identity_property import IdentityProperty
from ..types.identity_type import IdentityType
from .raw_client import AsyncRawIdentitiesClient, RawIdentitiesClient
from .types.list_agents_for_identity_request_include_item import ListAgentsForIdentityRequestIncludeItem
from .types.list_agents_for_identity_request_order import ListAgentsForIdentityRequestOrder
from .types.list_agents_for_identity_request_order_by import ListAgentsForIdentityRequestOrderBy
from .types.list_blocks_for_identity_request_order import ListBlocksForIdentityRequestOrder
from .types.list_blocks_for_identity_request_order_by import ListBlocksForIdentityRequestOrderBy
from .types.list_identities_request_order import ListIdentitiesRequestOrder
from .types.list_identities_request_order_by import ListIdentitiesRequestOrderBy


OMIT = typing.cast(typing.Any, ...)


class IdentitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIdentitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIdentitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIdentitiesClient
        """
        return self._raw_client

    def list_identities(
        self,
        *,
        name: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        identifier_key: typing.Optional[str] = None,
        identity_type: typing.Optional[IdentityType] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListIdentitiesRequestOrder] = None,
        order_by: typing.Optional[ListIdentitiesRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Identity]:
        """
        Get a list of all identities in the database

        Parameters
        ----------
        name : typing.Optional[str]

        project_id : typing.Optional[str]
            [DEPRECATED: Use X-Project-Id header instead] Filter identities by project ID

        identifier_key : typing.Optional[str]

        identity_type : typing.Optional[IdentityType]

        before : typing.Optional[str]
            Identity ID cursor for pagination. Returns identities that come before this identity ID in the specified sort order

        after : typing.Optional[str]
            Identity ID cursor for pagination. Returns identities that come after this identity ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of identities to return

        order : typing.Optional[ListIdentitiesRequestOrder]
            Sort order for identities by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListIdentitiesRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Identity]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identities.list_identities()
        """
        _response = self._raw_client.list_identities(
            name=name,
            project_id=project_id,
            identifier_key=identifier_key,
            identity_type=identity_type,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    def create_identity(
        self,
        *,
        identifier_key: str,
        name: str,
        identity_type: IdentityType,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Identity:
        """
        Parameters
        ----------
        identifier_key : str
            External, user-generated identifier key of the identity.

        name : str
            The name of the identity.

        identity_type : IdentityType
            The type of the identity.

        project : typing.Optional[str]
            The project slug to associate with the identity (cloud only).

        project_id : typing.Optional[str]
            The project id of the identity, if applicable.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Identity
            Successful Response

        Examples
        --------
        from fern import FernApi, IdentityType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identities.create_identity(
            identifier_key="identifier_key",
            name="name",
            identity_type=IdentityType.ORG,
        )
        """
        _response = self._raw_client.create_identity(
            identifier_key=identifier_key,
            name=name,
            identity_type=identity_type,
            project=project,
            project_id=project_id,
            agent_ids=agent_ids,
            block_ids=block_ids,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    def upsert_identity(
        self,
        *,
        identifier_key: str,
        name: str,
        identity_type: IdentityType,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Identity:
        """
        Parameters
        ----------
        identifier_key : str
            External, user-generated identifier key of the identity.

        name : str
            The name of the identity.

        identity_type : IdentityType
            The type of the identity.

        project : typing.Optional[str]
            The project slug to associate with the identity (cloud only).

        project_id : typing.Optional[str]
            The project id of the identity, if applicable.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Identity
            Successful Response

        Examples
        --------
        from fern import FernApi, IdentityType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identities.upsert_identity(
            identifier_key="identifier_key",
            name="name",
            identity_type=IdentityType.ORG,
        )
        """
        _response = self._raw_client.upsert_identity(
            identifier_key=identifier_key,
            name=name,
            identity_type=identity_type,
            project=project,
            project_id=project_id,
            agent_ids=agent_ids,
            block_ids=block_ids,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    def count_identities(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Get count of all identities for a user

        Parameters
        ----------
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
        client.identities.count_identities()
        """
        _response = self._raw_client.count_identities(request_options=request_options)
        return _response.data

    def retrieve_identity(
        self, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Identity:
        """
        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Identity
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identities.retrieve_identity(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.retrieve_identity(identity_id, request_options=request_options)
        return _response.data

    def delete_identity(
        self, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Delete an identity by its identifier key

        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

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
        client.identities.delete_identity(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.delete_identity(identity_id, request_options=request_options)
        return _response.data

    def update_identity(
        self,
        identity_id: str,
        *,
        identifier_key: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        identity_type: typing.Optional[IdentityType] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Identity:
        """
        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        identifier_key : typing.Optional[str]
            External, user-generated identifier key of the identity.

        name : typing.Optional[str]
            The name of the identity.

        identity_type : typing.Optional[IdentityType]
            The type of the identity.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Identity
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identities.update_identity(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.update_identity(
            identity_id,
            identifier_key=identifier_key,
            name=name,
            identity_type=identity_type,
            agent_ids=agent_ids,
            block_ids=block_ids,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    def upsert_properties_for_identity(
        self,
        identity_id: str,
        *,
        request: typing.Sequence[IdentityProperty],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        request : typing.Sequence[IdentityProperty]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi, IdentityProperty, IdentityPropertyType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identities.upsert_properties_for_identity(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
            request=[
                IdentityProperty(
                    key="key",
                    value="value",
                    type=IdentityPropertyType.STRING,
                )
            ],
        )
        """
        _response = self._raw_client.upsert_properties_for_identity(
            identity_id, request=request, request_options=request_options
        )
        return _response.data

    def list_agents_for_identity(
        self,
        identity_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentsForIdentityRequestOrder] = None,
        order_by: typing.Optional[ListAgentsForIdentityRequestOrderBy] = None,
        include: typing.Optional[
            typing.Union[
                ListAgentsForIdentityRequestIncludeItem, typing.Sequence[ListAgentsForIdentityRequestIncludeItem]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AgentState]:
        """
        Get all agents associated with the specified identity.

        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        before : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order

        after : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of agents to return

        order : typing.Optional[ListAgentsForIdentityRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListAgentsForIdentityRequestOrderBy]
            Field to sort by

        include : typing.Optional[typing.Union[ListAgentsForIdentityRequestIncludeItem, typing.Sequence[ListAgentsForIdentityRequestIncludeItem]]]
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
        client.identities.list_agents_for_identity(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.list_agents_for_identity(
            identity_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            include=include,
            request_options=request_options,
        )
        return _response.data

    def list_blocks_for_identity(
        self,
        identity_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListBlocksForIdentityRequestOrder] = None,
        order_by: typing.Optional[ListBlocksForIdentityRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BlockResponse]:
        """
        Get all blocks associated with the specified identity.

        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        before : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come before this block ID in the specified sort order

        after : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come after this block ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of blocks to return

        order : typing.Optional[ListBlocksForIdentityRequestOrder]
            Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListBlocksForIdentityRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BlockResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identities.list_blocks_for_identity(
            identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
        )
        """
        _response = self._raw_client.list_blocks_for_identity(
            identity_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data


class AsyncIdentitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIdentitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIdentitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIdentitiesClient
        """
        return self._raw_client

    async def list_identities(
        self,
        *,
        name: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        identifier_key: typing.Optional[str] = None,
        identity_type: typing.Optional[IdentityType] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListIdentitiesRequestOrder] = None,
        order_by: typing.Optional[ListIdentitiesRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Identity]:
        """
        Get a list of all identities in the database

        Parameters
        ----------
        name : typing.Optional[str]

        project_id : typing.Optional[str]
            [DEPRECATED: Use X-Project-Id header instead] Filter identities by project ID

        identifier_key : typing.Optional[str]

        identity_type : typing.Optional[IdentityType]

        before : typing.Optional[str]
            Identity ID cursor for pagination. Returns identities that come before this identity ID in the specified sort order

        after : typing.Optional[str]
            Identity ID cursor for pagination. Returns identities that come after this identity ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of identities to return

        order : typing.Optional[ListIdentitiesRequestOrder]
            Sort order for identities by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListIdentitiesRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Identity]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identities.list_identities()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_identities(
            name=name,
            project_id=project_id,
            identifier_key=identifier_key,
            identity_type=identity_type,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data

    async def create_identity(
        self,
        *,
        identifier_key: str,
        name: str,
        identity_type: IdentityType,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Identity:
        """
        Parameters
        ----------
        identifier_key : str
            External, user-generated identifier key of the identity.

        name : str
            The name of the identity.

        identity_type : IdentityType
            The type of the identity.

        project : typing.Optional[str]
            The project slug to associate with the identity (cloud only).

        project_id : typing.Optional[str]
            The project id of the identity, if applicable.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Identity
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, IdentityType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identities.create_identity(
                identifier_key="identifier_key",
                name="name",
                identity_type=IdentityType.ORG,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_identity(
            identifier_key=identifier_key,
            name=name,
            identity_type=identity_type,
            project=project,
            project_id=project_id,
            agent_ids=agent_ids,
            block_ids=block_ids,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    async def upsert_identity(
        self,
        *,
        identifier_key: str,
        name: str,
        identity_type: IdentityType,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Identity:
        """
        Parameters
        ----------
        identifier_key : str
            External, user-generated identifier key of the identity.

        name : str
            The name of the identity.

        identity_type : IdentityType
            The type of the identity.

        project : typing.Optional[str]
            The project slug to associate with the identity (cloud only).

        project_id : typing.Optional[str]
            The project id of the identity, if applicable.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Identity
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, IdentityType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identities.upsert_identity(
                identifier_key="identifier_key",
                name="name",
                identity_type=IdentityType.ORG,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert_identity(
            identifier_key=identifier_key,
            name=name,
            identity_type=identity_type,
            project=project,
            project_id=project_id,
            agent_ids=agent_ids,
            block_ids=block_ids,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    async def count_identities(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Get count of all identities for a user

        Parameters
        ----------
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
            await client.identities.count_identities()


        asyncio.run(main())
        """
        _response = await self._raw_client.count_identities(request_options=request_options)
        return _response.data

    async def retrieve_identity(
        self, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Identity:
        """
        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Identity
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identities.retrieve_identity(
                identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_identity(identity_id, request_options=request_options)
        return _response.data

    async def delete_identity(
        self, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Delete an identity by its identifier key

        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

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
            await client.identities.delete_identity(
                identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_identity(identity_id, request_options=request_options)
        return _response.data

    async def update_identity(
        self,
        identity_id: str,
        *,
        identifier_key: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        identity_type: typing.Optional[IdentityType] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Identity:
        """
        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        identifier_key : typing.Optional[str]
            External, user-generated identifier key of the identity.

        name : typing.Optional[str]
            The name of the identity.

        identity_type : typing.Optional[IdentityType]
            The type of the identity.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Identity
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identities.update_identity(
                identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_identity(
            identity_id,
            identifier_key=identifier_key,
            name=name,
            identity_type=identity_type,
            agent_ids=agent_ids,
            block_ids=block_ids,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    async def upsert_properties_for_identity(
        self,
        identity_id: str,
        *,
        request: typing.Sequence[IdentityProperty],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        request : typing.Sequence[IdentityProperty]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, IdentityProperty, IdentityPropertyType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identities.upsert_properties_for_identity(
                identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
                request=[
                    IdentityProperty(
                        key="key",
                        value="value",
                        type=IdentityPropertyType.STRING,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert_properties_for_identity(
            identity_id, request=request, request_options=request_options
        )
        return _response.data

    async def list_agents_for_identity(
        self,
        identity_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentsForIdentityRequestOrder] = None,
        order_by: typing.Optional[ListAgentsForIdentityRequestOrderBy] = None,
        include: typing.Optional[
            typing.Union[
                ListAgentsForIdentityRequestIncludeItem, typing.Sequence[ListAgentsForIdentityRequestIncludeItem]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[AgentState]:
        """
        Get all agents associated with the specified identity.

        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        before : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order

        after : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of agents to return

        order : typing.Optional[ListAgentsForIdentityRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListAgentsForIdentityRequestOrderBy]
            Field to sort by

        include : typing.Optional[typing.Union[ListAgentsForIdentityRequestIncludeItem, typing.Sequence[ListAgentsForIdentityRequestIncludeItem]]]
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
            await client.identities.list_agents_for_identity(
                identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_agents_for_identity(
            identity_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            include=include,
            request_options=request_options,
        )
        return _response.data

    async def list_blocks_for_identity(
        self,
        identity_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListBlocksForIdentityRequestOrder] = None,
        order_by: typing.Optional[ListBlocksForIdentityRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[BlockResponse]:
        """
        Get all blocks associated with the specified identity.

        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        before : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come before this block ID in the specified sort order

        after : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come after this block ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of blocks to return

        order : typing.Optional[ListBlocksForIdentityRequestOrder]
            Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListBlocksForIdentityRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BlockResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identities.list_blocks_for_identity(
                identity_id="identity-123e4567-e89b-42d3-8456-426614174000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_blocks_for_identity(
            identity_id,
            before=before,
            after=after,
            limit=limit,
            order=order,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data
