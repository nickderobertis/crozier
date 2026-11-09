

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.platform import Platform
from ..types.token import Token
from .raw_client import AsyncRawTokensClient, RawTokensClient
from .types.post_v1users_tokens_response import PostV1UsersTokensResponse


OMIT = typing.cast(typing.Any, ...)


class TokensClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTokensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTokensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTokensClient
        """
        return self._raw_client

    def register_a_push_token(
        self,
        *,
        platform: Platform,
        token: str,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1UsersTokensResponse:
        """
        Creates the user if the provided id does not exist. Generates a user id if id is omitted.

        Parameters
        ----------
        platform : Platform

        token : str

        id : typing.Optional[str]
            Optional user id. A UUID is generated when omitted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1UsersTokensResponse
            Token registered.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tokens.register_a_push_token(
            platform="apns",
            token="device-token",
        )
        """
        _response = self._raw_client.register_a_push_token(
            platform=platform, token=token, id=id, request_options=request_options
        )
        return _response.data

    def list_a_users_push_tokens(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Token]:
        """
        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Token]
            Tokens for the user. Unknown users currently return an empty list.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tokens.list_a_users_push_tokens(
            user_id="user-123",
        )
        """
        _response = self._raw_client.list_a_users_push_tokens(user_id, request_options=request_options)
        return _response.data

    def delete_a_push_token(
        self, user_id: str, token_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        The current handler deletes by tokenID; userID is part of the route but is not used for authorization.

        Parameters
        ----------
        user_id : str

        token_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tokens.delete_a_push_token(
            user_id="user-123",
            token_id="018f7b7a-a9b7-7a22-9d6f-6fb3c9b6b9c0",
        )
        """
        _response = self._raw_client.delete_a_push_token(user_id, token_id, request_options=request_options)
        return _response.data


class AsyncTokensClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTokensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTokensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTokensClient
        """
        return self._raw_client

    async def register_a_push_token(
        self,
        *,
        platform: Platform,
        token: str,
        id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1UsersTokensResponse:
        """
        Creates the user if the provided id does not exist. Generates a user id if id is omitted.

        Parameters
        ----------
        platform : Platform

        token : str

        id : typing.Optional[str]
            Optional user id. A UUID is generated when omitted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1UsersTokensResponse
            Token registered.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tokens.register_a_push_token(
                platform="apns",
                token="device-token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_a_push_token(
            platform=platform, token=token, id=id, request_options=request_options
        )
        return _response.data

    async def list_a_users_push_tokens(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Token]:
        """
        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Token]
            Tokens for the user. Unknown users currently return an empty list.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tokens.list_a_users_push_tokens(
                user_id="user-123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_a_users_push_tokens(user_id, request_options=request_options)
        return _response.data

    async def delete_a_push_token(
        self, user_id: str, token_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        The current handler deletes by tokenID; userID is part of the route but is not used for authorization.

        Parameters
        ----------
        user_id : str

        token_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tokens.delete_a_push_token(
                user_id="user-123",
                token_id="018f7b7a-a9b7-7a22-9d6f-6fb3c9b6b9c0",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_push_token(user_id, token_id, request_options=request_options)
        return _response.data
