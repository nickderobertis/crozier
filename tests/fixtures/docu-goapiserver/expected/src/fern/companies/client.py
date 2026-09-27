

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.company import Company
from ..types.company_settings import CompanySettings
from .raw_client import AsyncRawCompaniesClient, RawCompaniesClient


class CompaniesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCompaniesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCompaniesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCompaniesClient
        """
        return self._raw_client

    def get_companies_id_settings_v3(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CompanySettings:
        """
        The path ID is the EMS company UUID. It must match the session company when the session has one. Returns 404 when the company or its settings are absent.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompanySettings
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.companies.get_companies_id_settings_v3(
            id="id",
        )
        """
        _response = self._raw_client.get_companies_id_settings_v3(id, request_options=request_options)
        return _response.data

    def get_companies_id_v3(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Company:
        """
        The path ID is the EMS company UUID. It must match the session company when the session has one. Returns 404 when the company or its settings are absent.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Company
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.companies.get_companies_id_v3(
            id="id",
        )
        """
        _response = self._raw_client.get_companies_id_v3(id, request_options=request_options)
        return _response.data


class AsyncCompaniesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCompaniesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCompaniesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCompaniesClient
        """
        return self._raw_client

    async def get_companies_id_settings_v3(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CompanySettings:
        """
        The path ID is the EMS company UUID. It must match the session company when the session has one. Returns 404 when the company or its settings are absent.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompanySettings
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.companies.get_companies_id_settings_v3(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_companies_id_settings_v3(id, request_options=request_options)
        return _response.data

    async def get_companies_id_v3(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Company:
        """
        The path ID is the EMS company UUID. It must match the session company when the session has one. Returns 404 when the company or its settings are absent.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Company
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.companies.get_companies_id_v3(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_companies_id_v3(id, request_options=request_options)
        return _response.data
