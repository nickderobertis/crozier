

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.actor_definition_resource_requirements import ActorDefinitionResourceRequirements
from ..types.destination_definition_create import DestinationDefinitionCreate
from ..types.destination_definition_id import DestinationDefinitionId
from ..types.destination_definition_read import DestinationDefinitionRead
from ..types.destination_definition_read_list import DestinationDefinitionReadList
from ..types.private_destination_definition_read import PrivateDestinationDefinitionRead
from ..types.private_destination_definition_read_list import PrivateDestinationDefinitionReadList
from ..types.workspace_id import WorkspaceId
from .raw_client import AsyncRawDestinationDefinitionClient, RawDestinationDefinitionClient


OMIT = typing.cast(typing.Any, ...)


class DestinationDefinitionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDestinationDefinitionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDestinationDefinitionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDestinationDefinitionClient
        """
        return self._raw_client

    def create_custom_destination_definition(
        self,
        *,
        destination_definition: DestinationDefinitionCreate,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationDefinitionRead:
        """
        Parameters
        ----------
        destination_definition : DestinationDefinitionCreate

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationDefinitionRead
            Successful operation

        Examples
        --------
        from fern import DestinationDefinitionCreate, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination_definition.create_custom_destination_definition(
            destination_definition=DestinationDefinitionCreate(
                docker_image_tag="dockerImageTag",
                docker_repository="dockerRepository",
                documentation_url="documentationUrl",
                name="name",
            ),
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.create_custom_destination_definition(
            destination_definition=destination_definition, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def delete_destination_definition(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

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
        client.destination_definition.delete_destination_definition(
            destination_definition_id="destinationDefinitionId",
        )
        """
        _response = self._raw_client.delete_destination_definition(
            destination_definition_id=destination_definition_id, request_options=request_options
        )
        return _response.data

    def get_destination_definition(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationDefinitionRead:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationDefinitionRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination_definition.get_destination_definition(
            destination_definition_id="destinationDefinitionId",
        )
        """
        _response = self._raw_client.get_destination_definition(
            destination_definition_id=destination_definition_id, request_options=request_options
        )
        return _response.data

    def get_destination_definition_for_workspace(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationDefinitionRead:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationDefinitionRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination_definition.get_destination_definition_for_workspace(
            destination_definition_id="destinationDefinitionId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_destination_definition_for_workspace(
            destination_definition_id=destination_definition_id,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    def grant_destination_definition_to_workspace(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrivateDestinationDefinitionRead:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateDestinationDefinitionRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination_definition.grant_destination_definition_to_workspace(
            destination_definition_id="destinationDefinitionId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.grant_destination_definition_to_workspace(
            destination_definition_id=destination_definition_id,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    def list_destination_definitions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DestinationDefinitionReadList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationDefinitionReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination_definition.list_destination_definitions()
        """
        _response = self._raw_client.list_destination_definitions(request_options=request_options)
        return _response.data

    def list_destination_definitions_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> DestinationDefinitionReadList:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationDefinitionReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination_definition.list_destination_definitions_for_workspace(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.list_destination_definitions_for_workspace(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def list_latest_destination_definitions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DestinationDefinitionReadList:
        """
        Guaranteed to retrieve the latest information on supported destinations.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationDefinitionReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination_definition.list_latest_destination_definitions()
        """
        _response = self._raw_client.list_latest_destination_definitions(request_options=request_options)
        return _response.data

    def list_private_destination_definitions(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> PrivateDestinationDefinitionReadList:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateDestinationDefinitionReadList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination_definition.list_private_destination_definitions(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.list_private_destination_definitions(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    def revoke_destination_definition_from_workspace(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

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
        client.destination_definition.revoke_destination_definition_from_workspace(
            destination_definition_id="destinationDefinitionId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.revoke_destination_definition_from_workspace(
            destination_definition_id=destination_definition_id,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    def update_destination_definition(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        docker_image_tag: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ActorDefinitionResourceRequirements] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationDefinitionRead:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        docker_image_tag : typing.Optional[str]

        resource_requirements : typing.Optional[ActorDefinitionResourceRequirements]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationDefinitionRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination_definition.update_destination_definition(
            destination_definition_id="destinationDefinitionId",
        )
        """
        _response = self._raw_client.update_destination_definition(
            destination_definition_id=destination_definition_id,
            docker_image_tag=docker_image_tag,
            resource_requirements=resource_requirements,
            request_options=request_options,
        )
        return _response.data


class AsyncDestinationDefinitionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDestinationDefinitionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDestinationDefinitionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDestinationDefinitionClient
        """
        return self._raw_client

    async def create_custom_destination_definition(
        self,
        *,
        destination_definition: DestinationDefinitionCreate,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationDefinitionRead:
        """
        Parameters
        ----------
        destination_definition : DestinationDefinitionCreate

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationDefinitionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, DestinationDefinitionCreate

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination_definition.create_custom_destination_definition(
                destination_definition=DestinationDefinitionCreate(
                    docker_image_tag="dockerImageTag",
                    docker_repository="dockerRepository",
                    documentation_url="documentationUrl",
                    name="name",
                ),
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_custom_destination_definition(
            destination_definition=destination_definition, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def delete_destination_definition(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

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
            await client.destination_definition.delete_destination_definition(
                destination_definition_id="destinationDefinitionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_destination_definition(
            destination_definition_id=destination_definition_id, request_options=request_options
        )
        return _response.data

    async def get_destination_definition(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationDefinitionRead:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationDefinitionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination_definition.get_destination_definition(
                destination_definition_id="destinationDefinitionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_destination_definition(
            destination_definition_id=destination_definition_id, request_options=request_options
        )
        return _response.data

    async def get_destination_definition_for_workspace(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationDefinitionRead:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationDefinitionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination_definition.get_destination_definition_for_workspace(
                destination_definition_id="destinationDefinitionId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_destination_definition_for_workspace(
            destination_definition_id=destination_definition_id,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    async def grant_destination_definition_to_workspace(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrivateDestinationDefinitionRead:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateDestinationDefinitionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination_definition.grant_destination_definition_to_workspace(
                destination_definition_id="destinationDefinitionId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.grant_destination_definition_to_workspace(
            destination_definition_id=destination_definition_id,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    async def list_destination_definitions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DestinationDefinitionReadList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationDefinitionReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination_definition.list_destination_definitions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_destination_definitions(request_options=request_options)
        return _response.data

    async def list_destination_definitions_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> DestinationDefinitionReadList:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationDefinitionReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination_definition.list_destination_definitions_for_workspace(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_destination_definitions_for_workspace(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def list_latest_destination_definitions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DestinationDefinitionReadList:
        """
        Guaranteed to retrieve the latest information on supported destinations.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationDefinitionReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination_definition.list_latest_destination_definitions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_latest_destination_definitions(request_options=request_options)
        return _response.data

    async def list_private_destination_definitions(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> PrivateDestinationDefinitionReadList:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateDestinationDefinitionReadList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination_definition.list_private_destination_definitions(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_private_destination_definitions(
            workspace_id=workspace_id, request_options=request_options
        )
        return _response.data

    async def revoke_destination_definition_from_workspace(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

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
            await client.destination_definition.revoke_destination_definition_from_workspace(
                destination_definition_id="destinationDefinitionId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_destination_definition_from_workspace(
            destination_definition_id=destination_definition_id,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data

    async def update_destination_definition(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        docker_image_tag: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ActorDefinitionResourceRequirements] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationDefinitionRead:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        docker_image_tag : typing.Optional[str]

        resource_requirements : typing.Optional[ActorDefinitionResourceRequirements]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationDefinitionRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination_definition.update_destination_definition(
                destination_definition_id="destinationDefinitionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_destination_definition(
            destination_definition_id=destination_definition_id,
            docker_image_tag=docker_image_tag,
            resource_requirements=resource_requirements,
            request_options=request_options,
        )
        return _response.data
