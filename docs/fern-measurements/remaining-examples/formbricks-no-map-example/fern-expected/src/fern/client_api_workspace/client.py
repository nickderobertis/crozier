

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawClientApiWorkspaceClient, RawClientApiWorkspaceClient


class ClientApiWorkspaceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClientApiWorkspaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClientApiWorkspaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClientApiWorkspaceClient
        """
        return self._raw_client

    def get_workspace_state(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Retrieves the Workspace state to be used in Formbricks SDKs. Note - Environments are deprecated. Use Workspace/workspaceId terminology. **Cache Behavior**: This endpoint uses server-side caching with a **5-minute TTL (Time To Live)**. Any changes to surveys, action classes, Workspace settings, or other Workspace data will take up to 5 minutes to reflect in the API response. This caching is implemented to improve performance for high-frequency SDK requests.

        Parameters
        ----------
        workspace_id : str
            The ID of the Workspace. Deprecated alias `environmentId`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.client_api_workspace.get_workspace_state(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.get_workspace_state(workspace_id, request_options=request_options)
        return _response.data


class AsyncClientApiWorkspaceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClientApiWorkspaceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClientApiWorkspaceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClientApiWorkspaceClient
        """
        return self._raw_client

    async def get_workspace_state(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Retrieves the Workspace state to be used in Formbricks SDKs. Note - Environments are deprecated. Use Workspace/workspaceId terminology. **Cache Behavior**: This endpoint uses server-side caching with a **5-minute TTL (Time To Live)**. Any changes to surveys, action classes, Workspace settings, or other Workspace data will take up to 5 minutes to reflect in the API response. This caching is implemented to improve performance for high-frequency SDK requests.

        Parameters
        ----------
        workspace_id : str
            The ID of the Workspace. Deprecated alias `environmentId`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.client_api_workspace.get_workspace_state(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_workspace_state(workspace_id, request_options=request_options)
        return _response.data
