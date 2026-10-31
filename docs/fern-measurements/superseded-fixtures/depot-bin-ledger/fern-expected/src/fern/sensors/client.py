

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSensorsClient, RawSensorsClient


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

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Sensor ids.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sensors.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def float_(self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> float:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Level, from 0 to 1.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sensors.float_(
            sensor_id="sensorId",
        )
        """
        _response = self._raw_client.float_(sensor_id, request_options=request_options)
        return _response.data

    def bool_(self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            True when closed.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sensors.bool_(
            sensor_id="sensorId",
        )
        """
        _response = self._raw_client.bool_(sensor_id, request_options=request_options)
        return _response.data

    def int_(self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Lifts since the last service.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sensors.int_(
            sensor_id="sensorId",
        )
        """
        _response = self._raw_client.int_(sensor_id, request_options=request_options)
        return _response.data

    def long_(self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Lifetime lifts.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sensors.long_(
            sensor_id="sensorId",
        )
        """
        _response = self._raw_client.long_(sensor_id, request_options=request_options)
        return _response.data

    def uuid_(self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The sensor's hardware id.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sensors.uuid_(
            sensor_id="sensorId",
        )
        """
        _response = self._raw_client.uuid_(sensor_id, request_options=request_options)
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

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Sensor ids.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sensors.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def float_(self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> float:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Level, from 0 to 1.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sensors.float_(
                sensor_id="sensorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.float_(sensor_id, request_options=request_options)
        return _response.data

    async def bool_(self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            True when closed.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sensors.bool_(
                sensor_id="sensorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bool_(sensor_id, request_options=request_options)
        return _response.data

    async def int_(self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Lifts since the last service.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sensors.int_(
                sensor_id="sensorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.int_(sensor_id, request_options=request_options)
        return _response.data

    async def long_(self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Lifetime lifts.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sensors.long_(
                sensor_id="sensorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.long_(sensor_id, request_options=request_options)
        return _response.data

    async def uuid_(self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The sensor's hardware id.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sensors.uuid_(
                sensor_id="sensorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.uuid_(sensor_id, request_options=request_options)
        return _response.data
