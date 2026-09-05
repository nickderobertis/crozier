

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_block import GetBlock
from ..types.get_ethereum_balance import GetEthereumBalance
from ..types.get_exchange_rate import GetExchangeRate
from ..types.get_gas_price import GetGasPrice
from ..types.get_last_block_number import GetLastBlockNumber
from ..types.get_token import GetToken
from ..types.get_token_balance import GetTokenBalance
from ..types.get_transactions import GetTransactions
from .raw_client import AsyncRawInfoRequestsClient, RawInfoRequestsClient


OMIT = typing.cast(typing.Any, ...)


class InfoRequestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInfoRequestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInfoRequestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInfoRequestsClient
        """
        return self._raw_client

    def get_block(
        self, *, authorization: str, block: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBlock:
        """
        Returns information of an ethereum block with or without transactions

        Parameters
        ----------
        authorization : str
            API Key

        block : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBlock


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.info_requests.get_block(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            block="5000000",
        )
        """
        _response = self._raw_client.get_block(
            authorization=authorization, block=block, request_options=request_options
        )
        return _response.data

    def get_ethereum_balance(
        self, *, authorization: str, ethereumaddress: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetEthereumBalance:
        """
        Returns the ethereum balance of a given address.

        Parameters
        ----------
        authorization : str
            API Key

        ethereumaddress : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEthereumBalance


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.info_requests.get_ethereum_balance(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            ethereumaddress="0xa1f36016221d48ce7f15cde7b826a4fbe09bacce",
        )
        """
        _response = self._raw_client.get_ethereum_balance(
            authorization=authorization, ethereumaddress=ethereumaddress, request_options=request_options
        )
        return _response.data

    def get_exchange_rate(
        self, *, authorization: str, currency: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetExchangeRate:
        """
        Returns the current Ethereum price in Euro or US Dollar.

        Parameters
        ----------
        authorization : str
            API Key

        currency : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetExchangeRate


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.info_requests.get_exchange_rate(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            currency="eur",
        )
        """
        _response = self._raw_client.get_exchange_rate(
            authorization=authorization, currency=currency, request_options=request_options
        )
        return _response.data

    def get_gas_price(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetGasPrice:
        """
        Returns the current gas price in GWEI.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGasPrice


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.info_requests.get_gas_price(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
        )
        """
        _response = self._raw_client.get_gas_price(authorization=authorization, request_options=request_options)
        return _response.data

    def get_last_block_number(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetLastBlockNumber:
        """
        Returns the block number of the last mined ethereum block.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLastBlockNumber


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.info_requests.get_last_block_number(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
        )
        """
        _response = self._raw_client.get_last_block_number(authorization=authorization, request_options=request_options)
        return _response.data

    def get_token(
        self, *, authorization: str, contractaddress: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetToken:
        """
        Returns information about a specific ERC20 token like name, symbol, decimal places and total supply.

        Parameters
        ----------
        authorization : str
            API Key

        contractaddress : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetToken


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.info_requests.get_token(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            contractaddress="0x5b86a33f0c232fe909eb4602a9d039072869d915",
        )
        """
        _response = self._raw_client.get_token(
            authorization=authorization, contractaddress=contractaddress, request_options=request_options
        )
        return _response.data

    def get_token_balance(
        self,
        *,
        authorization: str,
        contractaddress: str,
        ethereumaddress: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTokenBalance:
        """
        Returns the token balance of a given address.

        Parameters
        ----------
        authorization : str
            API Key

        contractaddress : str

        ethereumaddress : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTokenBalance


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.info_requests.get_token_balance(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            contractaddress="0x5b86a33f0c232fe909eb4602a9d039072869d915",
            ethereumaddress="0xa1f36016221d48ce7f15cde7b826a4fbe09bacce",
        )
        """
        _response = self._raw_client.get_token_balance(
            authorization=authorization,
            contractaddress=contractaddress,
            ethereumaddress=ethereumaddress,
            request_options=request_options,
        )
        return _response.data

    def get_transactions(
        self, *, authorization: str, txid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTransactions:
        """
        Returns information like confirmations, token contract address, amount, gas price and more of a given transaction.

        Parameters
        ----------
        authorization : str
            API Key

        txid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTransactions


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.info_requests.get_transactions(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            txid="0x8ab5543bc103bdd908681da501d03c2c495afd7fde5ed104935ba97b1550d65b",
        )
        """
        _response = self._raw_client.get_transactions(
            authorization=authorization, txid=txid, request_options=request_options
        )
        return _response.data


class AsyncInfoRequestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInfoRequestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInfoRequestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInfoRequestsClient
        """
        return self._raw_client

    async def get_block(
        self, *, authorization: str, block: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetBlock:
        """
        Returns information of an ethereum block with or without transactions

        Parameters
        ----------
        authorization : str
            API Key

        block : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetBlock


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.info_requests.get_block(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
                block="5000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_block(
            authorization=authorization, block=block, request_options=request_options
        )
        return _response.data

    async def get_ethereum_balance(
        self, *, authorization: str, ethereumaddress: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetEthereumBalance:
        """
        Returns the ethereum balance of a given address.

        Parameters
        ----------
        authorization : str
            API Key

        ethereumaddress : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEthereumBalance


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.info_requests.get_ethereum_balance(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
                ethereumaddress="0xa1f36016221d48ce7f15cde7b826a4fbe09bacce",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ethereum_balance(
            authorization=authorization, ethereumaddress=ethereumaddress, request_options=request_options
        )
        return _response.data

    async def get_exchange_rate(
        self, *, authorization: str, currency: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetExchangeRate:
        """
        Returns the current Ethereum price in Euro or US Dollar.

        Parameters
        ----------
        authorization : str
            API Key

        currency : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetExchangeRate


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.info_requests.get_exchange_rate(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
                currency="eur",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_exchange_rate(
            authorization=authorization, currency=currency, request_options=request_options
        )
        return _response.data

    async def get_gas_price(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetGasPrice:
        """
        Returns the current gas price in GWEI.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGasPrice


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.info_requests.get_gas_price(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_gas_price(authorization=authorization, request_options=request_options)
        return _response.data

    async def get_last_block_number(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetLastBlockNumber:
        """
        Returns the block number of the last mined ethereum block.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLastBlockNumber


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.info_requests.get_last_block_number(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_last_block_number(
            authorization=authorization, request_options=request_options
        )
        return _response.data

    async def get_token(
        self, *, authorization: str, contractaddress: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetToken:
        """
        Returns information about a specific ERC20 token like name, symbol, decimal places and total supply.

        Parameters
        ----------
        authorization : str
            API Key

        contractaddress : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetToken


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.info_requests.get_token(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
                contractaddress="0x5b86a33f0c232fe909eb4602a9d039072869d915",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_token(
            authorization=authorization, contractaddress=contractaddress, request_options=request_options
        )
        return _response.data

    async def get_token_balance(
        self,
        *,
        authorization: str,
        contractaddress: str,
        ethereumaddress: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetTokenBalance:
        """
        Returns the token balance of a given address.

        Parameters
        ----------
        authorization : str
            API Key

        contractaddress : str

        ethereumaddress : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTokenBalance


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.info_requests.get_token_balance(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
                contractaddress="0x5b86a33f0c232fe909eb4602a9d039072869d915",
                ethereumaddress="0xa1f36016221d48ce7f15cde7b826a4fbe09bacce",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_token_balance(
            authorization=authorization,
            contractaddress=contractaddress,
            ethereumaddress=ethereumaddress,
            request_options=request_options,
        )
        return _response.data

    async def get_transactions(
        self, *, authorization: str, txid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTransactions:
        """
        Returns information like confirmations, token contract address, amount, gas price and more of a given transaction.

        Parameters
        ----------
        authorization : str
            API Key

        txid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTransactions


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.info_requests.get_transactions(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
                txid="0x8ab5543bc103bdd908681da501d03c2c495afd7fde5ed104935ba97b1550d65b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_transactions(
            authorization=authorization, txid=txid, request_options=request_options
        )
        return _response.data
