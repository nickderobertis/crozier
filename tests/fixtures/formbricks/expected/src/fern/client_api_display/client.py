

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawClientApiDisplayClient, RawClientApiDisplayClient


OMIT = typing.cast(typing.Any, ...)


class ClientApiDisplayClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClientApiDisplayClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClientApiDisplayClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClientApiDisplayClient
        """
        return self._raw_client

    def create_display(
        self,
        workspace_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Create a new display for a valid survey ID. If a userId is passed, the display is linked to the user. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        workspace_id : str
            The ID of the Workspace. Deprecated alias `environmentId`.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.client_api_display.create_display(
            workspace_id="workspaceId",
            request={"surveyId": "survey123", "userId": "user123"},
        )
        """
        _response = self._raw_client.create_display(workspace_id, request=request, request_options=request_options)
        return _response.data


class AsyncClientApiDisplayClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClientApiDisplayClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClientApiDisplayClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClientApiDisplayClient
        """
        return self._raw_client

    async def create_display(
        self,
        workspace_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Create a new display for a valid survey ID. If a userId is passed, the display is linked to the user. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        workspace_id : str
            The ID of the Workspace. Deprecated alias `environmentId`.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.client_api_display.create_display(
                workspace_id="workspaceId",
                request={"surveyId": "survey123", "userId": "user123"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_display(
            workspace_id, request=request, request_options=request_options
        )
        return _response.data
