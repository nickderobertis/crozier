

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.kitty_gender import KittyGender
from ..types.kitty_status import KittyStatus
from ..types.parent import Parent
from .raw_client import AsyncRawMutationClient, RawMutationClient


OMIT = typing.cast(typing.Any, ...)


class MutationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMutationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMutationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMutationClient
        """
        return self._raw_client

    def set_kitty_property(
        self,
        *,
        owner: typing.Optional[str] = OMIT,
        dna: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        gender: typing.Optional[KittyGender] = OMIT,
        mom: typing.Optional[Parent] = OMIT,
        dad: typing.Optional[Parent] = OMIT,
        breedings: typing.Optional[float] = OMIT,
        status: typing.Optional[KittyStatus] = OMIT,
        for_sale: typing.Optional[bool] = OMIT,
        price: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Change any property of the kitty, should accept partial properties of kitty

        Parameters
        ----------
        owner : typing.Optional[str]
            address of owner

        dna : typing.Optional[str]
            should be string, as js can't handle long format

        name : typing.Optional[str]

        gender : typing.Optional[KittyGender]

        mom : typing.Optional[Parent]

        dad : typing.Optional[Parent]

        breedings : typing.Optional[float]

        status : typing.Optional[KittyStatus]

        for_sale : typing.Optional[bool]

        price : typing.Optional[float]
            if not present, will be considered not for sale

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.mutation.set_kitty_property()
        """
        _response = self._raw_client.set_kitty_property(
            owner=owner,
            dna=dna,
            name=name,
            gender=gender,
            mom=mom,
            dad=dad,
            breedings=breedings,
            status=status,
            for_sale=for_sale,
            price=price,
            request_options=request_options,
        )
        return _response.data


class AsyncMutationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMutationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMutationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMutationClient
        """
        return self._raw_client

    async def set_kitty_property(
        self,
        *,
        owner: typing.Optional[str] = OMIT,
        dna: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        gender: typing.Optional[KittyGender] = OMIT,
        mom: typing.Optional[Parent] = OMIT,
        dad: typing.Optional[Parent] = OMIT,
        breedings: typing.Optional[float] = OMIT,
        status: typing.Optional[KittyStatus] = OMIT,
        for_sale: typing.Optional[bool] = OMIT,
        price: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Change any property of the kitty, should accept partial properties of kitty

        Parameters
        ----------
        owner : typing.Optional[str]
            address of owner

        dna : typing.Optional[str]
            should be string, as js can't handle long format

        name : typing.Optional[str]

        gender : typing.Optional[KittyGender]

        mom : typing.Optional[Parent]

        dad : typing.Optional[Parent]

        breedings : typing.Optional[float]

        status : typing.Optional[KittyStatus]

        for_sale : typing.Optional[bool]

        price : typing.Optional[float]
            if not present, will be considered not for sale

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.mutation.set_kitty_property()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_kitty_property(
            owner=owner,
            dna=dna,
            name=name,
            gender=gender,
            mom=mom,
            dad=dad,
            breedings=breedings,
            status=status,
            for_sale=for_sale,
            price=price,
            request_options=request_options,
        )
        return _response.data
