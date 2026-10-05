

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.observatory import Observatory
from ..types.observatory_instruments_item import ObservatoryInstrumentsItem
from .raw_client import AsyncRawObservatoriesClient, RawObservatoriesClient


OMIT = typing.cast(typing.Any, ...)


class ObservatoriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawObservatoriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawObservatoriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawObservatoriesClient
        """
        return self._raw_client

    def register_observatory(
        self,
        *,
        site: str,
        instruments: typing.Optional[typing.Sequence[ObservatoryInstrumentsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Observatory:
        """
        Parameters
        ----------
        site : str

        instruments : typing.Optional[typing.Sequence[ObservatoryInstrumentsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Observatory
            The registered observatory.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.observatories.register_observatory(
            site="site",
        )
        """
        _response = self._raw_client.register_observatory(
            site=site, instruments=instruments, request_options=request_options
        )
        return _response.data


class AsyncObservatoriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawObservatoriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawObservatoriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawObservatoriesClient
        """
        return self._raw_client

    async def register_observatory(
        self,
        *,
        site: str,
        instruments: typing.Optional[typing.Sequence[ObservatoryInstrumentsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Observatory:
        """
        Parameters
        ----------
        site : str

        instruments : typing.Optional[typing.Sequence[ObservatoryInstrumentsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Observatory
            The registered observatory.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.observatories.register_observatory(
                site="site",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_observatory(
            site=site, instruments=instruments, request_options=request_options
        )
        return _response.data
