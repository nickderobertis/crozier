

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawClientApiUserClient, RawClientApiUserClient


OMIT = typing.cast(typing.Any, ...)


class ClientApiUserClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClientApiUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClientApiUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClientApiUserClient
        """
        return self._raw_client

    def create_or_identify_user(
        self,
        workspace_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Endpoint for creating or identifying a user within the specified Workspace. If the user already exists, this will identify them and potentially update user attributes. If they don't exist, it will create a new user. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

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
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.client_api_user.create_or_identify_user(
            workspace_id="workspaceId",
            request={"userId": "user123", "attributes": {}},
        )
        """
        _response = self._raw_client.create_or_identify_user(
            workspace_id, request=request, request_options=request_options
        )
        return _response.data


class AsyncClientApiUserClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClientApiUserClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClientApiUserClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClientApiUserClient
        """
        return self._raw_client

    async def create_or_identify_user(
        self,
        workspace_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Endpoint for creating or identifying a user within the specified Workspace. If the user already exists, this will identify them and potentially update user attributes. If they don't exist, it will create a new user. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

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
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.client_api_user.create_or_identify_user(
                workspace_id="workspaceId",
                request={"userId": "user123", "attributes": {}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_or_identify_user(
            workspace_id, request=request, request_options=request_options
        )
        return _response.data
