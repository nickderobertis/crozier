

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTokenClient, RawTokenClient
from .types.authorized_by_token_response import AuthorizedByTokenResponse
from .types.introspect_token_response import IntrospectTokenResponse


class TokenClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTokenClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTokenClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTokenClient
        """
        return self._raw_client

    def authorized_by(self, *, request_options: typing.Optional[RequestOptions] = None) -> AuthorizedByTokenResponse:
        """
        Information about the Authorized User

        Required Scope | `authorized_user:read`

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorizedByTokenResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.token.authorized_by()
        """
        _response = self._raw_client.authorized_by(request_options=request_options)
        return _response.data

    def introspect(self, *, request_options: typing.Optional[RequestOptions] = None) -> IntrospectTokenResponse:
        """
        Information about the authorization token

        <Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/data-clients/getting-started).</Note>

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IntrospectTokenResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.token.introspect()
        """
        _response = self._raw_client.introspect(request_options=request_options)
        return _response.data


class AsyncTokenClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTokenClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTokenClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTokenClient
        """
        return self._raw_client

    async def authorized_by(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthorizedByTokenResponse:
        """
        Information about the Authorized User

        Required Scope | `authorized_user:read`

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorizedByTokenResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.token.authorized_by()


        asyncio.run(main())
        """
        _response = await self._raw_client.authorized_by(request_options=request_options)
        return _response.data

    async def introspect(self, *, request_options: typing.Optional[RequestOptions] = None) -> IntrospectTokenResponse:
        """
        Information about the authorization token

        <Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/data-clients/getting-started).</Note>

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IntrospectTokenResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.token.introspect()


        asyncio.run(main())
        """
        _response = await self._raw_client.introspect(request_options=request_options)
        return _response.data
