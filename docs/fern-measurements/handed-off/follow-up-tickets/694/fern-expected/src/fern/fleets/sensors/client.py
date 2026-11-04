

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawSensorsClient, RawSensorsClient
from .types.create_sensors_request import CreateSensorsRequest


OMIT = typing.cast(typing.Any, ...)


class SensorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSensorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSensorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSensorsClient
        """
        return self._raw_client

    def create(self, *, request: CreateSensorsRequest, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : CreateSensorsRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.fleets.sensors import FixedSensor

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.fleets.sensors.create(
            request=FixedSensor(),
        )
        """
        _response = self._raw_client.create(request=request, request_options=request_options)
        return _response.data


class AsyncSensorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSensorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSensorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSensorsClient
        """
        return self._raw_client

    async def create(
        self, *, request: CreateSensorsRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : CreateSensorsRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.fleets.sensors import FixedSensor

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.fleets.sensors.create(
                request=FixedSensor(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(request=request, request_options=request_options)
        return _response.data
