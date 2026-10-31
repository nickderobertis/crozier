

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.curve import Curve
from .raw_client import AsyncRawCurvesClient, RawCurvesClient


OMIT = typing.cast(typing.Any, ...)


class CurvesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCurvesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCurvesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCurvesClient
        """
        return self._raw_client

    def record_curve(
        self,
        *,
        tolerance: float,
        glaze: float,
        readings: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Curve:
        """
        Parameters
        ----------
        tolerance : float

        glaze : float

        readings : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Curve
            The curve was recorded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.curves.record_curve(
            tolerance=0.9584673068551939,
            glaze=0.9921600467158583,
            readings=[
                ["kiln-east-b", "2026-03-01", 0.24200106749781558, 0.36454792138880565],
                [
                    "kiln-north-a",
                    "2026-03-01",
                    0.24200106749781558,
                    0.36454792138880565,
                ],
                ["kiln-east-b", "2026-03-02", 0.38480342994262373, 0.46566309815988427],
            ],
        )
        """
        _response = self._raw_client.record_curve(
            tolerance=tolerance, glaze=glaze, readings=readings, request_options=request_options
        )
        return _response.data


class AsyncCurvesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCurvesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCurvesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCurvesClient
        """
        return self._raw_client

    async def record_curve(
        self,
        *,
        tolerance: float,
        glaze: float,
        readings: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Curve:
        """
        Parameters
        ----------
        tolerance : float

        glaze : float

        readings : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Curve
            The curve was recorded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.curves.record_curve(
                tolerance=0.9584673068551939,
                glaze=0.9921600467158583,
                readings=[
                    [
                        "kiln-east-b",
                        "2026-03-01",
                        0.24200106749781558,
                        0.36454792138880565,
                    ],
                    [
                        "kiln-north-a",
                        "2026-03-01",
                        0.24200106749781558,
                        0.36454792138880565,
                    ],
                    [
                        "kiln-east-b",
                        "2026-03-02",
                        0.38480342994262373,
                        0.46566309815988427,
                    ],
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_curve(
            tolerance=tolerance, glaze=glaze, readings=readings, request_options=request_options
        )
        return _response.data
