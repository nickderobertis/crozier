

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.authentication_resource import AuthenticationResource
from .raw_client import AsyncRawAuthClient, RawAuthClient
from .types.auth_me_response import AuthMeResponse


OMIT = typing.cast(typing.Any, ...)


class AuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthClient
        """
        return self._raw_client

    def redeem(self, *, token: str, request_options: typing.Optional[RequestOptions] = None) -> AuthenticationResource:
        """
        Parameters
        ----------
        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthenticationResource
            `AuthenticationResource`

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.redeem(
            token="token",
        )
        """
        _response = self._raw_client.redeem(token=token, request_options=request_options)
        return _response.data

    def refresh(self, *, request_options: typing.Optional[RequestOptions] = None) -> AuthenticationResource:
        """
        Authenticated, unlike invitation redemption: the credential being renewed is the one the
        request carries, so a client whose token has already expired signs in again rather than
        refreshing.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthenticationResource
            `AuthenticationResource`

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.refresh()
        """
        _response = self._raw_client.refresh(request_options=request_options)
        return _response.data

    def revoke(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.revoke()
        """
        _response = self._raw_client.revoke(request_options=request_options)
        return _response.data

    def me(self, *, request_options: typing.Optional[RequestOptions] = None) -> AuthMeResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthMeResponse
            `UserResource`

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.auth.me()
        """
        _response = self._raw_client.me(request_options=request_options)
        return _response.data


class AsyncAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthClient
        """
        return self._raw_client

    async def redeem(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthenticationResource:
        """
        Parameters
        ----------
        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthenticationResource
            `AuthenticationResource`

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.redeem(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.redeem(token=token, request_options=request_options)
        return _response.data

    async def refresh(self, *, request_options: typing.Optional[RequestOptions] = None) -> AuthenticationResource:
        """
        Authenticated, unlike invitation redemption: the credential being renewed is the one the
        request carries, so a client whose token has already expired signs in again rather than
        refreshing.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthenticationResource
            `AuthenticationResource`

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.refresh()


        asyncio.run(main())
        """
        _response = await self._raw_client.refresh(request_options=request_options)
        return _response.data

    async def revoke(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            await client.auth.revoke()


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke(request_options=request_options)
        return _response.data

    async def me(self, *, request_options: typing.Optional[RequestOptions] = None) -> AuthMeResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthMeResponse
            `UserResource`

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.auth.me()


        asyncio.run(main())
        """
        _response = await self._raw_client.me(request_options=request_options)
        return _response.data
