

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.municipality_feature_collection import MunicipalityFeatureCollection
from .raw_client import AsyncRawMunicipalitiesV2Client, RawMunicipalitiesV2Client


class MunicipalitiesV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMunicipalitiesV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMunicipalitiesV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMunicipalitiesV2Client
        """
        return self._raw_client

    def get_municipalities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MunicipalityFeatureCollection:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MunicipalityFeatureCollection
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.municipalities_v2.get_municipalities()
        """
        _response = self._raw_client.get_municipalities(request_options=request_options)
        return _response.data


class AsyncMunicipalitiesV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMunicipalitiesV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMunicipalitiesV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMunicipalitiesV2Client
        """
        return self._raw_client

    async def get_municipalities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MunicipalityFeatureCollection:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MunicipalityFeatureCollection
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.municipalities_v2.get_municipalities()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_municipalities(request_options=request_options)
        return _response.data
