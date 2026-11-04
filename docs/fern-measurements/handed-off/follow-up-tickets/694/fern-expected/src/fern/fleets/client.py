

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFleetsClient, RawFleetsClient
from .types.create_fleets_request_sensors_item import CreateFleetsRequestSensorsItem

if typing.TYPE_CHECKING:
    from .sensors.client import AsyncSensorsClient, SensorsClient

OMIT = typing.cast(typing.Any, ...)


class FleetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFleetsClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._sensors: typing.Optional[SensorsClient] = None

    @property
    def with_raw_response(self) -> RawFleetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFleetsClient
        """
        return self._raw_client

    def create(
        self,
        *,
        sensors: typing.Optional[typing.Sequence[CreateFleetsRequestSensorsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        sensors : typing.Optional[typing.Sequence[CreateFleetsRequestSensorsItem]]

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
        client.fleets.create()
        """
        _response = self._raw_client.create(sensors=sensors, request_options=request_options)
        return _response.data

    @property
    def sensors(self):
        if self._sensors is None:
            from .sensors.client import SensorsClient

            self._sensors = SensorsClient(client_wrapper=self._client_wrapper)
        return self._sensors


class AsyncFleetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFleetsClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._sensors: typing.Optional[AsyncSensorsClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFleetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFleetsClient
        """
        return self._raw_client

    async def create(
        self,
        *,
        sensors: typing.Optional[typing.Sequence[CreateFleetsRequestSensorsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        sensors : typing.Optional[typing.Sequence[CreateFleetsRequestSensorsItem]]

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
            await client.fleets.create()


        asyncio.run(main())
        """
        _response = await self._raw_client.create(sensors=sensors, request_options=request_options)
        return _response.data

    @property
    def sensors(self):
        if self._sensors is None:
            from .sensors.client import AsyncSensorsClient

            self._sensors = AsyncSensorsClient(client_wrapper=self._client_wrapper)
        return self._sensors
