

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dealer_db_models_license import DealerDbModelsLicense
from .raw_client import AsyncRawLicensesClient, RawLicensesClient


class LicensesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLicensesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLicensesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLicensesClient
        """
        return self._raw_client

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DealerDbModelsLicense:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the license to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DealerDbModelsLicense
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.licenses.get(
            id="ID",
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data


class AsyncLicensesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLicensesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLicensesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLicensesClient
        """
        return self._raw_client

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DealerDbModelsLicense:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the license to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DealerDbModelsLicense
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.licenses.get(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(id, request_options=request_options)
        return _response.data
