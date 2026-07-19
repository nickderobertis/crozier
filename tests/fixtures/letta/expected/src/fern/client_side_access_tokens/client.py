

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawClientSideAccessTokensClient, RawClientSideAccessTokensClient
from .types.client_side_access_tokens_create_client_side_access_token_request_policy_item import (
    ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem,
)
from .types.client_side_access_tokens_create_client_side_access_token_response import (
    ClientSideAccessTokensCreateClientSideAccessTokenResponse,
)
from .types.client_side_access_tokens_list_client_side_access_tokens_response import (
    ClientSideAccessTokensListClientSideAccessTokensResponse,
)


OMIT = typing.cast(typing.Any, ...)


class ClientSideAccessTokensClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClientSideAccessTokensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClientSideAccessTokensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClientSideAccessTokensClient
        """
        return self._raw_client

    def client_side_access_tokens_list_client_side_access_tokens(
        self,
        *,
        agent_id: typing.Optional[str] = None,
        offset: typing.Optional[float] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClientSideAccessTokensListClientSideAccessTokensResponse:
        """
        List all client side access tokens for the current account. This is only available for cloud users.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            The agent ID to filter tokens by. If provided, only tokens for this agent will be returned.

        offset : typing.Optional[float]
            The offset for pagination. Defaults to 0.

        limit : typing.Optional[float]
            The number of tokens to return per page. Defaults to 10.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClientSideAccessTokensListClientSideAccessTokensResponse
            200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.client_side_access_tokens.client_side_access_tokens_list_client_side_access_tokens()
        """
        _response = self._raw_client.client_side_access_tokens_list_client_side_access_tokens(
            agent_id=agent_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def client_side_access_tokens_create_client_side_access_token(
        self,
        *,
        policy: typing.Sequence[ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem],
        hostname: str,
        expires_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClientSideAccessTokensCreateClientSideAccessTokenResponse:
        """
        Create a new client side access token with the specified configuration.

        Parameters
        ----------
        policy : typing.Sequence[ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem]

        hostname : str
            The hostname of the client side application. Please specify the full URL including the protocol (http or https).

        expires_at : typing.Optional[str]
            The expiration date of the token. If not provided, the token will expire in 5 minutes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClientSideAccessTokensCreateClientSideAccessTokenResponse
            201

        Examples
        --------
        from fern.client_side_access_tokens import (
            ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem,
            ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemAccessItem,
            ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemType,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.client_side_access_tokens.client_side_access_tokens_create_client_side_access_token(
            policy=[
                ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem(
                    type=ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemType.AGENT,
                    id="id",
                    access=[
                        ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemAccessItem.READ_MESSAGES
                    ],
                )
            ],
            hostname="hostname",
        )
        """
        _response = self._raw_client.client_side_access_tokens_create_client_side_access_token(
            policy=policy, hostname=hostname, expires_at=expires_at, request_options=request_options
        )
        return _response.data

    def client_side_access_tokens_delete_client_side_access_token(
        self, token: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Delete a client side access token.

        Parameters
        ----------
        token : str
            The access token to delete

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            204

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.client_side_access_tokens.client_side_access_tokens_delete_client_side_access_token(
            token="token",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.client_side_access_tokens_delete_client_side_access_token(
            token, request=request, request_options=request_options
        )
        return _response.data


class AsyncClientSideAccessTokensClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClientSideAccessTokensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClientSideAccessTokensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClientSideAccessTokensClient
        """
        return self._raw_client

    async def client_side_access_tokens_list_client_side_access_tokens(
        self,
        *,
        agent_id: typing.Optional[str] = None,
        offset: typing.Optional[float] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClientSideAccessTokensListClientSideAccessTokensResponse:
        """
        List all client side access tokens for the current account. This is only available for cloud users.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            The agent ID to filter tokens by. If provided, only tokens for this agent will be returned.

        offset : typing.Optional[float]
            The offset for pagination. Defaults to 0.

        limit : typing.Optional[float]
            The number of tokens to return per page. Defaults to 10.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClientSideAccessTokensListClientSideAccessTokensResponse
            200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.client_side_access_tokens.client_side_access_tokens_list_client_side_access_tokens()


        asyncio.run(main())
        """
        _response = await self._raw_client.client_side_access_tokens_list_client_side_access_tokens(
            agent_id=agent_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def client_side_access_tokens_create_client_side_access_token(
        self,
        *,
        policy: typing.Sequence[ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem],
        hostname: str,
        expires_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClientSideAccessTokensCreateClientSideAccessTokenResponse:
        """
        Create a new client side access token with the specified configuration.

        Parameters
        ----------
        policy : typing.Sequence[ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem]

        hostname : str
            The hostname of the client side application. Please specify the full URL including the protocol (http or https).

        expires_at : typing.Optional[str]
            The expiration date of the token. If not provided, the token will expire in 5 minutes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClientSideAccessTokensCreateClientSideAccessTokenResponse
            201

        Examples
        --------
        import asyncio

        from fern.client_side_access_tokens import (
            ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem,
            ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemAccessItem,
            ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemType,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.client_side_access_tokens.client_side_access_tokens_create_client_side_access_token(
                policy=[
                    ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItem(
                        type=ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemType.AGENT,
                        id="id",
                        access=[
                            ClientSideAccessTokensCreateClientSideAccessTokenRequestPolicyItemAccessItem.READ_MESSAGES
                        ],
                    )
                ],
                hostname="hostname",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.client_side_access_tokens_create_client_side_access_token(
            policy=policy, hostname=hostname, expires_at=expires_at, request_options=request_options
        )
        return _response.data

    async def client_side_access_tokens_delete_client_side_access_token(
        self, token: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Delete a client side access token.

        Parameters
        ----------
        token : str
            The access token to delete

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            204

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.client_side_access_tokens.client_side_access_tokens_delete_client_side_access_token(
                token="token",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.client_side_access_tokens_delete_client_side_access_token(
            token, request=request, request_options=request_options
        )
        return _response.data
