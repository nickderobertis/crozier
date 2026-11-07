

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawConnectionsClient, RawConnectionsClient
from .types.post_v3connections_google_docs_token_response import PostV3ConnectionsGoogleDocsTokenResponse
from .types.post_v3connections_slack_token_response import PostV3ConnectionsSlackTokenResponse


OMIT = typing.cast(typing.Any, ...)


class ConnectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConnectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConnectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConnectionsClient
        """
        return self._raw_client

    def post_v3connections_slack_token(
        self, *, team_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV3ConnectionsSlackTokenResponse:
        """
        Get a valid Slack access token for a connected workspace. Automatically refreshes the token if expired.

        Parameters
        ----------
        team_id : str
            The Slack team/workspace ID (e.g., 'T9TK3CUKW')

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV3ConnectionsSlackTokenResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connections.post_v3connections_slack_token(
            team_id="team_id",
        )
        """
        _response = self._raw_client.post_v3connections_slack_token(team_id=team_id, request_options=request_options)
        return _response.data

    def post_v3connections_google_docs_token(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV3ConnectionsGoogleDocsTokenResponse:
        """
        Get a valid Google access token for a connected Google account. Automatically refreshes the token if expired.

        Parameters
        ----------
        email : str
            The Google account email

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV3ConnectionsGoogleDocsTokenResponse
            Default Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.connections.post_v3connections_google_docs_token(
            email="email",
        )
        """
        _response = self._raw_client.post_v3connections_google_docs_token(email=email, request_options=request_options)
        return _response.data


class AsyncConnectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConnectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConnectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConnectionsClient
        """
        return self._raw_client

    async def post_v3connections_slack_token(
        self, *, team_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV3ConnectionsSlackTokenResponse:
        """
        Get a valid Slack access token for a connected workspace. Automatically refreshes the token if expired.

        Parameters
        ----------
        team_id : str
            The Slack team/workspace ID (e.g., 'T9TK3CUKW')

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV3ConnectionsSlackTokenResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connections.post_v3connections_slack_token(
                team_id="team_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v3connections_slack_token(
            team_id=team_id, request_options=request_options
        )
        return _response.data

    async def post_v3connections_google_docs_token(
        self, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV3ConnectionsGoogleDocsTokenResponse:
        """
        Get a valid Google access token for a connected Google account. Automatically refreshes the token if expired.

        Parameters
        ----------
        email : str
            The Google account email

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV3ConnectionsGoogleDocsTokenResponse
            Default Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.connections.post_v3connections_google_docs_token(
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v3connections_google_docs_token(
            email=email, request_options=request_options
        )
        return _response.data
