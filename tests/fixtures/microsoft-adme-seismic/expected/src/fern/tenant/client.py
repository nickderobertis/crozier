

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tenant import Tenant
from .raw_client import AsyncRawTenantClient, RawTenantClient


OMIT = typing.cast(typing.Any, ...)


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

    def get(self, tenantid: str, *, request_options: typing.Optional[RequestOptions] = None) -> Tenant:
        """
        <ul><li>Return the tenant metadata.</li><li>Required roles: seistore.system.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tenant
            Retrieved subproject metadata successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenant.get(
            tenantid="tenantid",
        )
        """
        _response = self._raw_client.get(tenantid, request_options=request_options)
        return _response.data

    def create(
        self,
        tenantid: str,
        *,
        gcpid: str,
        esd: str,
        default_acls: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tenant:
        """
        <ul><li>Register a data partition in seismic-dms.</li><li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        gcpid : str
            Google cloud project id associated with the tenant. For other providers, name of the data partition.

        esd : str
            Entitlements group Sub Domain (ESD). For instance, if the entitlements group is users.datalake.viewers@{datapartition}.{domain}.com, the esd value is {datapartition}.{domain}.com. It must start with the name of the data partition.

        default_acls : str
            Entitlements authorization group to manage tenant administrators.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tenant
            Creation of the tenant was successful.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenant.create(
            tenantid="tenantid",
            gcpid="datapartition",
            esd="{datapartition}.{domain}.com",
            default_acls="users.datalake.admins@{datapartition}.{domain}.com",
        )
        """
        _response = self._raw_client.create(
            tenantid, gcpid=gcpid, esd=esd, default_acls=default_acls, request_options=request_options
        )
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

    async def get(self, tenantid: str, *, request_options: typing.Optional[RequestOptions] = None) -> Tenant:
        """
        <ul><li>Return the tenant metadata.</li><li>Required roles: seistore.system.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tenant
            Retrieved subproject metadata successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenant.get(
                tenantid="tenantid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(tenantid, request_options=request_options)
        return _response.data

    async def create(
        self,
        tenantid: str,
        *,
        gcpid: str,
        esd: str,
        default_acls: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tenant:
        """
        <ul><li>Register a data partition in seismic-dms.</li><li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        gcpid : str
            Google cloud project id associated with the tenant. For other providers, name of the data partition.

        esd : str
            Entitlements group Sub Domain (ESD). For instance, if the entitlements group is users.datalake.viewers@{datapartition}.{domain}.com, the esd value is {datapartition}.{domain}.com. It must start with the name of the data partition.

        default_acls : str
            Entitlements authorization group to manage tenant administrators.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tenant
            Creation of the tenant was successful.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenant.create(
                tenantid="tenantid",
                gcpid="datapartition",
                esd="{datapartition}.{domain}.com",
                default_acls="users.datalake.admins@{datapartition}.{domain}.com",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            tenantid, gcpid=gcpid, esd=esd, default_acls=default_acls, request_options=request_options
        )
        return _response.data
