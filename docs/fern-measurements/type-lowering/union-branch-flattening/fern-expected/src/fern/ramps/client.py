

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.fiat_source import FiatSource
from ..types.ramp import Ramp
from ..types.ramp_method import RampMethod
from ..types.ticket import Ticket
from .raw_client import AsyncRawRampsClient, RawRampsClient
from .types.ramp_request_direction import RampRequestDirection
from .types.ramp_request_payment_instructions import RampRequestPaymentInstructions


OMIT = typing.cast(typing.Any, ...)


class RampsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRampsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRampsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRampsClient
        """
        return self._raw_client

    def create_ramp(
        self,
        *,
        amount: str,
        direction: typing.Optional[RampRequestDirection] = OMIT,
        source: typing.Optional[FiatSource] = OMIT,
        destination: typing.Optional[str] = OMIT,
        payment_instructions: typing.Optional[RampRequestPaymentInstructions] = OMIT,
        hops: typing.Optional[int] = OMIT,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ramp:
        """
        Parameters
        ----------
        amount : str

        direction : typing.Optional[RampRequestDirection]

        source : typing.Optional[FiatSource]

        destination : typing.Optional[str]

        payment_instructions : typing.Optional[RampRequestPaymentInstructions]

        hops : typing.Optional[int]

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ramp
            The ramp.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.ramps.create_ramp(
            amount="amount",
        )
        """
        _response = self._raw_client.create_ramp(
            amount=amount,
            direction=direction,
            source=source,
            destination=destination,
            payment_instructions=payment_instructions,
            hops=hops,
            note=note,
            request_options=request_options,
        )
        return _response.data

    def list_methods(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[RampMethod]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RampMethod]
            The methods.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.ramps.list_methods()
        """
        _response = self._raw_client.list_methods(request_options=request_options)
        return _response.data

    def list_tickets(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Ticket]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Ticket]
            The tickets.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.ramps.list_tickets()
        """
        _response = self._raw_client.list_tickets(request_options=request_options)
        return _response.data


class AsyncRampsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRampsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRampsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRampsClient
        """
        return self._raw_client

    async def create_ramp(
        self,
        *,
        amount: str,
        direction: typing.Optional[RampRequestDirection] = OMIT,
        source: typing.Optional[FiatSource] = OMIT,
        destination: typing.Optional[str] = OMIT,
        payment_instructions: typing.Optional[RampRequestPaymentInstructions] = OMIT,
        hops: typing.Optional[int] = OMIT,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ramp:
        """
        Parameters
        ----------
        amount : str

        direction : typing.Optional[RampRequestDirection]

        source : typing.Optional[FiatSource]

        destination : typing.Optional[str]

        payment_instructions : typing.Optional[RampRequestPaymentInstructions]

        hops : typing.Optional[int]

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ramp
            The ramp.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ramps.create_ramp(
                amount="amount",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_ramp(
            amount=amount,
            direction=direction,
            source=source,
            destination=destination,
            payment_instructions=payment_instructions,
            hops=hops,
            note=note,
            request_options=request_options,
        )
        return _response.data

    async def list_methods(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[RampMethod]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RampMethod]
            The methods.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ramps.list_methods()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_methods(request_options=request_options)
        return _response.data

    async def list_tickets(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Ticket]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Ticket]
            The tickets.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ramps.list_tickets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_tickets(request_options=request_options)
        return _response.data
