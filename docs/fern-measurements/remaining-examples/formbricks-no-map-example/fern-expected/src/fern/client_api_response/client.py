

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawClientApiResponseClient, RawClientApiResponseClient


OMIT = typing.cast(typing.Any, ...)


class ClientApiResponseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClientApiResponseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClientApiResponseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClientApiResponseClient
        """
        return self._raw_client

    def update_response(
        self,
        workspace_id: str,
        response_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update an existing response for example when you want to mark a response as finished or you want to change an existing response's value. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        workspace_id : str
            The ID of the Workspace. Deprecated alias `environmentId`.

        response_id : str

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
        client.client_api_response.update_response(
            workspace_id="workspaceId",
            response_id="responseId",
            request={
                "data": {"tcgls0063n8ri7dtrbnepcmz": "Who? Who? Who?"},
                "finished": True,
            },
        )
        """
        _response = self._raw_client.update_response(
            workspace_id, response_id, request=request, request_options=request_options
        )
        return _response.data

    def create_response(
        self,
        workspace_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Create a response for a survey and its fields with the user's responses. The userId & meta here is optional. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

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
        client.client_api_response.create_response(
            workspace_id="workspaceId",
            request={"surveyId": "survey123", "responses": {}},
        )
        """
        _response = self._raw_client.create_response(workspace_id, request=request, request_options=request_options)
        return _response.data


class AsyncClientApiResponseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClientApiResponseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClientApiResponseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClientApiResponseClient
        """
        return self._raw_client

    async def update_response(
        self,
        workspace_id: str,
        response_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update an existing response for example when you want to mark a response as finished or you want to change an existing response's value. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        workspace_id : str
            The ID of the Workspace. Deprecated alias `environmentId`.

        response_id : str

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
            await client.client_api_response.update_response(
                workspace_id="workspaceId",
                response_id="responseId",
                request={
                    "data": {"tcgls0063n8ri7dtrbnepcmz": "Who? Who? Who?"},
                    "finished": True,
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_response(
            workspace_id, response_id, request=request, request_options=request_options
        )
        return _response.data

    async def create_response(
        self,
        workspace_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Create a response for a survey and its fields with the user's responses. The userId & meta here is optional. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

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
            await client.client_api_response.create_response(
                workspace_id="workspaceId",
                request={"surveyId": "survey123", "responses": {}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_response(
            workspace_id, request=request, request_options=request_options
        )
        return _response.data
