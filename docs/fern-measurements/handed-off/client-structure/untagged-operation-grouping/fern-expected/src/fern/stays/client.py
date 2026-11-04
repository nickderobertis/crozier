

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.stay import Stay
from .raw_client import AsyncRawStaysClient, RawStaysClient


class StaysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStaysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStaysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStaysClient
        """
        return self._raw_client

    def list_stays(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Stay]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Stay]
            Every stay.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.stays.list_stays()
        """
        _response = self._raw_client.list_stays(request_options=request_options)
        return _response.data

    def get_stay(self, stay_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Stay:
        """
        Parameters
        ----------
        stay_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Stay
            One stay.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.stays.get_stay(
            stay_id="stayId",
        )
        """
        _response = self._raw_client.get_stay(stay_id, request_options=request_options)
        return _response.data


class AsyncStaysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStaysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStaysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStaysClient
        """
        return self._raw_client

    async def list_stays(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Stay]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Stay]
            Every stay.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.stays.list_stays()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_stays(request_options=request_options)
        return _response.data

    async def get_stay(self, stay_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Stay:
        """
        Parameters
        ----------
        stay_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Stay
            One stay.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.stays.get_stay(
                stay_id="stayId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_stay(stay_id, request_options=request_options)
        return _response.data
