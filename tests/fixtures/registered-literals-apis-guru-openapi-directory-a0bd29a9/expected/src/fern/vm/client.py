

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.user_identity import UserIdentity
from ..types.vm_result import VmResult
from .raw_client import AsyncRawVmClient, RawVmClient


OMIT = typing.cast(typing.Any, ...)


class VmClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVmClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVmClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVmClient
        """
        return self._raw_client

    def get_api_v1tenant_tenant_id_pool_pool_name_vm(
        self, tenant_id: str, pool_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[VmResult]:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[VmResult]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vm.get_api_v1tenant_tenant_id_pool_pool_name_vm(
            tenant_id="tenantId",
            pool_name="poolName",
        )
        """
        _response = self._raw_client.get_api_v1tenant_tenant_id_pool_pool_name_vm(
            tenant_id, pool_name, request_options=request_options
        )
        return _response.data

    def get_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
        self, tenant_id: str, pool_name: str, vm_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VmResult:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        vm_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vm.get_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
            tenant_id="tenantId",
            pool_name="poolName",
            vm_name="vmName",
        )
        """
        _response = self._raw_client.get_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
            tenant_id, pool_name, vm_name, request_options=request_options
        )
        return _response.data

    def put_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
        self,
        tenant_id: str,
        pool_name: str,
        vm_name: str,
        *,
        user: UserIdentity,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VmResult:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        vm_name : str

        user : UserIdentity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmResult
            Success

        Examples
        --------
        from fern import FernApi, UserIdentity

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vm.put_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
            tenant_id="tenantId",
            pool_name="poolName",
            vm_name="vmName",
            user=UserIdentity(
                user_principal_name="userPrincipalName",
            ),
        )
        """
        _response = self._raw_client.put_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
            tenant_id, pool_name, vm_name, user=user, request_options=request_options
        )
        return _response.data

    def delete_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
        self, tenant_id: str, pool_name: str, vm_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        vm_name : str

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
        client.vm.delete_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
            tenant_id="tenantId",
            pool_name="poolName",
            vm_name="vmName",
        )
        """
        _response = self._raw_client.delete_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
            tenant_id, pool_name, vm_name, request_options=request_options
        )
        return _response.data

    def post_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name_start(
        self, tenant_id: str, pool_name: str, vm_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        vm_name : str

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
        client.vm.post_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name_start(
            tenant_id="tenantId",
            pool_name="poolName",
            vm_name="vmName",
        )
        """
        _response = self._raw_client.post_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name_start(
            tenant_id, pool_name, vm_name, request_options=request_options
        )
        return _response.data

    def post_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name_stop(
        self, tenant_id: str, pool_name: str, vm_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        vm_name : str

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
        client.vm.post_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name_stop(
            tenant_id="tenantId",
            pool_name="poolName",
            vm_name="vmName",
        )
        """
        _response = self._raw_client.post_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name_stop(
            tenant_id, pool_name, vm_name, request_options=request_options
        )
        return _response.data


class AsyncVmClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVmClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVmClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVmClient
        """
        return self._raw_client

    async def get_api_v1tenant_tenant_id_pool_pool_name_vm(
        self, tenant_id: str, pool_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[VmResult]:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[VmResult]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vm.get_api_v1tenant_tenant_id_pool_pool_name_vm(
                tenant_id="tenantId",
                pool_name="poolName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1tenant_tenant_id_pool_pool_name_vm(
            tenant_id, pool_name, request_options=request_options
        )
        return _response.data

    async def get_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
        self, tenant_id: str, pool_name: str, vm_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VmResult:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        vm_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vm.get_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
                tenant_id="tenantId",
                pool_name="poolName",
                vm_name="vmName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
            tenant_id, pool_name, vm_name, request_options=request_options
        )
        return _response.data

    async def put_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
        self,
        tenant_id: str,
        pool_name: str,
        vm_name: str,
        *,
        user: UserIdentity,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VmResult:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        vm_name : str

        user : UserIdentity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UserIdentity

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vm.put_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
                tenant_id="tenantId",
                pool_name="poolName",
                vm_name="vmName",
                user=UserIdentity(
                    user_principal_name="userPrincipalName",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
            tenant_id, pool_name, vm_name, user=user, request_options=request_options
        )
        return _response.data

    async def delete_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
        self, tenant_id: str, pool_name: str, vm_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        vm_name : str

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
            await client.vm.delete_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
                tenant_id="tenantId",
                pool_name="poolName",
                vm_name="vmName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name(
            tenant_id, pool_name, vm_name, request_options=request_options
        )
        return _response.data

    async def post_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name_start(
        self, tenant_id: str, pool_name: str, vm_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        vm_name : str

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
            await client.vm.post_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name_start(
                tenant_id="tenantId",
                pool_name="poolName",
                vm_name="vmName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name_start(
            tenant_id, pool_name, vm_name, request_options=request_options
        )
        return _response.data

    async def post_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name_stop(
        self, tenant_id: str, pool_name: str, vm_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        pool_name : str

        vm_name : str

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
            await client.vm.post_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name_stop(
                tenant_id="tenantId",
                pool_name="poolName",
                vm_name="vmName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1tenant_tenant_id_pool_pool_name_vm_vm_name_stop(
            tenant_id, pool_name, vm_name, request_options=request_options
        )
        return _response.data
