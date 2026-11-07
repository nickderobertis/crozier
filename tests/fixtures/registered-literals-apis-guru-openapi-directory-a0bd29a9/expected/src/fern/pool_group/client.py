

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.azure_location import AzureLocation
from ..types.pool_group_result import PoolGroupResult
from .raw_client import AsyncRawPoolGroupClient, RawPoolGroupClient


OMIT = typing.cast(typing.Any, ...)


class PoolGroupClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPoolGroupClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPoolGroupClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPoolGroupClient
        """
        return self._raw_client

    def get_api_v1tenant_tenant_id_pool_group_pool_group_name(
        self, tenant_id: str, pool_group_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PoolGroupResult:
        """
        Parameters
        ----------
        tenant_id : str

        pool_group_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PoolGroupResult
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pool_group.get_api_v1tenant_tenant_id_pool_group_pool_group_name(
            tenant_id="tenantId",
            pool_group_name="poolGroupName",
        )
        """
        _response = self._raw_client.get_api_v1tenant_tenant_id_pool_group_pool_group_name(
            tenant_id, pool_group_name, request_options=request_options
        )
        return _response.data

    def put_api_v1tenant_tenant_id_pool_group_pool_group_name(
        self,
        tenant_id: str,
        pool_group_name: str,
        *,
        display_name: str,
        region: AzureLocation,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        pool_group_name : str

        display_name : str

        region : AzureLocation

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

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
        client.pool_group.put_api_v1tenant_tenant_id_pool_group_pool_group_name(
            tenant_id="tenantId",
            pool_group_name="poolGroupName",
            display_name="displayName",
            region=1,
        )
        """
        _response = self._raw_client.put_api_v1tenant_tenant_id_pool_group_pool_group_name(
            tenant_id,
            pool_group_name,
            display_name=display_name,
            region=region,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    def delete_api_v1tenant_tenant_id_pool_group_pool_group_name(
        self, tenant_id: str, pool_group_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        pool_group_name : str

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
        client.pool_group.delete_api_v1tenant_tenant_id_pool_group_pool_group_name(
            tenant_id="tenantId",
            pool_group_name="poolGroupName",
        )
        """
        _response = self._raw_client.delete_api_v1tenant_tenant_id_pool_group_pool_group_name(
            tenant_id, pool_group_name, request_options=request_options
        )
        return _response.data

    def patch_api_v1tenant_tenant_id_pool_group_pool_group_name(
        self,
        tenant_id: str,
        pool_group_name: str,
        *,
        display_name: str,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        pool_group_name : str

        display_name : str

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

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
        client.pool_group.patch_api_v1tenant_tenant_id_pool_group_pool_group_name(
            tenant_id="tenantId",
            pool_group_name="poolGroupName",
            display_name="displayName",
        )
        """
        _response = self._raw_client.patch_api_v1tenant_tenant_id_pool_group_pool_group_name(
            tenant_id, pool_group_name, display_name=display_name, tags=tags, request_options=request_options
        )
        return _response.data


class AsyncPoolGroupClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPoolGroupClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPoolGroupClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPoolGroupClient
        """
        return self._raw_client

    async def get_api_v1tenant_tenant_id_pool_group_pool_group_name(
        self, tenant_id: str, pool_group_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PoolGroupResult:
        """
        Parameters
        ----------
        tenant_id : str

        pool_group_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PoolGroupResult
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pool_group.get_api_v1tenant_tenant_id_pool_group_pool_group_name(
                tenant_id="tenantId",
                pool_group_name="poolGroupName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1tenant_tenant_id_pool_group_pool_group_name(
            tenant_id, pool_group_name, request_options=request_options
        )
        return _response.data

    async def put_api_v1tenant_tenant_id_pool_group_pool_group_name(
        self,
        tenant_id: str,
        pool_group_name: str,
        *,
        display_name: str,
        region: AzureLocation,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        pool_group_name : str

        display_name : str

        region : AzureLocation

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

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
            await client.pool_group.put_api_v1tenant_tenant_id_pool_group_pool_group_name(
                tenant_id="tenantId",
                pool_group_name="poolGroupName",
                display_name="displayName",
                region=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1tenant_tenant_id_pool_group_pool_group_name(
            tenant_id,
            pool_group_name,
            display_name=display_name,
            region=region,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    async def delete_api_v1tenant_tenant_id_pool_group_pool_group_name(
        self, tenant_id: str, pool_group_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        pool_group_name : str

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
            await client.pool_group.delete_api_v1tenant_tenant_id_pool_group_pool_group_name(
                tenant_id="tenantId",
                pool_group_name="poolGroupName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_v1tenant_tenant_id_pool_group_pool_group_name(
            tenant_id, pool_group_name, request_options=request_options
        )
        return _response.data

    async def patch_api_v1tenant_tenant_id_pool_group_pool_group_name(
        self,
        tenant_id: str,
        pool_group_name: str,
        *,
        display_name: str,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        tenant_id : str

        pool_group_name : str

        display_name : str

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

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
            await client.pool_group.patch_api_v1tenant_tenant_id_pool_group_pool_group_name(
                tenant_id="tenantId",
                pool_group_name="poolGroupName",
                display_name="displayName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_api_v1tenant_tenant_id_pool_group_pool_group_name(
            tenant_id, pool_group_name, display_name=display_name, tags=tags, request_options=request_options
        )
        return _response.data
