

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tenant_info_result import TenantInfoResult
from .raw_client import AsyncRawTenantClient, RawTenantClient


class TenantClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTenantClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTenantClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTenantClient
        """
        return self._raw_client

    def get_api_v1tenant_tenant_id(
        self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TenantInfoResult:
        """
        Parameters
        ----------
        tenant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantInfoResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tenant.get_api_v1tenant_tenant_id(
            tenant_id="tenantId",
        )
        """
        _response = self._raw_client.get_api_v1tenant_tenant_id(tenant_id, request_options=request_options)
        return _response.data

    def put_api_v1tenant_tenant_id(
        self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tenant.put_api_v1tenant_tenant_id(
            tenant_id="tenantId",
        )
        """
        _response = self._raw_client.put_api_v1tenant_tenant_id(tenant_id, request_options=request_options)
        return _response.data

    def delete_api_v1tenant_tenant_id(
        self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tenant.delete_api_v1tenant_tenant_id(
            tenant_id="tenantId",
        )
        """
        _response = self._raw_client.delete_api_v1tenant_tenant_id(tenant_id, request_options=request_options)
        return _response.data


class AsyncTenantClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTenantClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTenantClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTenantClient
        """
        return self._raw_client

    async def get_api_v1tenant_tenant_id(
        self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TenantInfoResult:
        """
        Parameters
        ----------
        tenant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantInfoResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tenant.get_api_v1tenant_tenant_id(
                tenant_id="tenantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1tenant_tenant_id(tenant_id, request_options=request_options)
        return _response.data

    async def put_api_v1tenant_tenant_id(
        self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tenant.put_api_v1tenant_tenant_id(
                tenant_id="tenantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1tenant_tenant_id(tenant_id, request_options=request_options)
        return _response.data

    async def delete_api_v1tenant_tenant_id(
        self, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tenant.delete_api_v1tenant_tenant_id(
                tenant_id="tenantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_v1tenant_tenant_id(tenant_id, request_options=request_options)
        return _response.data
