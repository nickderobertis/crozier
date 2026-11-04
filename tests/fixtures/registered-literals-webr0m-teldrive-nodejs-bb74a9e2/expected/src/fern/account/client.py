

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_profile import UserProfile
from .raw_client import AsyncRawAccountClient, RawAccountClient


class AccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountClient
        """
        return self._raw_client

    def get_current_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> UserProfile:
        """
        Return the authenticated user profile.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserProfile
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.account.get_current_user()
        """
        _response = self._raw_client.get_current_user(request_options=request_options)
        return _response.data

    def get_profile_photo(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Iterator[bytes]:
        """
        Return the authenticated Telegram user's small profile photo.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.account.get_profile_photo()
        """
        with self._raw_client.get_profile_photo(request_options=request_options) as r:
            yield from r.data

    def logout_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Revoke the current session.

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

        client = FernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )
        client.account.logout_session()
        """
        _response = self._raw_client.logout_session(request_options=request_options)
        return _response.data


class AsyncAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountClient
        """
        return self._raw_client

    async def get_current_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> UserProfile:
        """
        Return the authenticated user profile.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserProfile
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account.get_current_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_user(request_options=request_options)
        return _response.data

    async def get_profile_photo(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Return the authenticated Telegram user's small profile photo.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account.get_profile_photo()


        asyncio.run(main())
        """
        async with self._raw_client.get_profile_photo(request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def logout_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Revoke the current session.

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

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account.logout_session()


        asyncio.run(main())
        """
        _response = await self._raw_client.logout_session(request_options=request_options)
        return _response.data
