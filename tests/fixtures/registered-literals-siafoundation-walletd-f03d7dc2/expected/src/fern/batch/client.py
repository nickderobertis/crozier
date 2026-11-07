

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address import Address
from ..types.address_siacoin_elements_response import AddressSiacoinElementsResponse
from ..types.address_siafund_elements_response import AddressSiafundElementsResponse
from ..types.balance import Balance
from ..types.event import Event
from .raw_client import AsyncRawBatchClient, RawBatchClient


OMIT = typing.cast(typing.Any, ...)


class BatchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBatchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBatchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBatchClient
        """
        return self._raw_client

    def post_batch_addresses_balance(
        self, *, addresses: typing.Sequence[Address], request_options: typing.Optional[RequestOptions] = None
    ) -> Balance:
        """
        Returns the aggregate balance for all supplied addresses.

        Parameters
        ----------
        addresses : typing.Sequence[Address]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Balance
            Combined balance across addresses.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.batch.post_batch_addresses_balance(
            addresses=["addresses"],
        )
        """
        _response = self._raw_client.post_batch_addresses_balance(addresses=addresses, request_options=request_options)
        return _response.data

    def post_batch_addresses_events(
        self,
        *,
        addresses: typing.Sequence[Address],
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Event]:
        """
        Parameters
        ----------
        addresses : typing.Sequence[Address]

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 100).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Event]
            Events touching any of the supplied addresses.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.batch.post_batch_addresses_events(
            addresses=["addresses"],
        )
        """
        _response = self._raw_client.post_batch_addresses_events(
            addresses=addresses, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def post_batch_addresses_siacoin_outputs(
        self,
        *,
        addresses: typing.Sequence[Address],
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddressSiacoinElementsResponse:
        """
        Parameters
        ----------
        addresses : typing.Sequence[Address]

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 100).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddressSiacoinElementsResponse
            Unspent siacoin outputs for the supplied addresses.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.batch.post_batch_addresses_siacoin_outputs(
            addresses=["addresses"],
        )
        """
        _response = self._raw_client.post_batch_addresses_siacoin_outputs(
            addresses=addresses, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def post_batch_addresses_siafund_outputs(
        self,
        *,
        addresses: typing.Sequence[Address],
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddressSiafundElementsResponse:
        """
        Parameters
        ----------
        addresses : typing.Sequence[Address]

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 100).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddressSiafundElementsResponse
            Unspent siafund outputs for the supplied addresses.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.batch.post_batch_addresses_siafund_outputs(
            addresses=["addresses"],
        )
        """
        _response = self._raw_client.post_batch_addresses_siafund_outputs(
            addresses=addresses, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data


class AsyncBatchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBatchClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBatchClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBatchClient
        """
        return self._raw_client

    async def post_batch_addresses_balance(
        self, *, addresses: typing.Sequence[Address], request_options: typing.Optional[RequestOptions] = None
    ) -> Balance:
        """
        Returns the aggregate balance for all supplied addresses.

        Parameters
        ----------
        addresses : typing.Sequence[Address]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Balance
            Combined balance across addresses.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.batch.post_batch_addresses_balance(
                addresses=["addresses"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_batch_addresses_balance(
            addresses=addresses, request_options=request_options
        )
        return _response.data

    async def post_batch_addresses_events(
        self,
        *,
        addresses: typing.Sequence[Address],
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Event]:
        """
        Parameters
        ----------
        addresses : typing.Sequence[Address]

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 100).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Event]
            Events touching any of the supplied addresses.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.batch.post_batch_addresses_events(
                addresses=["addresses"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_batch_addresses_events(
            addresses=addresses, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def post_batch_addresses_siacoin_outputs(
        self,
        *,
        addresses: typing.Sequence[Address],
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddressSiacoinElementsResponse:
        """
        Parameters
        ----------
        addresses : typing.Sequence[Address]

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 100).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddressSiacoinElementsResponse
            Unspent siacoin outputs for the supplied addresses.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.batch.post_batch_addresses_siacoin_outputs(
                addresses=["addresses"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_batch_addresses_siacoin_outputs(
            addresses=addresses, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def post_batch_addresses_siafund_outputs(
        self,
        *,
        addresses: typing.Sequence[Address],
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddressSiafundElementsResponse:
        """
        Parameters
        ----------
        addresses : typing.Sequence[Address]

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 100).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddressSiafundElementsResponse
            Unspent siafund outputs for the supplied addresses.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.batch.post_batch_addresses_siafund_outputs(
                addresses=["addresses"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_batch_addresses_siafund_outputs(
            addresses=addresses, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data
