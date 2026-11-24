

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.fit_summary import FitSummary
from .raw_client import AsyncRawFitsClient, RawFitsClient


class FitsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFitsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFitsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFitsClient
        """
        return self._raw_client

    def get_fit(self, fit_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> FitSummary:
        """
        Parameters
        ----------
        fit_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FitSummary
            The fit.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.fits.get_fit(
            fit_id="fit_id",
        )
        """
        _response = self._raw_client.get_fit(fit_id, request_options=request_options)
        return _response.data


class AsyncFitsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFitsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFitsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFitsClient
        """
        return self._raw_client

    async def get_fit(self, fit_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> FitSummary:
        """
        Parameters
        ----------
        fit_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FitSummary
            The fit.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.fits.get_fit(
                fit_id="fit_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fit(fit_id, request_options=request_options)
        return _response.data
