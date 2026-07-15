

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.source_definition_id import SourceDefinitionId
from ..types.source_definition_specification_read import SourceDefinitionSpecificationRead
from ..types.workspace_id import WorkspaceId
from .raw_client import AsyncRawSourceDefinitionSpecificationClient, RawSourceDefinitionSpecificationClient


OMIT = typing.cast(typing.Any, ...)


class SourceDefinitionSpecificationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSourceDefinitionSpecificationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSourceDefinitionSpecificationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSourceDefinitionSpecificationClient
        """
        return self._raw_client

    def get_source_definition_specification(
        self,
        *,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceDefinitionSpecificationRead:
        """
        Parameters
        ----------
        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDefinitionSpecificationRead
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.source_definition_specification.get_source_definition_specification(
            source_definition_id="sourceDefinitionId",
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_source_definition_specification(
            source_definition_id=source_definition_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data


class AsyncSourceDefinitionSpecificationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSourceDefinitionSpecificationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSourceDefinitionSpecificationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSourceDefinitionSpecificationClient
        """
        return self._raw_client

    async def get_source_definition_specification(
        self,
        *,
        source_definition_id: SourceDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SourceDefinitionSpecificationRead:
        """
        Parameters
        ----------
        source_definition_id : SourceDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SourceDefinitionSpecificationRead
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.source_definition_specification.get_source_definition_specification(
                source_definition_id="sourceDefinitionId",
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_source_definition_specification(
            source_definition_id=source_definition_id, workspace_id=workspace_id, request_options=request_options
        )
        return _response.data
