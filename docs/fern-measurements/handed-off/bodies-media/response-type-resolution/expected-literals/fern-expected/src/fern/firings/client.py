

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFiringsClient, RawFiringsClient
from .types.get_firing_response import GetFiringResponse
from .types.get_schedule_response import GetScheduleResponse
from .types.get_state_response import GetStateResponse
from .types.start_firing_response import StartFiringResponse


class FiringsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFiringsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFiringsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFiringsClient
        """
        return self._raw_client

    def get_firing(
        self, kiln_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[GetFiringResponse]:
        """
        Parameters
        ----------
        kiln_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[GetFiringResponse]
            The current firing, or null when the kiln is cold.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.firings.get_firing(
            kiln_id="kilnId",
        )
        """
        _response = self._raw_client.get_firing(kiln_id, request_options=request_options)
        return _response.data

    def get_schedule(
        self, kiln_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[GetScheduleResponse]:
        """
        Parameters
        ----------
        kiln_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[GetScheduleResponse]
            The next booking, or null.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.firings.get_schedule(
            kiln_id="kilnId",
        )
        """
        _response = self._raw_client.get_schedule(kiln_id, request_options=request_options)
        return _response.data

    def start_firing(
        self, kiln_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StartFiringResponse:
        """
        Parameters
        ----------
        kiln_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StartFiringResponse
            Acknowledged.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.firings.start_firing(
            kiln_id="kilnId",
        )
        """
        _response = self._raw_client.start_firing(kiln_id, request_options=request_options)
        return _response.data

    def get_state(self, kiln_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetStateResponse:
        """
        Parameters
        ----------
        kiln_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStateResponse
            The kiln's state.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.firings.get_state(
            kiln_id="kilnId",
        )
        """
        _response = self._raw_client.get_state(kiln_id, request_options=request_options)
        return _response.data

    def stream_log(
        self, kiln_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[str]:
        """
        Parameters
        ----------
        kiln_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            One log line per event.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        response = client.firings.stream_log(
            kiln_id="kilnId",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.stream_log(kiln_id, request_options=request_options) as r:
            yield from r.data


class AsyncFiringsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFiringsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFiringsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFiringsClient
        """
        return self._raw_client

    async def get_firing(
        self, kiln_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[GetFiringResponse]:
        """
        Parameters
        ----------
        kiln_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[GetFiringResponse]
            The current firing, or null when the kiln is cold.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.firings.get_firing(
                kiln_id="kilnId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_firing(kiln_id, request_options=request_options)
        return _response.data

    async def get_schedule(
        self, kiln_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[GetScheduleResponse]:
        """
        Parameters
        ----------
        kiln_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[GetScheduleResponse]
            The next booking, or null.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.firings.get_schedule(
                kiln_id="kilnId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_schedule(kiln_id, request_options=request_options)
        return _response.data

    async def start_firing(
        self, kiln_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StartFiringResponse:
        """
        Parameters
        ----------
        kiln_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StartFiringResponse
            Acknowledged.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.firings.start_firing(
                kiln_id="kilnId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_firing(kiln_id, request_options=request_options)
        return _response.data

    async def get_state(
        self, kiln_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetStateResponse:
        """
        Parameters
        ----------
        kiln_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStateResponse
            The kiln's state.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.firings.get_state(
                kiln_id="kilnId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_state(kiln_id, request_options=request_options)
        return _response.data

    async def stream_log(
        self, kiln_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[str]:
        """
        Parameters
        ----------
        kiln_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            One log line per event.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            response = client.firings.stream_log(
                kiln_id="kilnId",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.stream_log(kiln_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
