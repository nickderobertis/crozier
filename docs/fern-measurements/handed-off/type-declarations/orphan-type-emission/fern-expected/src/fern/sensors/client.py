

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSensorsClient, RawSensorsClient


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

    def register_sensor(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        name : str

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
        client.sensors.register_sensor(
            name="name",
        )
        """
        _response = self._raw_client.register_sensor(name=name, request_options=request_options)
        return _response.data

    def addnote(
        self,
        sensor_id: str,
        *,
        text: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        sensor_id : str

        text : typing.Optional[str]

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
        client.sensors.addnote(
            sensor_id="sensorId",
        )
        """
        _response = self._raw_client.addnote(sensor_id, text=text, request_options=request_options)
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

    async def register_sensor(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        name : str

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
            await client.sensors.register_sensor(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_sensor(name=name, request_options=request_options)
        return _response.data

    async def addnote(
        self,
        sensor_id: str,
        *,
        text: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        sensor_id : str

        text : typing.Optional[str]

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
            await client.sensors.addnote(
                sensor_id="sensorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.addnote(sensor_id, text=text, request_options=request_options)
        return _response.data
