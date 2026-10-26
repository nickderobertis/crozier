

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.channels import Channels
from ..types.gap import Gap
from ..types.lull import Lull
from ..types.pitch import Pitch
from ..types.reading import Reading
from ..types.reading_mode import ReadingMode
from ..types.silence import Silence
from ..types.stillness import Stillness
from ..types.tone import Tone
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

    def get_silence(
        self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Silence]:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Silence]
            The sensor's silence marker.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sensors.get_silence(
            sensor_id="sensorId",
        )
        """
        _response = self._raw_client.get_silence(sensor_id, request_options=request_options)
        return _response.data

    def get_gap(
        self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Gap]:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Gap]
            The sensor's gap marker.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sensors.get_gap(
            sensor_id="sensorId",
        )
        """
        _response = self._raw_client.get_gap(sensor_id, request_options=request_options)
        return _response.data

    def put_reading(
        self,
        sensor_id: str,
        *,
        label: str,
        silence: typing.Optional[Silence] = OMIT,
        lull: typing.Optional[Lull] = OMIT,
        hush: typing.Optional[typing.Sequence[typing.Optional[typing.Any]]] = OMIT,
        stillness: typing.Optional[Stillness] = OMIT,
        void: typing.Optional[typing.Any] = OMIT,
        pitch: typing.Optional[Pitch] = OMIT,
        tone: typing.Optional[Tone] = OMIT,
        mode: typing.Optional[ReadingMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Reading:
        """
        Parameters
        ----------
        sensor_id : str

        label : str

        silence : typing.Optional[Silence]

        lull : typing.Optional[Lull]

        hush : typing.Optional[typing.Sequence[typing.Optional[typing.Any]]]

        stillness : typing.Optional[Stillness]

        void : typing.Optional[typing.Any]

        pitch : typing.Optional[Pitch]

        tone : typing.Optional[Tone]

        mode : typing.Optional[ReadingMode]
            Whether the sensor is sampling.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Reading
            The stored reading.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sensors.put_reading(
            sensor_id="sensorId",
            label="label",
        )
        """
        _response = self._raw_client.put_reading(
            sensor_id,
            label=label,
            silence=silence,
            lull=lull,
            hush=hush,
            stillness=stillness,
            void=void,
            pitch=pitch,
            tone=tone,
            mode=mode,
            request_options=request_options,
        )
        return _response.data

    def put_channel(
        self, sensor_id: str, *, request: Channels, request_options: typing.Optional[RequestOptions] = None
    ) -> Channels:
        """
        Parameters
        ----------
        sensor_id : str

        request : Channels

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Channels
            The channel the sensor now listens on.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sensors.put_channel(
            sensor_id="sensorId",
            request="south",
        )
        """
        _response = self._raw_client.put_channel(sensor_id, request=request, request_options=request_options)
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

    async def get_silence(
        self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Silence]:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Silence]
            The sensor's silence marker.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sensors.get_silence(
                sensor_id="sensorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_silence(sensor_id, request_options=request_options)
        return _response.data

    async def get_gap(
        self, sensor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[Gap]:
        """
        Parameters
        ----------
        sensor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[Gap]
            The sensor's gap marker.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sensors.get_gap(
                sensor_id="sensorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_gap(sensor_id, request_options=request_options)
        return _response.data

    async def put_reading(
        self,
        sensor_id: str,
        *,
        label: str,
        silence: typing.Optional[Silence] = OMIT,
        lull: typing.Optional[Lull] = OMIT,
        hush: typing.Optional[typing.Sequence[typing.Optional[typing.Any]]] = OMIT,
        stillness: typing.Optional[Stillness] = OMIT,
        void: typing.Optional[typing.Any] = OMIT,
        pitch: typing.Optional[Pitch] = OMIT,
        tone: typing.Optional[Tone] = OMIT,
        mode: typing.Optional[ReadingMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Reading:
        """
        Parameters
        ----------
        sensor_id : str

        label : str

        silence : typing.Optional[Silence]

        lull : typing.Optional[Lull]

        hush : typing.Optional[typing.Sequence[typing.Optional[typing.Any]]]

        stillness : typing.Optional[Stillness]

        void : typing.Optional[typing.Any]

        pitch : typing.Optional[Pitch]

        tone : typing.Optional[Tone]

        mode : typing.Optional[ReadingMode]
            Whether the sensor is sampling.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Reading
            The stored reading.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sensors.put_reading(
                sensor_id="sensorId",
                label="label",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_reading(
            sensor_id,
            label=label,
            silence=silence,
            lull=lull,
            hush=hush,
            stillness=stillness,
            void=void,
            pitch=pitch,
            tone=tone,
            mode=mode,
            request_options=request_options,
        )
        return _response.data

    async def put_channel(
        self, sensor_id: str, *, request: Channels, request_options: typing.Optional[RequestOptions] = None
    ) -> Channels:
        """
        Parameters
        ----------
        sensor_id : str

        request : Channels

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Channels
            The channel the sensor now listens on.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sensors.put_channel(
                sensor_id="sensorId",
                request="south",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_channel(sensor_id, request=request, request_options=request_options)
        return _response.data
