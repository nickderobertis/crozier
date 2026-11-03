

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCalibrationsClient, RawCalibrationsClient
from .types.record_calibration_response import RecordCalibrationResponse


OMIT = typing.cast(typing.Any, ...)


class CalibrationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCalibrationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCalibrationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCalibrationsClient
        """
        return self._raw_client

    def record_calibration(
        self, *, gain: float, offsets: typing.Sequence[float], request_options: typing.Optional[RequestOptions] = None
    ) -> RecordCalibrationResponse:
        """
        Parameters
        ----------
        gain : float

        offsets : typing.Sequence[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordCalibrationResponse
            Recorded

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.calibrations.record_calibration(
            gain=0.9345407030264767,
            offsets=[0.1234567890123456, 2.718281828459045],
        )
        """
        _response = self._raw_client.record_calibration(gain=gain, offsets=offsets, request_options=request_options)
        return _response.data


class AsyncCalibrationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCalibrationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCalibrationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCalibrationsClient
        """
        return self._raw_client

    async def record_calibration(
        self, *, gain: float, offsets: typing.Sequence[float], request_options: typing.Optional[RequestOptions] = None
    ) -> RecordCalibrationResponse:
        """
        Parameters
        ----------
        gain : float

        offsets : typing.Sequence[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordCalibrationResponse
            Recorded

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.calibrations.record_calibration(
                gain=0.9345407030264767,
                offsets=[0.1234567890123456, 2.718281828459045],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_calibration(
            gain=gain, offsets=offsets, request_options=request_options
        )
        return _response.data
