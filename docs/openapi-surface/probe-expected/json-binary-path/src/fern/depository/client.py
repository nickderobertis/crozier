

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDepositoryClient, RawDepositoryClient


OMIT = typing.cast(typing.Any, ...)


class DepositoryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDepositoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDepositoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDepositoryClient
        """
        return self._raw_client

    def deposit_parcel(
        self, locker: str, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        locker : str

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
        client.depository.deposit_parcel(
            locker="locker",
            request="string",
        )
        """
        _response = self._raw_client.deposit_parcel(locker, request=request, request_options=request_options)
        return _response.data

    def list_parcels(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Parcel names

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.depository.list_parcels()
        """
        _response = self._raw_client.list_parcels(request_options=request_options)
        return _response.data


class AsyncDepositoryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDepositoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDepositoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDepositoryClient
        """
        return self._raw_client

    async def deposit_parcel(
        self, locker: str, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        locker : str

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
            await client.depository.deposit_parcel(
                locker="locker",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deposit_parcel(locker, request=request, request_options=request_options)
        return _response.data

    async def list_parcels(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Parcel names

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.depository.list_parcels()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_parcels(request_options=request_options)
        return _response.data
