

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.destination_definition_id import DestinationDefinitionId
from ..types.destination_definition_specification_read import DestinationDefinitionSpecificationRead
from ..types.workspace_id import WorkspaceId
from .raw_client import AsyncRawDestinationDefinitionSpecificationClient, RawDestinationDefinitionSpecificationClient


OMIT = typing.cast(typing.Any, ...)


class DestinationDefinitionSpecificationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDestinationDefinitionSpecificationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDestinationDefinitionSpecificationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDestinationDefinitionSpecificationClient
        """
        return self._raw_client

    def get_destination_definition_specification(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationDefinitionSpecificationRead:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationDefinitionSpecificationRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.destination_definition_specification.get_destination_definition_specification(
            destination_definition_id="destinationDefinitionId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_destination_definition_specification(
            destination_definition_id=destination_definition_id,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data


class AsyncDestinationDefinitionSpecificationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDestinationDefinitionSpecificationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDestinationDefinitionSpecificationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDestinationDefinitionSpecificationClient
        """
        return self._raw_client

    async def get_destination_definition_specification(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationDefinitionSpecificationRead:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationDefinitionSpecificationRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.destination_definition_specification.get_destination_definition_specification(
                destination_definition_id="destinationDefinitionId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_destination_definition_specification(
            destination_definition_id=destination_definition_id,
            workspace_id=workspace_id,
            request_options=request_options,
        )
        return _response.data
