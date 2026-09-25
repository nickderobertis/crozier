

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_company_response import GetCompanyResponse
from .raw_client import AsyncRawCompanyClient, RawCompanyClient


class CompanyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCompanyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCompanyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCompanyClient
        """
        return self._raw_client

    def get_company(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetCompanyResponse:
        """
        Returns company information for the authenticated company.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCompanyResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.company.get_company()
        """
        _response = self._raw_client.get_company(request_options=request_options)
        return _response.data


class AsyncCompanyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCompanyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCompanyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCompanyClient
        """
        return self._raw_client

    async def get_company(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetCompanyResponse:
        """
        Returns company information for the authenticated company.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCompanyResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.company.get_company()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_company(request_options=request_options)
        return _response.data
