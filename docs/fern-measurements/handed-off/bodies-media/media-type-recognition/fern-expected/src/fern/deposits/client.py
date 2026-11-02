

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.deposit import Deposit
from .raw_client import AsyncRawDepositsClient, RawDepositsClient


OMIT = typing.cast(typing.Any, ...)


class DepositsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDepositsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDepositsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDepositsClient
        """
        return self._raw_client

    def record_deposit(
        self, *, species: str, grams: float, request_options: typing.Optional[RequestOptions] = None
    ) -> Deposit:
        """
        Parameters
        ----------
        species : str

        grams : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deposit
            The deposit as stored.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.deposits.record_deposit(
            species="species",
            grams=1.1,
        )
        """
        _response = self._raw_client.record_deposit(species=species, grams=grams, request_options=request_options)
        return _response.data

    def record_germination(
        self, deposit_id: str, *, sown: int, sprouted: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        deposit_id : str

        sown : int

        sprouted : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.deposits.record_germination(
            deposit_id="depositId",
            sown=1,
            sprouted=1,
        )
        """
        _response = self._raw_client.record_germination(
            deposit_id, sown=sown, sprouted=sprouted, request_options=request_options
        )
        return _response.data


class AsyncDepositsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDepositsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDepositsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDepositsClient
        """
        return self._raw_client

    async def record_deposit(
        self, *, species: str, grams: float, request_options: typing.Optional[RequestOptions] = None
    ) -> Deposit:
        """
        Parameters
        ----------
        species : str

        grams : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deposit
            The deposit as stored.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.deposits.record_deposit(
                species="species",
                grams=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_deposit(species=species, grams=grams, request_options=request_options)
        return _response.data

    async def record_germination(
        self, deposit_id: str, *, sown: int, sprouted: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        deposit_id : str

        sown : int

        sprouted : int

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
            await client.deposits.record_germination(
                deposit_id="depositId",
                sown=1,
                sprouted=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_germination(
            deposit_id, sown=sown, sprouted=sprouted, request_options=request_options
        )
        return _response.data
