

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.health_status import HealthStatus
from ..types.me_response import MeResponse
from ..types.version_info import VersionInfo
from .raw_client import AsyncRawSystemClient, RawSystemClient


class SystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSystemClient
        """
        return self._raw_client

    def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthStatus:
        """
        无需鉴权的健康检查端点，返回整体与组件级（db / worker）健康信息。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthStatus
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.system.health()
        """
        _response = self._raw_client.health(request_options=request_options)
        return _response.data

    def version(self, *, request_options: typing.Optional[RequestOptions] = None) -> VersionInfo:
        """
        无需鉴权的版本与许可证信息端点。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionInfo
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.system.version()
        """
        _response = self._raw_client.version(request_options=request_options)
        return _response.data

    def get_me(self, *, request_options: typing.Optional[RequestOptions] = None) -> MeResponse:
        """
        返回当前 token 对应的用户 ID、角色与备注名，可用于登录后路由与 token 校验。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MeResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.system.get_me()
        """
        _response = self._raw_client.get_me(request_options=request_options)
        return _response.data


class AsyncSystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSystemClient
        """
        return self._raw_client

    async def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthStatus:
        """
        无需鉴权的健康检查端点，返回整体与组件级（db / worker）健康信息。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthStatus
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.system.health()


        asyncio.run(main())
        """
        _response = await self._raw_client.health(request_options=request_options)
        return _response.data

    async def version(self, *, request_options: typing.Optional[RequestOptions] = None) -> VersionInfo:
        """
        无需鉴权的版本与许可证信息端点。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionInfo
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.system.version()


        asyncio.run(main())
        """
        _response = await self._raw_client.version(request_options=request_options)
        return _response.data

    async def get_me(self, *, request_options: typing.Optional[RequestOptions] = None) -> MeResponse:
        """
        返回当前 token 对应的用户 ID、角色与备注名，可用于登录后路由与 token 校验。

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MeResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.system.get_me()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_me(request_options=request_options)
        return _response.data
