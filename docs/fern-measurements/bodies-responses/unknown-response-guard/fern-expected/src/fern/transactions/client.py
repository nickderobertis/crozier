

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tx_cbor import TxCbor
from ..types.tx_info import TxInfo
from .raw_client import AsyncRawTransactionsClient, RawTransactionsClient


OMIT = typing.cast(typing.Any, ...)


class TransactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransactionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransactionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransactionsClient
        """
        return self._raw_client

    def get_tx_cbor(
        self,
        *,
        tx_hashes: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TxCbor:
        """
        Parameters
        ----------
        tx_hashes : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TxCbor
            The raw transactions.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.transactions.get_tx_cbor()
        """
        _response = self._raw_client.get_tx_cbor(tx_hashes=tx_hashes, request_options=request_options)
        return _response.data

    def get_tx_info(
        self,
        *,
        tx_hashes: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TxInfo:
        """
        Parameters
        ----------
        tx_hashes : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TxInfo
            Typed transactions.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.transactions.get_tx_info()
        """
        _response = self._raw_client.get_tx_info(tx_hashes=tx_hashes, request_options=request_options)
        return _response.data


class AsyncTransactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransactionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransactionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransactionsClient
        """
        return self._raw_client

    async def get_tx_cbor(
        self,
        *,
        tx_hashes: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TxCbor:
        """
        Parameters
        ----------
        tx_hashes : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TxCbor
            The raw transactions.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.transactions.get_tx_cbor()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tx_cbor(tx_hashes=tx_hashes, request_options=request_options)
        return _response.data

    async def get_tx_info(
        self,
        *,
        tx_hashes: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TxInfo:
        """
        Parameters
        ----------
        tx_hashes : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TxInfo
            Typed transactions.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.transactions.get_tx_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tx_info(tx_hashes=tx_hashes, request_options=request_options)
        return _response.data
