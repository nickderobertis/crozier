

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.pool_status_response_body import PoolStatusResponseBody
from ..types.system_configuration_response import SystemConfigurationResponse
from .raw_client import AsyncRawPoolsClient, RawPoolsClient


OMIT = typing.cast(typing.Any, ...)


class PoolsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPoolsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPoolsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPoolsClient
        """
        return self._raw_client

    def post_api_v1geneva_actions_pools_change_resource_deletion_setting(
        self,
        *,
        comment: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        pool_code: typing.Optional[str] = OMIT,
        pool_type: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SystemConfigurationResponse:
        """
        Parameters
        ----------
        comment : typing.Optional[str]

        enabled : typing.Optional[bool]

        pool_code : typing.Optional[str]

        pool_type : typing.Optional[str]

        region : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemConfigurationResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pools.post_api_v1geneva_actions_pools_change_resource_deletion_setting()
        """
        _response = self._raw_client.post_api_v1geneva_actions_pools_change_resource_deletion_setting(
            comment=comment,
            enabled=enabled,
            pool_code=pool_code,
            pool_type=pool_type,
            region=region,
            request_options=request_options,
        )
        return _response.data

    def post_api_v1geneva_actions_pools_pool_code_rotate_pool(
        self, pool_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        pool_code : str

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
        client.pools.post_api_v1geneva_actions_pools_pool_code_rotate_pool(
            pool_code="poolCode",
        )
        """
        _response = self._raw_client.post_api_v1geneva_actions_pools_pool_code_rotate_pool(
            pool_code, request_options=request_options
        )
        return _response.data

    def post_api_v1geneva_actions_pools_target(
        self,
        target: str,
        *,
        comment: typing.Optional[str] = OMIT,
        max_target_count: typing.Optional[str] = OMIT,
        min_target_count: typing.Optional[str] = OMIT,
        pool_code: typing.Optional[str] = OMIT,
        pool_type: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        target_count: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SystemConfigurationResponse:
        """
        Parameters
        ----------
        target : str

        comment : typing.Optional[str]

        max_target_count : typing.Optional[str]

        min_target_count : typing.Optional[str]

        pool_code : typing.Optional[str]

        pool_type : typing.Optional[str]

        region : typing.Optional[str]

        target_count : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemConfigurationResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pools.post_api_v1geneva_actions_pools_target(
            target="target",
        )
        """
        _response = self._raw_client.post_api_v1geneva_actions_pools_target(
            target,
            comment=comment,
            max_target_count=max_target_count,
            min_target_count=min_target_count,
            pool_code=pool_code,
            pool_type=pool_type,
            region=region,
            target_count=target_count,
            request_options=request_options,
        )
        return _response.data

    def get_api_v1pools_default(
        self,
        *,
        sku_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PoolStatusResponseBody]:
        """
        Parameters
        ----------
        sku_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PoolStatusResponseBody]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pools.get_api_v1pools_default()
        """
        _response = self._raw_client.get_api_v1pools_default(sku_name=sku_name, request_options=request_options)
        return _response.data


class AsyncPoolsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPoolsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPoolsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPoolsClient
        """
        return self._raw_client

    async def post_api_v1geneva_actions_pools_change_resource_deletion_setting(
        self,
        *,
        comment: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        pool_code: typing.Optional[str] = OMIT,
        pool_type: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SystemConfigurationResponse:
        """
        Parameters
        ----------
        comment : typing.Optional[str]

        enabled : typing.Optional[bool]

        pool_code : typing.Optional[str]

        pool_type : typing.Optional[str]

        region : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemConfigurationResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pools.post_api_v1geneva_actions_pools_change_resource_deletion_setting()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1geneva_actions_pools_change_resource_deletion_setting(
            comment=comment,
            enabled=enabled,
            pool_code=pool_code,
            pool_type=pool_type,
            region=region,
            request_options=request_options,
        )
        return _response.data

    async def post_api_v1geneva_actions_pools_pool_code_rotate_pool(
        self, pool_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        pool_code : str

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
            await client.pools.post_api_v1geneva_actions_pools_pool_code_rotate_pool(
                pool_code="poolCode",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1geneva_actions_pools_pool_code_rotate_pool(
            pool_code, request_options=request_options
        )
        return _response.data

    async def post_api_v1geneva_actions_pools_target(
        self,
        target: str,
        *,
        comment: typing.Optional[str] = OMIT,
        max_target_count: typing.Optional[str] = OMIT,
        min_target_count: typing.Optional[str] = OMIT,
        pool_code: typing.Optional[str] = OMIT,
        pool_type: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        target_count: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SystemConfigurationResponse:
        """
        Parameters
        ----------
        target : str

        comment : typing.Optional[str]

        max_target_count : typing.Optional[str]

        min_target_count : typing.Optional[str]

        pool_code : typing.Optional[str]

        pool_type : typing.Optional[str]

        region : typing.Optional[str]

        target_count : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemConfigurationResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pools.post_api_v1geneva_actions_pools_target(
                target="target",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1geneva_actions_pools_target(
            target,
            comment=comment,
            max_target_count=max_target_count,
            min_target_count=min_target_count,
            pool_code=pool_code,
            pool_type=pool_type,
            region=region,
            target_count=target_count,
            request_options=request_options,
        )
        return _response.data

    async def get_api_v1pools_default(
        self,
        *,
        sku_name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PoolStatusResponseBody]:
        """
        Parameters
        ----------
        sku_name : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PoolStatusResponseBody]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pools.get_api_v1pools_default()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_v1pools_default(sku_name=sku_name, request_options=request_options)
        return _response.data
