

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSoundingsClient, RawSoundingsClient


class SoundingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSoundingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSoundingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSoundingsClient
        """
        return self._raw_client

    def list_soundings(
        self, *, depth: int, fathoms: int, cables: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[float]:
        """
        An integer bounded by a minimum and a maximum.

        Parameters
        ----------
        depth : int

        fathoms : int

        cables : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[float]
            Soundings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.soundings.list_soundings(
            depth=1,
            fathoms=1,
            cables=1,
        )
        """
        _response = self._raw_client.list_soundings(
            depth=depth, fathoms=fathoms, cables=cables, request_options=request_options
        )
        return _response.data

    def get_sounding_log(
        self, *, depth: int, fathoms: int, cables: int, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Bounded integers on an operation answering text.

        Parameters
        ----------
        depth : int

        fathoms : int

        cables : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The log

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.soundings.get_sounding_log(
            depth=1024,
            fathoms=40,
            cables=5,
        )
        """
        _response = self._raw_client.get_sounding_log(
            depth=depth, fathoms=fathoms, cables=cables, request_options=request_options
        )
        return _response.data


class AsyncSoundingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSoundingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSoundingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSoundingsClient
        """
        return self._raw_client

    async def list_soundings(
        self, *, depth: int, fathoms: int, cables: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[float]:
        """
        An integer bounded by a minimum and a maximum.

        Parameters
        ----------
        depth : int

        fathoms : int

        cables : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[float]
            Soundings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.soundings.list_soundings(
                depth=1,
                fathoms=1,
                cables=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_soundings(
            depth=depth, fathoms=fathoms, cables=cables, request_options=request_options
        )
        return _response.data

    async def get_sounding_log(
        self, *, depth: int, fathoms: int, cables: int, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Bounded integers on an operation answering text.

        Parameters
        ----------
        depth : int

        fathoms : int

        cables : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The log

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.soundings.get_sounding_log(
                depth=1024,
                fathoms=40,
                cables=5,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sounding_log(
            depth=depth, fathoms=fathoms, cables=cables, request_options=request_options
        )
        return _response.data
