

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.check_addresses_response import CheckAddressesResponse
from ..types.state_response import StateResponse
from .raw_client import AsyncRawMiscClient, RawMiscClient


OMIT = typing.cast(typing.Any, ...)


class MiscClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMiscClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMiscClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMiscClient
        """
        return self._raw_client

    def get_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> StateResponse:
        """
        Returns build metadata and runtime information about the walletd instance.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StateResponse
            Current daemon state.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.misc.get_state()
        """
        _response = self._raw_client.get_state(request_options=request_options)
        return _response.data

    def get_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Dict[str, typing.Any]]:
        """
        Returns 200 when walletd is healthy.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Dict[str, typing.Any]]
            Walletd is healthy.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.misc.get_health()
        """
        _response = self._raw_client.get_health(request_options=request_options)
        return _response.data

    def post_check_addresses(
        self, *, addresses: typing.Sequence[Address], request_options: typing.Optional[RequestOptions] = None
    ) -> CheckAddressesResponse:
        """
        Returns whether any supplied addresses are currently tracked by walletd. In personal indexing mode, only registered wallet addresses are recognized.

        Parameters
        ----------
        addresses : typing.Sequence[Address]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckAddressesResponse
            Address membership check result.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.misc.post_check_addresses(
            addresses=["addresses"],
        )
        """
        _response = self._raw_client.post_check_addresses(addresses=addresses, request_options=request_options)
        return _response.data


class AsyncMiscClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMiscClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMiscClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMiscClient
        """
        return self._raw_client

    async def get_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> StateResponse:
        """
        Returns build metadata and runtime information about the walletd instance.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StateResponse
            Current daemon state.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.misc.get_state()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_state(request_options=request_options)
        return _response.data

    async def get_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Dict[str, typing.Any]]:
        """
        Returns 200 when walletd is healthy.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Dict[str, typing.Any]]
            Walletd is healthy.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.misc.get_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_health(request_options=request_options)
        return _response.data

    async def post_check_addresses(
        self, *, addresses: typing.Sequence[Address], request_options: typing.Optional[RequestOptions] = None
    ) -> CheckAddressesResponse:
        """
        Returns whether any supplied addresses are currently tracked by walletd. In personal indexing mode, only registered wallet addresses are recognized.

        Parameters
        ----------
        addresses : typing.Sequence[Address]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckAddressesResponse
            Address membership check result.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.misc.post_check_addresses(
                addresses=["addresses"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_check_addresses(addresses=addresses, request_options=request_options)
        return _response.data
