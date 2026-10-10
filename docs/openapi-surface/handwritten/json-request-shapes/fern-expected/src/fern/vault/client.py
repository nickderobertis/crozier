

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawVaultClient, RawVaultClient


OMIT = typing.cast(typing.Any, ...)


class VaultClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVaultClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVaultClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVaultClient
        """
        return self._raw_client

    def list_bundles(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Bundle names

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.vault.list_bundles()
        """
        _response = self._raw_client.list_bundles(request_options=request_options)
        return _response.data

    def deposit_bundle(self, *, request: bytes, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.vault.deposit_bundle(
            request="string",
        )
        """
        _response = self._raw_client.deposit_bundle(request=request, request_options=request_options)
        return _response.data


class AsyncVaultClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVaultClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVaultClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVaultClient
        """
        return self._raw_client

    async def list_bundles(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Bundle names

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vault.list_bundles()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_bundles(request_options=request_options)
        return _response.data

    async def deposit_bundle(self, *, request: bytes, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : bytes

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.vault.deposit_bundle(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deposit_bundle(request=request, request_options=request_options)
        return _response.data
