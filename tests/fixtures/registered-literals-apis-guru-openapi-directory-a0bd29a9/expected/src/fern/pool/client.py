

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.domain_user_credentials import DomainUserCredentials
from ..types.hot_pool_settings import HotPoolSettings
from ..types.pool_result import PoolResult
from ..types.vm_specs import VmSpecs
from .raw_client import AsyncRawPoolClient, RawPoolClient


OMIT = typing.cast(typing.Any, ...)


class PoolClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPoolClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPoolClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPoolClient
        """
        return self._raw_client

    def get_api_v1tenant_tenant_id_pool_pool_name(
        self, tenant_id: str, pool_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PoolResult:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PoolResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pool.get_api_v1tenant_tenant_id_pool_pool_name(
            tenant_id="tenantId",
            pool_name="poolName",
        )
        """
        _response = self._raw_client.get_api_v1tenant_tenant_id_pool_pool_name(
            tenant_id, pool_name, request_options=request_options
        )
        return _response.data

    def put_api_v1tenant_tenant_id_pool_pool_name(
        self,
        tenant_id: str,
        pool_name: str,
        *,
        pool_group_name: str,
        vm_specs: VmSpecs,
        domain_user_credentials: typing.Optional[DomainUserCredentials] = OMIT,
        hot_pool_settings: typing.Optional[HotPoolSettings] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        user_group_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PoolResult:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        pool_group_name : str

        vm_specs : VmSpecs

        domain_user_credentials : typing.Optional[DomainUserCredentials]

        hot_pool_settings : typing.Optional[HotPoolSettings]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        user_group_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PoolResult
            Success

        Examples
        --------
        from fern import FernApi, VmSpecs

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pool.put_api_v1tenant_tenant_id_pool_pool_name(
            tenant_id="tenantId",
            pool_name="poolName",
            pool_group_name="poolGroupName",
            vm_specs=VmSpecs(
                disk_type=1,
                image_resource_id="imageResourceId",
                size="size",
                subnet_resource_id="subnetResourceId",
            ),
        )
        """
        _response = self._raw_client.put_api_v1tenant_tenant_id_pool_pool_name(
            tenant_id,
            pool_name,
            pool_group_name=pool_group_name,
            vm_specs=vm_specs,
            domain_user_credentials=domain_user_credentials,
            hot_pool_settings=hot_pool_settings,
            tags=tags,
            user_group_name=user_group_name,
            request_options=request_options,
        )
        return _response.data

    def delete_api_v1tenant_tenant_id_pool_pool_name(
        self, tenant_id: str, pool_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

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
        client.pool.delete_api_v1tenant_tenant_id_pool_pool_name(
            tenant_id="tenantId",
            pool_name="poolName",
        )
        """
        _response = self._raw_client.delete_api_v1tenant_tenant_id_pool_pool_name(
            tenant_id, pool_name, request_options=request_options
        )
        return _response.data

    def patch_api_v1tenant_tenant_id_pool_pool_name(
        self,
        tenant_id: str,
        pool_name: str,
        *,
        pool_group_name: str,
        vm_specs: VmSpecs,
        domain_user_credentials: typing.Optional[DomainUserCredentials] = OMIT,
        hot_pool_settings: typing.Optional[HotPoolSettings] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        user_group_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PoolResult:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        pool_group_name : str

        vm_specs : VmSpecs

        domain_user_credentials : typing.Optional[DomainUserCredentials]

        hot_pool_settings : typing.Optional[HotPoolSettings]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        user_group_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PoolResult
            Success

        Examples
        --------
        from fern import FernApi, VmSpecs

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pool.patch_api_v1tenant_tenant_id_pool_pool_name(
            tenant_id="tenantId",
            pool_name="poolName",
            pool_group_name="poolGroupName",
            vm_specs=VmSpecs(
                disk_type=1,
                image_resource_id="imageResourceId",
                size="size",
                subnet_resource_id="subnetResourceId",
            ),
        )
        """
        _response = self._raw_client.patch_api_v1tenant_tenant_id_pool_pool_name(
            tenant_id,
            pool_name,
            pool_group_name=pool_group_name,
            vm_specs=vm_specs,
            domain_user_credentials=domain_user_credentials,
            hot_pool_settings=hot_pool_settings,
            tags=tags,
            user_group_name=user_group_name,
            request_options=request_options,
        )
        return _response.data


class AsyncPoolClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPoolClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPoolClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPoolClient
        """
        return self._raw_client

    async def get_api_v1tenant_tenant_id_pool_pool_name(
        self, tenant_id: str, pool_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PoolResult:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PoolResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pool.get_api_v1tenant_tenant_id_pool_pool_name(
                tenant_id="tenantId",
                pool_name="poolName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1tenant_tenant_id_pool_pool_name(
            tenant_id, pool_name, request_options=request_options
        )
        return _response.data

    async def put_api_v1tenant_tenant_id_pool_pool_name(
        self,
        tenant_id: str,
        pool_name: str,
        *,
        pool_group_name: str,
        vm_specs: VmSpecs,
        domain_user_credentials: typing.Optional[DomainUserCredentials] = OMIT,
        hot_pool_settings: typing.Optional[HotPoolSettings] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        user_group_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PoolResult:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        pool_group_name : str

        vm_specs : VmSpecs

        domain_user_credentials : typing.Optional[DomainUserCredentials]

        hot_pool_settings : typing.Optional[HotPoolSettings]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        user_group_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PoolResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, VmSpecs

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pool.put_api_v1tenant_tenant_id_pool_pool_name(
                tenant_id="tenantId",
                pool_name="poolName",
                pool_group_name="poolGroupName",
                vm_specs=VmSpecs(
                    disk_type=1,
                    image_resource_id="imageResourceId",
                    size="size",
                    subnet_resource_id="subnetResourceId",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1tenant_tenant_id_pool_pool_name(
            tenant_id,
            pool_name,
            pool_group_name=pool_group_name,
            vm_specs=vm_specs,
            domain_user_credentials=domain_user_credentials,
            hot_pool_settings=hot_pool_settings,
            tags=tags,
            user_group_name=user_group_name,
            request_options=request_options,
        )
        return _response.data

    async def delete_api_v1tenant_tenant_id_pool_pool_name(
        self, tenant_id: str, pool_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

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
            await client.pool.delete_api_v1tenant_tenant_id_pool_pool_name(
                tenant_id="tenantId",
                pool_name="poolName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_v1tenant_tenant_id_pool_pool_name(
            tenant_id, pool_name, request_options=request_options
        )
        return _response.data

    async def patch_api_v1tenant_tenant_id_pool_pool_name(
        self,
        tenant_id: str,
        pool_name: str,
        *,
        pool_group_name: str,
        vm_specs: VmSpecs,
        domain_user_credentials: typing.Optional[DomainUserCredentials] = OMIT,
        hot_pool_settings: typing.Optional[HotPoolSettings] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        user_group_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PoolResult:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        pool_group_name : str

        vm_specs : VmSpecs

        domain_user_credentials : typing.Optional[DomainUserCredentials]

        hot_pool_settings : typing.Optional[HotPoolSettings]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        user_group_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PoolResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, VmSpecs

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pool.patch_api_v1tenant_tenant_id_pool_pool_name(
                tenant_id="tenantId",
                pool_name="poolName",
                pool_group_name="poolGroupName",
                vm_specs=VmSpecs(
                    disk_type=1,
                    image_resource_id="imageResourceId",
                    size="size",
                    subnet_resource_id="subnetResourceId",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_api_v1tenant_tenant_id_pool_pool_name(
            tenant_id,
            pool_name,
            pool_group_name=pool_group_name,
            vm_specs=vm_specs,
            domain_user_credentials=domain_user_credentials,
            hot_pool_settings=hot_pool_settings,
            tags=tags,
            user_group_name=user_group_name,
            request_options=request_options,
        )
        return _response.data
