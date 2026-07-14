

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.actor_definition_resource_requirements import ActorDefinitionResourceRequirements
from ..types.private_source_definition_read import PrivateSourceDefinitionRead
from ..types.private_source_definition_read_list import PrivateSourceDefinitionReadList
from ..types.source_definition_create import SourceDefinitionCreate
from ..types.source_definition_id import SourceDefinitionId
from ..types.source_definition_read import SourceDefinitionRead
from ..types.source_definition_read_list import SourceDefinitionReadList
from ..types.workspace_id import WorkspaceId
from .raw_client import AsyncRawSourceDefinitionClient, RawSourceDefinitionClient


OMIT = typing.cast(typing.Any, ...)


class SourceDefinitionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSourceDefinitionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSourceDefinitionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSourceDefinitionClient
        """
        return self._raw_client

    def create_custom_source_definition(
        self,
        *,
        source_definition: SourceDefinitionCreate,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceDefinitionRead:
        """
        Parameters
        ----------
        source_definition : SourceDefinitionCreate

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDefinitionRead
            Successful operation

        Examples
        --------
        from fern import FernApi, SourceDefinitionCreate

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source_definition.create_custom_source_definition(
            source_definition=SourceDefinitionCreate(
                docker_image_tag="dockerImageTag",
                docker_repository="dockerRepository",
                documentation_url="documentationUrl",
                name="name",
            ),
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.create_custom_source_definition(
            source_definition=source_definition, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def delete_source_definition(
        self, *, source_definition_id: SourceDefinitionId, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        source_definition_id : SourceDefinitionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source_definition.delete_source_definition(
            source_definition_id="sourceDefinitionId",
        )
        """
        _response = self._raw_client.delete_source_definition(
            source_definition_id=source_definition_id, request_options=request_options
        )
        return _response.data

    def get_source_definition(
        self, *, source_definition_id: SourceDefinitionId, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceDefinitionRead:
        """
        Parameters
        ----------
        source_definition_id : SourceDefinitionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDefinitionRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source_definition.get_source_definition(
            source_definition_id="sourceDefinitionId",
        )
        """
        _response = self._raw_client.get_source_definition(
            source_definition_id=source_definition_id, request_options=request_options
        )
        return _response.data

    def get_source_definition_for_workspace(
        self,
        *,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceDefinitionRead:
        """
        Parameters
        ----------
        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDefinitionRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source_definition.get_source_definition_for_workspace(
            source_definition_id="sourceDefinitionId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_source_definition_for_workspace(
            source_definition_id=source_definition_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def grant_source_definition_to_workspace(
        self,
        *,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrivateSourceDefinitionRead:
        """
        Parameters
        ----------
        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateSourceDefinitionRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source_definition.grant_source_definition_to_workspace(
            source_definition_id="sourceDefinitionId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.grant_source_definition_to_workspace(
            source_definition_id=source_definition_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def list_source_definitions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceDefinitionReadList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDefinitionReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source_definition.list_source_definitions()
        """
        _response = self._raw_client.list_source_definitions(request_options=request_options)
        return _response.data

    def list_source_definitions_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceDefinitionReadList:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDefinitionReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source_definition.list_source_definitions_for_workspace(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.list_source_definitions_for_workspace(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def list_latest_source_definitions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceDefinitionReadList:
        """
        Guaranteed to retrieve the latest information on supported sources.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDefinitionReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source_definition.list_latest_source_definitions()
        """
        _response = self._raw_client.list_latest_source_definitions(request_options=request_options)
        return _response.data

    def list_private_source_definitions(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> PrivateSourceDefinitionReadList:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateSourceDefinitionReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source_definition.list_private_source_definitions(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.list_private_source_definitions(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def revoke_source_definition_from_workspace(
        self,
        *,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source_definition.revoke_source_definition_from_workspace(
            source_definition_id="sourceDefinitionId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.revoke_source_definition_from_workspace(
            source_definition_id=source_definition_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def update_source_definition(
        self,
        *,
        docker_image_tag: str,
        source_definition_id: SourceDefinitionId,
        resource_requirements: typing.Optional[ActorDefinitionResourceRequirements] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceDefinitionRead:
        """
        Parameters
        ----------
        docker_image_tag : str

        source_definition_id : SourceDefinitionId

        resource_requirements : typing.Optional[ActorDefinitionResourceRequirements]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDefinitionRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source_definition.update_source_definition(
            docker_image_tag="dockerImageTag",
            source_definition_id="sourceDefinitionId",
        )
        """
        _response = self._raw_client.update_source_definition(
            docker_image_tag=docker_image_tag,
            source_definition_id=source_definition_id,
            resource_requirements=resource_requirements,
            request_options=request_options,
        )
        return _response.data


class AsyncSourceDefinitionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSourceDefinitionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSourceDefinitionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSourceDefinitionClient
        """
        return self._raw_client

    async def create_custom_source_definition(
        self,
        *,
        source_definition: SourceDefinitionCreate,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceDefinitionRead:
        """
        Parameters
        ----------
        source_definition : SourceDefinitionCreate

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDefinitionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SourceDefinitionCreate

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source_definition.create_custom_source_definition(
                source_definition=SourceDefinitionCreate(
                    docker_image_tag="dockerImageTag",
                    docker_repository="dockerRepository",
                    documentation_url="documentationUrl",
                    name="name",
                ),
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_custom_source_definition(
            source_definition=source_definition, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def delete_source_definition(
        self, *, source_definition_id: SourceDefinitionId, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        source_definition_id : SourceDefinitionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source_definition.delete_source_definition(
                source_definition_id="sourceDefinitionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_source_definition(
            source_definition_id=source_definition_id, request_options=request_options
        )
        return _response.data

    async def get_source_definition(
        self, *, source_definition_id: SourceDefinitionId, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceDefinitionRead:
        """
        Parameters
        ----------
        source_definition_id : SourceDefinitionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDefinitionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source_definition.get_source_definition(
                source_definition_id="sourceDefinitionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_source_definition(
            source_definition_id=source_definition_id, request_options=request_options
        )
        return _response.data

    async def get_source_definition_for_workspace(
        self,
        *,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceDefinitionRead:
        """
        Parameters
        ----------
        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDefinitionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source_definition.get_source_definition_for_workspace(
                source_definition_id="sourceDefinitionId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_source_definition_for_workspace(
            source_definition_id=source_definition_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def grant_source_definition_to_workspace(
        self,
        *,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrivateSourceDefinitionRead:
        """
        Parameters
        ----------
        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateSourceDefinitionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source_definition.grant_source_definition_to_workspace(
                source_definition_id="sourceDefinitionId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.grant_source_definition_to_workspace(
            source_definition_id=source_definition_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def list_source_definitions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceDefinitionReadList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDefinitionReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source_definition.list_source_definitions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_source_definitions(request_options=request_options)
        return _response.data

    async def list_source_definitions_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceDefinitionReadList:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDefinitionReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source_definition.list_source_definitions_for_workspace(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_source_definitions_for_workspace(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def list_latest_source_definitions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SourceDefinitionReadList:
        """
        Guaranteed to retrieve the latest information on supported sources.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDefinitionReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source_definition.list_latest_source_definitions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_latest_source_definitions(request_options=request_options)
        return _response.data

    async def list_private_source_definitions(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> PrivateSourceDefinitionReadList:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateSourceDefinitionReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source_definition.list_private_source_definitions(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_private_source_definitions(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def revoke_source_definition_from_workspace(
        self,
        *,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source_definition.revoke_source_definition_from_workspace(
                source_definition_id="sourceDefinitionId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_source_definition_from_workspace(
            source_definition_id=source_definition_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def update_source_definition(
        self,
        *,
        docker_image_tag: str,
        source_definition_id: SourceDefinitionId,
        resource_requirements: typing.Optional[ActorDefinitionResourceRequirements] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceDefinitionRead:
        """
        Parameters
        ----------
        docker_image_tag : str

        source_definition_id : SourceDefinitionId

        resource_requirements : typing.Optional[ActorDefinitionResourceRequirements]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDefinitionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source_definition.update_source_definition(
                docker_image_tag="dockerImageTag",
                source_definition_id="sourceDefinitionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_source_definition(
            docker_image_tag=docker_image_tag,
            source_definition_id=source_definition_id,
            resource_requirements=resource_requirements,
            request_options=request_options,
        )
        return _response.data
