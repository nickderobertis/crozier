

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.complex_ import Complex
from ..types.range import Range
from .raw_client import AsyncRawSweepsClient, RawSweepsClient


OMIT = typing.cast(typing.Any, ...)


class SweepsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSweepsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSweepsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSweepsClient
        """
        return self._raw_client

    def complex_(
        self,
        sweep_id: str,
        *,
        frequency: float,
        complex_: typing.Optional[bool] = None,
        complex_request_complex: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Complex:
        """
        Parameters
        ----------
        sweep_id : str

        frequency : float
            Sweep frequency in hertz.

        complex_ : typing.Optional[bool]
            Report the point in rectangular rather than polar form.

        complex_request_complex : typing.Optional[bool]
            Return the conjugate as well.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Complex
            The resolved point.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sweeps.complex_(
            sweep_id="sweepId",
            frequency=1.1,
        )
        """
        _response = self._raw_client.complex_(
            sweep_id,
            frequency=frequency,
            complex_=complex_,
            complex_request_complex=complex_request_complex,
            request_options=request_options,
        )
        return _response.data

    def calibrate(
        self,
        *,
        complex_: typing.Optional[bool] = None,
        calibration_complex: typing.Optional[float] = OMIT,
        gain: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        complex_ : typing.Optional[bool]
            Apply the correction to the complex plane only.

        calibration_complex : typing.Optional[float]
            Phase correction, in degrees.

        gain : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sweeps.calibrate()
        """
        _response = self._raw_client.calibrate(
            complex_=complex_, calibration_complex=calibration_complex, gain=gain, request_options=request_options
        )
        return _response.data

    def get_range(self, sweep_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Range:
        """
        Parameters
        ----------
        sweep_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Range
            The frequency span the sweep covered.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.sweeps.get_range(
            sweep_id="sweepId",
        )
        """
        _response = self._raw_client.get_range(sweep_id, request_options=request_options)
        return _response.data


class AsyncSweepsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSweepsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSweepsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSweepsClient
        """
        return self._raw_client

    async def complex_(
        self,
        sweep_id: str,
        *,
        frequency: float,
        complex_: typing.Optional[bool] = None,
        complex_request_complex: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Complex:
        """
        Parameters
        ----------
        sweep_id : str

        frequency : float
            Sweep frequency in hertz.

        complex_ : typing.Optional[bool]
            Report the point in rectangular rather than polar form.

        complex_request_complex : typing.Optional[bool]
            Return the conjugate as well.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Complex
            The resolved point.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sweeps.complex_(
                sweep_id="sweepId",
                frequency=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complex_(
            sweep_id,
            frequency=frequency,
            complex_=complex_,
            complex_request_complex=complex_request_complex,
            request_options=request_options,
        )
        return _response.data

    async def calibrate(
        self,
        *,
        complex_: typing.Optional[bool] = None,
        calibration_complex: typing.Optional[float] = OMIT,
        gain: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        complex_ : typing.Optional[bool]
            Apply the correction to the complex plane only.

        calibration_complex : typing.Optional[float]
            Phase correction, in degrees.

        gain : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sweeps.calibrate()


        asyncio.run(main())
        """
        _response = await self._raw_client.calibrate(
            complex_=complex_, calibration_complex=calibration_complex, gain=gain, request_options=request_options
        )
        return _response.data

    async def get_range(self, sweep_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Range:
        """
        Parameters
        ----------
        sweep_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Range
            The frequency span the sweep covered.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.sweeps.get_range(
                sweep_id="sweepId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_range(sweep_id, request_options=request_options)
        return _response.data
