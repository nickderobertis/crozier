

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.clear_address import ClearAddress
from ..types.send_ethereum import SendEthereum
from ..types.send_token import SendToken
from .raw_client import AsyncRawTransactionRequestsClient, RawTransactionRequestsClient


OMIT = typing.cast(typing.Any, ...)


class TransactionRequestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransactionRequestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransactionRequestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransactionRequestsClient
        """
        return self._raw_client

    def clear_address(
        self,
        *,
        authorization: str,
        ethereumaddress: str,
        newaddress: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClearAddress:
        """
        Sends all available ethereum funds of an address to a specified receiver address.

        Parameters
        ----------
        authorization : str
            API Key

        ethereumaddress : str

        newaddress : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClearAddress


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.transaction_requests.clear_address(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            ethereumaddress="0x3a32c4c31fe8d2a89976af5d284a94a040b44aa8",
            newaddress="0xef4943d727e34280a2efa0b3352dfd61f508ee48",
            password="padN39QkRA2hJ",
        )
        """
        _response = self._raw_client.clear_address(
            authorization=authorization,
            ethereumaddress=ethereumaddress,
            newaddress=newaddress,
            password=password,
            request_options=request_options,
        )
        return _response.data

    def send_ethereum(
        self,
        *,
        authorization: str,
        amount: float,
        from_: str,
        password: str,
        to: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendEthereum:
        """
        Sends ethereum from an address controlled by the account to a specified receiver address.

        Parameters
        ----------
        authorization : str
            API Key

        amount : float

        from_ : str

        password : str

        to : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendEthereum


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.transaction_requests.send_ethereum(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            amount=0.01,
            from_="0x3a32c4c31fe8d2a89976af5d284a94a040b44aa8",
            password="padN39QkRA2hJ",
            to="0xef4943d727e34280a2efa0b3352dfd61f508ee48",
        )
        """
        _response = self._raw_client.send_ethereum(
            authorization=authorization,
            amount=amount,
            from_=from_,
            password=password,
            to=to,
            request_options=request_options,
        )
        return _response.data

    def send_token(
        self,
        *,
        authorization: str,
        amount: int,
        contractaddress: str,
        from_: str,
        identifier: str,
        password: str,
        to: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendToken:
        """
        Sends ERC20 tokens from an address controlled by the account to a specified receiver address. The token contract address is needed to specify the token. The use of the identifier parameter is recommend and awaits an unique string. Whenever a transaction is beeing sent, the identifier is checked and the transaction gets dropped if there is one with that identifier already.

        Parameters
        ----------
        authorization : str
            API Key

        amount : int

        contractaddress : str

        from_ : str

        identifier : str

        password : str

        to : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendToken


        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.transaction_requests.send_token(
            authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
            amount=5,
            contractaddress="0xdac17f958d2ee523a2206206994597c13d831ec7",
            from_="0x3a32c4c31fe8d2a89976af5d284a94a040b44aa8",
            identifier="CN562",
            password="padN39QkRA2hJ",
            to="0xef4943d727e34280a2efa0b3352dfd61f508ee48",
        )
        """
        _response = self._raw_client.send_token(
            authorization=authorization,
            amount=amount,
            contractaddress=contractaddress,
            from_=from_,
            identifier=identifier,
            password=password,
            to=to,
            request_options=request_options,
        )
        return _response.data


class AsyncTransactionRequestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransactionRequestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransactionRequestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransactionRequestsClient
        """
        return self._raw_client

    async def clear_address(
        self,
        *,
        authorization: str,
        ethereumaddress: str,
        newaddress: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClearAddress:
        """
        Sends all available ethereum funds of an address to a specified receiver address.

        Parameters
        ----------
        authorization : str
            API Key

        ethereumaddress : str

        newaddress : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClearAddress


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.transaction_requests.clear_address(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
                ethereumaddress="0x3a32c4c31fe8d2a89976af5d284a94a040b44aa8",
                newaddress="0xef4943d727e34280a2efa0b3352dfd61f508ee48",
                password="padN39QkRA2hJ",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clear_address(
            authorization=authorization,
            ethereumaddress=ethereumaddress,
            newaddress=newaddress,
            password=password,
            request_options=request_options,
        )
        return _response.data

    async def send_ethereum(
        self,
        *,
        authorization: str,
        amount: float,
        from_: str,
        password: str,
        to: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendEthereum:
        """
        Sends ethereum from an address controlled by the account to a specified receiver address.

        Parameters
        ----------
        authorization : str
            API Key

        amount : float

        from_ : str

        password : str

        to : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendEthereum


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.transaction_requests.send_ethereum(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
                amount=0.01,
                from_="0x3a32c4c31fe8d2a89976af5d284a94a040b44aa8",
                password="padN39QkRA2hJ",
                to="0xef4943d727e34280a2efa0b3352dfd61f508ee48",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_ethereum(
            authorization=authorization,
            amount=amount,
            from_=from_,
            password=password,
            to=to,
            request_options=request_options,
        )
        return _response.data

    async def send_token(
        self,
        *,
        authorization: str,
        amount: int,
        contractaddress: str,
        from_: str,
        identifier: str,
        password: str,
        to: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendToken:
        """
        Sends ERC20 tokens from an address controlled by the account to a specified receiver address. The token contract address is needed to specify the token. The use of the identifier parameter is recommend and awaits an unique string. Whenever a transaction is beeing sent, the identifier is checked and the transaction gets dropped if there is one with that identifier already.

        Parameters
        ----------
        authorization : str
            API Key

        amount : int

        contractaddress : str

        from_ : str

        identifier : str

        password : str

        to : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendToken


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.transaction_requests.send_token(
                authorization="q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m",
                amount=5,
                contractaddress="0xdac17f958d2ee523a2206206994597c13d831ec7",
                from_="0x3a32c4c31fe8d2a89976af5d284a94a040b44aa8",
                identifier="CN562",
                password="padN39QkRA2hJ",
                to="0xef4943d727e34280a2efa0b3352dfd61f508ee48",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_token(
            authorization=authorization,
            amount=amount,
            contractaddress=contractaddress,
            from_=from_,
            identifier=identifier,
            password=password,
            to=to,
            request_options=request_options,
        )
        return _response.data
