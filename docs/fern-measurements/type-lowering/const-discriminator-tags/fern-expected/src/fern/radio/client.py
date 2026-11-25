

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.event import Event
from ..types.signal import Signal
from ..types.timeline import Timeline
from .raw_client import AsyncRawRadioClient, RawRadioClient


class RadioClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRadioClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRadioClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRadioClient
        """
        return self._raw_client

    def get_timeline(self, *, request_options: typing.Optional[RequestOptions] = None) -> Timeline:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Timeline
            The timeline.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.radio.get_timeline()
        """
        _response = self._raw_client.get_timeline(request_options=request_options)
        return _response.data

    def list_events(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Event]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Event]
            The events.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.radio.list_events()
        """
        _response = self._raw_client.list_events(request_options=request_options)
        return _response.data

    def list_signals(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Signal]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Signal]
            The signals.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.radio.list_signals()
        """
        _response = self._raw_client.list_signals(request_options=request_options)
        return _response.data


class AsyncRadioClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRadioClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRadioClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRadioClient
        """
        return self._raw_client

    async def get_timeline(self, *, request_options: typing.Optional[RequestOptions] = None) -> Timeline:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Timeline
            The timeline.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.radio.get_timeline()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_timeline(request_options=request_options)
        return _response.data

    async def list_events(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Event]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Event]
            The events.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.radio.list_events()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_events(request_options=request_options)
        return _response.data

    async def list_signals(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Signal]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Signal]
            The signals.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.radio.list_signals()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_signals(request_options=request_options)
        return _response.data
