

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tool_execution_response import ToolExecutionResponse
from .raw_client import AsyncRawSystemClient, RawSystemClient


OMIT = typing.cast(typing.Any, ...)


class SystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSystemClient
        """
        return self._raw_client

    def execute_version_tool(
        self, *, interaction_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> ToolExecutionResponse:
        """
        Get comprehensive system health and diagnostics

        Parameters
        ----------
        interaction_id : typing.Optional[str]
            INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolExecutionResponse
            Tool execution result

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.execute_version_tool(
            interaction_id="example interaction_id",
        )
        """
        _response = self._raw_client.execute_version_tool(
            interaction_id=interaction_id, request_options=request_options
        )
        return _response.data


class AsyncSystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSystemClient
        """
        return self._raw_client

    async def execute_version_tool(
        self, *, interaction_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> ToolExecutionResponse:
        """
        Get comprehensive system health and diagnostics

        Parameters
        ----------
        interaction_id : typing.Optional[str]
            INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolExecutionResponse
            Tool execution result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.execute_version_tool(
                interaction_id="example interaction_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_version_tool(
            interaction_id=interaction_id, request_options=request_options
        )
        return _response.data
