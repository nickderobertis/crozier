

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTenantObsoleteClient, RawTenantObsoleteClient


class TenantObsoleteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTenantObsoleteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTenantObsoleteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTenantObsoleteClient
        """
        return self._raw_client

    def tenant_sdpath(self, *, datapartition: str, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        <ul><li>Return the seistore path to a tenant associated with the data partition.</li><li>Required roles: none</li></ul>

        Parameters
        ----------
        datapartition : str
            Datapartition of the tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Seismic store path to the tenant retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenant_obsolete.tenant_sdpath(
            datapartition="datapartition",
        )
        """
        _response = self._raw_client.tenant_sdpath(datapartition=datapartition, request_options=request_options)
        return _response.data


class AsyncTenantObsoleteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTenantObsoleteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTenantObsoleteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTenantObsoleteClient
        """
        return self._raw_client

    async def tenant_sdpath(
        self, *, datapartition: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        <ul><li>Return the seistore path to a tenant associated with the data partition.</li><li>Required roles: none</li></ul>

        Parameters
        ----------
        datapartition : str
            Datapartition of the tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Seismic store path to the tenant retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenant_obsolete.tenant_sdpath(
                datapartition="datapartition",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tenant_sdpath(datapartition=datapartition, request_options=request_options)
        return _response.data
