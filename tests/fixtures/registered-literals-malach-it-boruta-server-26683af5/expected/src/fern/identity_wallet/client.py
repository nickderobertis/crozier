

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawIdentityWalletClient, RawIdentityWalletClient


class IdentityWalletClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIdentityWalletClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIdentityWalletClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIdentityWalletClient
        """
        return self._raw_client

    def serve_the_wallet_application(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_wallet.serve_the_wallet_application()
        """
        _response = self._raw_client.serve_the_wallet_application(request_options=request_options)
        return _response.data

    def serve_a_wallet_asset_or_client_side_route(
        self, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        path : str
            Wallet asset filename or client-side route segment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Wallet application page or static asset

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_wallet.serve_a_wallet_asset_or_client_side_route(
            path="path",
        )
        """
        with self._raw_client.serve_a_wallet_asset_or_client_side_route(path, request_options=request_options) as r:
            yield from r.data


class AsyncIdentityWalletClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIdentityWalletClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIdentityWalletClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIdentityWalletClient
        """
        return self._raw_client

    async def serve_the_wallet_application(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_wallet.serve_the_wallet_application()


        asyncio.run(main())
        """
        _response = await self._raw_client.serve_the_wallet_application(request_options=request_options)
        return _response.data

    async def serve_a_wallet_asset_or_client_side_route(
        self, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        path : str
            Wallet asset filename or client-side route segment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Wallet application page or static asset

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_wallet.serve_a_wallet_asset_or_client_side_route(
                path="path",
            )


        asyncio.run(main())
        """
        async with self._raw_client.serve_a_wallet_asset_or_client_side_route(
            path, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk
