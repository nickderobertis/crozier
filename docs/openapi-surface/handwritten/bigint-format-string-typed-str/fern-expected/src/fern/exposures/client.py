

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.exposure import Exposure
from .raw_client import AsyncRawExposuresClient, RawExposuresClient


class ExposuresClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExposuresClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExposuresClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExposuresClient
        """
        return self._raw_client

    def fetch_exposure(self, exposure_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Exposure:
        """
        Parameters
        ----------
        exposure_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Exposure
            One exposure and its photon tally.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.exposures.fetch_exposure(
            exposure_id="exposureId",
        )
        """
        _response = self._raw_client.fetch_exposure(exposure_id, request_options=request_options)
        return _response.data


class AsyncExposuresClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExposuresClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExposuresClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExposuresClient
        """
        return self._raw_client

    async def fetch_exposure(
        self, exposure_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Exposure:
        """
        Parameters
        ----------
        exposure_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Exposure
            One exposure and its photon tally.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.exposures.fetch_exposure(
                exposure_id="exposureId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_exposure(exposure_id, request_options=request_options)
        return _response.data
