

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.address_response import AddressResponse
from ..types.btc_balance_response import BtcBalanceResponse
from ..types.estimate_fee_response import EstimateFeeResponse
from ..types.list_transactions_response import ListTransactionsResponse
from ..types.list_unspents_response import ListUnspentsResponse
from ..types.send_btc_response import SendBtcResponse
from .raw_client import AsyncRawOnChainClient, RawOnChainClient


OMIT = typing.cast(typing.Any, ...)


class OnChainClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOnChainClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOnChainClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOnChainClient
        """
        return self._raw_client

    def get_a_bitcoin_address(self, *, request_options: typing.Optional[RequestOptions] = None) -> AddressResponse:
        """
        Get a new Bitcoin address from the internal BDK wallet

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddressResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.on_chain.get_a_bitcoin_address()
        """
        _response = self._raw_client.get_a_bitcoin_address(request_options=request_options)
        return _response.data

    def get_the_btc_balance(
        self, *, skip_sync: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> BtcBalanceResponse:
        """
        Get the node's bitcoin balance for the vanilla and colored wallets

        Parameters
        ----------
        skip_sync : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BtcBalanceResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.on_chain.get_the_btc_balance(
            skip_sync=False,
        )
        """
        _response = self._raw_client.get_the_btc_balance(skip_sync=skip_sync, request_options=request_options)
        return _response.data

    def get_fee_estimation(
        self, *, blocks: int, request_options: typing.Optional[RequestOptions] = None
    ) -> EstimateFeeResponse:
        """
        Get on-chain fee estimation

        Parameters
        ----------
        blocks : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EstimateFeeResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.on_chain.get_fee_estimation(
            blocks=7,
        )
        """
        _response = self._raw_client.get_fee_estimation(blocks=blocks, request_options=request_options)
        return _response.data

    def list_transactions(
        self, *, skip_sync: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> ListTransactionsResponse:
        """
        List the node's on-chain transactions

        Parameters
        ----------
        skip_sync : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTransactionsResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.on_chain.list_transactions(
            skip_sync=False,
        )
        """
        _response = self._raw_client.list_transactions(skip_sync=skip_sync, request_options=request_options)
        return _response.data

    def list_unspents(
        self, *, settled_only: bool, skip_sync: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> ListUnspentsResponse:
        """
        List the unspent outputs of the internal BDK wallet

        Parameters
        ----------
        settled_only : bool

        skip_sync : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListUnspentsResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.on_chain.list_unspents(
            settled_only=False,
            skip_sync=False,
        )
        """
        _response = self._raw_client.list_unspents(
            settled_only=settled_only, skip_sync=skip_sync, request_options=request_options
        )
        return _response.data

    def send_btc(
        self,
        *,
        amount: int,
        address: str,
        fee_rate: int,
        skip_sync: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendBtcResponse:
        """
        Send bitcoins on-chain

        Parameters
        ----------
        amount : int

        address : str

        fee_rate : int

        skip_sync : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendBtcResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.on_chain.send_btc(
            amount=16900,
            address="bcrt1qwxht5tut39dws8tjcf649tp908r8fr2j75c94k",
            fee_rate=5,
            skip_sync=False,
        )
        """
        _response = self._raw_client.send_btc(
            amount=amount, address=address, fee_rate=fee_rate, skip_sync=skip_sync, request_options=request_options
        )
        return _response.data


class AsyncOnChainClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOnChainClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOnChainClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOnChainClient
        """
        return self._raw_client

    async def get_a_bitcoin_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AddressResponse:
        """
        Get a new Bitcoin address from the internal BDK wallet

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddressResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.on_chain.get_a_bitcoin_address()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_bitcoin_address(request_options=request_options)
        return _response.data

    async def get_the_btc_balance(
        self, *, skip_sync: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> BtcBalanceResponse:
        """
        Get the node's bitcoin balance for the vanilla and colored wallets

        Parameters
        ----------
        skip_sync : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BtcBalanceResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.on_chain.get_the_btc_balance(
                skip_sync=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_the_btc_balance(skip_sync=skip_sync, request_options=request_options)
        return _response.data

    async def get_fee_estimation(
        self, *, blocks: int, request_options: typing.Optional[RequestOptions] = None
    ) -> EstimateFeeResponse:
        """
        Get on-chain fee estimation

        Parameters
        ----------
        blocks : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EstimateFeeResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.on_chain.get_fee_estimation(
                blocks=7,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fee_estimation(blocks=blocks, request_options=request_options)
        return _response.data

    async def list_transactions(
        self, *, skip_sync: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> ListTransactionsResponse:
        """
        List the node's on-chain transactions

        Parameters
        ----------
        skip_sync : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTransactionsResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.on_chain.list_transactions(
                skip_sync=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_transactions(skip_sync=skip_sync, request_options=request_options)
        return _response.data

    async def list_unspents(
        self, *, settled_only: bool, skip_sync: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> ListUnspentsResponse:
        """
        List the unspent outputs of the internal BDK wallet

        Parameters
        ----------
        settled_only : bool

        skip_sync : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListUnspentsResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.on_chain.list_unspents(
                settled_only=False,
                skip_sync=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_unspents(
            settled_only=settled_only, skip_sync=skip_sync, request_options=request_options
        )
        return _response.data

    async def send_btc(
        self,
        *,
        amount: int,
        address: str,
        fee_rate: int,
        skip_sync: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendBtcResponse:
        """
        Send bitcoins on-chain

        Parameters
        ----------
        amount : int

        address : str

        fee_rate : int

        skip_sync : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendBtcResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.on_chain.send_btc(
                amount=16900,
                address="bcrt1qwxht5tut39dws8tjcf649tp908r8fr2j75c94k",
                fee_rate=5,
                skip_sync=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_btc(
            amount=amount, address=address, fee_rate=fee_rate, skip_sync=skip_sync, request_options=request_options
        )
        return _response.data
